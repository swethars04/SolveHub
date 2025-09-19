import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "You are a math tutor."},
        {"role": "user", "content": "What is 2 + 2?"}
    ],
    "temperature": 0.2
}

response = requests.post(url, headers=headers, json=payload)

print(f"Status code: {response.status_code}")
print("Response:", response.json())
