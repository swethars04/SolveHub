import pyttsx3
import os
import requests
from dotenv import load_dotenv
from PIL import Image
import pytesseract
import speech_recognition as sr
from pydub import AudioSegment
import io
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from utils.ocr import extract_text_from_image
from utils.voice import voice_to_text
from utils.solver import solve_math_problem
from werkzeug.utils import secure_filename
from models import db, MathProblem


# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)
engine = pyttsx3.init()
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ask Groq API
def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful AI math tutor."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"\u274c Error {response.status_code}: {response.text}"
    
# Add this route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Add these configurations after creating Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///math_tutor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create tables (add this before running the app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index1.html')

def text_to_audio(text):
    audio_file = "static/audio/response.mp3"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    return audio_file

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400
        
        image = request.files['image']
        if image.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)

        # Extract text from image
        question = extract_text_from_image(filepath)
        
        # Get solution from Groq
        solution = solve_math_problem(question)

        audio_file = text_to_audio(solution)

        # Save to database with web-accessible path
        math_problem = MathProblem(
            question=question,
            solution=solution,
            input_type='image',
            image_path=url_for('uploaded_file', filename=filename)
        )
        db.session.add(math_problem)
        db.session.commit()

        return jsonify({
            'question': question,
            'solution': solution,
            'audio_url': f'/{audio_file}'
           
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/process-voice', methods=['POST'])
def process_voice():
    try:
        question = voice_to_text()
        solution = solve_math_problem(question)
        audio_file = text_to_audio(solution)
        
        # Save to database
        math_problem = MathProblem(
            question=question,
            solution=solution,
            input_type='voice'
        )
        db.session.add(math_problem)
        db.session.commit()
        
        return jsonify({
            'question': question,
            'solution': solution,
            'audio_url': f'/{audio_file}'
            
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_answer', methods=['POST'])
def get_answer():
    question = request.json.get('question', '')
    if not question.strip():
        return jsonify({'answer': 'Please provide input', 'audio_url': ''})
    answer = ask_groq(question)
    audio_url = text_to_audio(answer)
    return jsonify({'answer': answer, 'audio_url': f'/{audio_url}'})

if __name__ == '__main__':
    app.run(debug=True)
