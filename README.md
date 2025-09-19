# Techies.
![github-submission-banner](https://github.com/user-attachments/assets/a1493b84-e4e2-456e-a791-ce35ee2bcf2f)
 
 # **SolveHub**
 
 >**One Hub.Every Solution**
 
 ---
 
 ## 📌 Problem Statement
  
 **Problem Statement 1 – Weave AI magic with Groq**
 
 ---
 
 ## 🎯 Objective

The proposed system is an AI-powered Math Tutor Web Application that can accept mathematical queries through images, voice, or text. It provides accurate solutions using a Large Language Model (LLM) API (Groq with LLaMA3), enhancing user interactivity with text-to-speech feedback and persistent query storage via a database.
 
 ---
 
 ## 🧠 Team & Approach
 
 ### Team Name:  
 `Techies`
 
 ### Team Members:  
 - VEGAVATHI GB   
 - VIBUSSHANI N.S  
 - SWETHA RS  
 
 
 ### Our Approach:  
 - Why we chose this problem:
   We wanted to make math more accessible and engaging by helping students solve math problems through voice or image input. Many learners struggle with typing or don’t have access to tutors, so a multi-input AI tutor can really help 
 - Key challenges we addressed:
   Extracting clear text from images (especially handwritten or unclear text).
   Converting speech to text accurately for math questions.
   Getting reliable math solutions from the AI (using Groq API).
   Giving audio feedback so it’s accessible for all types of users.
   Storing and retrieving solved problems using a database 
 - pivots, brainstorms, or breakthroughs during hacking:
   At first, we were only going to use text input, but then realized many users might prefer using voice or images, so we expanded it.
   We had issues with accuracy in OCR (image text extraction), so we tested different libraries and tweaked image handling.
   We integrated Groq’s powerful model instead of a simple rule-based solver for better math problem-solving.
   We added audio responses to make the experience feel more interactive and inclusive.  
 
 ---
 
 ## 🛠️ Tech Stack
 
 ### Core Technologies Used:
 - Frontend:
     -HTML/CSS: For designing the webpage layout and styling.
     -JavaScript: For adding interactivity and dynamic elements on the page.
     -Flask: Used for rendering templates and managing routes in the web application.
 - Backend:
     -Python: The main programming language for backend logic and processing requests.
     -Flask: A Python framework used to handle HTTP requests, routes, and logic for the app.
     -Pyttsx3: For converting text into speech (audio feedback for the users).
     -pytesseract: For OCR (Optical Character Recognition), extracting text from images.
     -SpeechRecognition: For converting speech (voice input) into text.
 - Database:
     -SQLite: A lightweight, file-based database used to store math problems and their solutions.
 - APIs:
     - Groq API: Provides AI-driven solutions for math problems (via chat completions).
 - Hosting:
 
 ### Sponsor Technologies Used:
 - ✅ **Groq:** Used Groq’s llama3-70b-8192 model as a math tutor to solve user-submitted math problems. The API is integrated via an endpoint that accepts a prompt (text extracted from image/voice or direct input) and sends it to Groq’s chat completion API. The response, containing a detailed solution, is returned and also converted to speech using pyttsx3. This allows users to get both textual and audio explanations for math problems.  

 ---
 
 ## ✨ Key Features
 
 - ✅ Image-Based Math Problem Solving
       Users can upload images containing handwritten or printed math problems. The app uses OCR (via Tesseract) to extract the question and sends it to the Groq API for solving. 
 - ✅ Voice-Based Math Query Support
       Users can ask math questions by voice. The audio is converted to text using speech recognition and then solved by the Groq-powered math tutor.
 - ✅ AI-Powered Math Tutor (Groq Integration)
       The app utilizes Groq's llama3-70b-8192 model to generate accurate and detailed solutions for math problems, simulating a helpful AI tutor.
 - ✅ Text-to-Speech Response Generation
       Every solution generated is converted to speech using pyttsx3, allowing users to hear the answer—enhancing accessibility and ease of use.  
 - ✅ Database connectivity
       Every question asked and solution generated is saved in a database which can helpful in future for further training the model.
 Add images, GIFs, or screenshots if helpful!
<img width="800" alt="image" src="https://github.com/user-attachments/assets/ce12d0ce-af95-4660-8f62-ba1fac3b3943" />
<img width="960" alt="image1" src = "https://github.com/user-attachments/assets/2253892a-fd65-4090-80e5-f051c15acede"/>
<img width="960" alt="image1" src = "https://github.com/user-attachments/assets/c1cb8ee6-380a-48d4-b8b3-41b401c4fd2b"/>

 ---
 
 ## 📽️ Demo & Deliverables
 
 - **Demo Video Link:** https://drive.google.com/file/d/1m0fLnK1dcHngPZ_q57iiSci2buygApLn/view?usp=sharing 
 - **Pitch Deck / PPT Link:** https://docs.google.com/presentation/d/1Ru8F8t_VtSiQWh9b-p_6BFKhW76V4Gy8sqMvsBwd1oY/edit?usp=sharing   
 
 ---
 
 ## ✅ Tasks & Bonus Checklist
 
 - ✅ **All members of the team completed the mandatory task - Followed at least 2 of our social channels and filled the form**  
 - ✅ **All members of the team completed Bonus Task 1 - Sharing of Badges and filled the form (2 points)**  
 - ✅ **All members of the team completed Bonus Task 2 - Signing up for Sprint.dev and filled the form (3 points)**  
 
 ---
 
 ## 🧪 How to Run the Project
 
 ### Requirements:
 - Python 3.8+
 - Tesseract OCR (for image-to-text)
 - FFmpeg (required by pydub)
 - **The following Python libraries:**
    - Flask
    - pyttsx3
    - SpeechRecognition
    - python-dotenv
    - requests
    - Pillow
    - pydub
    - SQLAlchemy
 - API Keys : Groq API Key
 - .env file setup:
    - Create a .env file in the root folder and add:
         - GROQ_API_KEY=your_groq_api_key_here
 
 ### Local Setup:
 ```bash
 # Clone the repo
 git clone https://github.com/Vegavathi/Techies.git
 
 # Install dependencies
 cd project-name
 npm install
 
 # Start development server
 npm run dev
 ```
 
 **Notes:**
 - Make sure Tesseract and FFmpeg are installed and added to your system PATH.
 - Uploaded images are saved in the uploads/ folder.
 - Audio responses are saved in the static/audio/ folder.
 - Access the app in your browser at: http://127.0.0.1:5000/
 ---
 
 ## 🧬 Future Scope
 
 List improvements, extensions, or follow-up features:
 
- 📈 More Integrations
    - Connect with platforms like Google Classroom, Microsoft Teams, or educational LMS systems to reach more students.

- 🛡️ Security Enhancements
    - Implement user authentication and secure API handling to ensure safe and private access to learning data.

- 🚀 Interactive Learning Modules
    - Introduce quizzes, step-by-step problem solving, and personalized learning paths.

- 🎓 Gamified Learning Experience
    - Add leaderboards, badges, and daily challenges to motivate students to solve more problems and improve continuously.
      
- 🤝 Peer Learning & Discussion Boards
    - Let students connect with each other, post their doubts, and solve problems collaboratively in a safe and moderated environment.
 
 ---
 
 ## 📎 Resources / Credits
 
 - 🔌 APIs & Services
     - Groq API – Used to generate accurate and clear math solutions through the LLaMA3 model.
     - Tesseract OCR – For extracting handwritten or printed text from uploaded math images.
 - Open source libraries or tools referenced
     - Flask 
     - SQLAlchemy 
     - SpeechRecognition 
     - pyttsx3 
     - pydub
     - dotenv 
     - Pillow (PIL)
 - Acknowledgements
     - Inspired by the vision of open and accessible math education for all.
     - Thanks to the open-source community for providing these incredible tools.
     - Special shoutout to Groq for enabling high-quality, low-latency AI interactions via their powerful models. 
 ---
 
 ## 🏁 Final Words
 Building SolveHub was an exciting and meaningful experience! 🚀
 
 We tackled challenges like combining OCR, voice input, and AI-generated solutions into one smooth workflow. Along the way, we learned a lot about real-time processing, user interaction, and API integration using Groq.

🧠 It was awesome to see how AI can truly help make education more accessible and engaging.

🎉 One of the best moments was hearing the app speak back the solution — it really felt like bringing a smart tutor to life!

🙏 Huge thanks to the Groq team for their powerful API, and to all open-source contributors whose tools made this project possible.

We're proud of what we built and excited to grow SolveHub into a go-to AI learning companion! 🌟


 ---
