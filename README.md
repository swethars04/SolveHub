# SolveHub
@@ -0,0 +1,138 @@
![github-submission-banner](https://github.com/user-attachments/assets/a1493b84-e4e2-456e-a791-ce35ee2bcf2f)
 
 # 🚀 Project Title
 
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
 
 
 ### Your Approach:  
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
 
 ### Sponsor Technologies Used (if any):
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
 
 Add images, GIFs, or screenshots if helpful!
 
 ---
 
 ## 📽️ Demo & Deliverables
 
 - **Demo Video Link:** [Paste YouTube or Loom link here]  
 - **Pitch Deck / PPT Link:** [Paste Google Slides / PDF link here]  
 
 ---
 
 ## ✅ Tasks & Bonus Checklist
 
 - ✅ **All members of the team completed the mandatory task - Followed at least 2 of our social channels and filled the form** (Details in Participant Manual)  
 - ✅ **All members of the team completed Bonus Task 1 - Sharing of Badges and filled the form (2 points)**  (Details in Participant Manual)
 - ✅ **All members of the team completed Bonus Task 2 - Signing up for Sprint.dev and filled the form (3 points)**  (Details in Participant Manual)
 
 *(Mark with ✅ if completed)*
 
 ---
 
 ## 🧪 How to Run the Project
 
 ### Requirements:
 - Node.js / Python / Docker / etc.
 - API Keys (if any)
 - .env file setup (if needed)
 
 ### Local Setup:
 ```bash
 # Clone the repo
 git clone https://github.com/your-team/project-name
 
 # Install dependencies
 cd project-name
 npm install
 
 # Start development server
 npm run dev
 ```
 
 Provide any backend/frontend split or environment setup notes here.
 
 ---
 
 ## 🧬 Future Scope
 
 List improvements, extensions, or follow-up features:
 
 - 📈 More integrations  
 - 🛡️ Security enhancements  
 - 🌐 Localization / broader accessibility  
 
 ---
 
 ## 📎 Resources / Credits
 
 - APIs or datasets used  
 - Open source libraries or tools referenced  
 - Acknowledgements  
 
 ---
 
 ## 🏁 Final Words
 
 Share your hackathon journey — challenges, learnings, fun moments, or shout-outs!
 
 ---
