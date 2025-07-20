import os
import google.generativeai as genai
from dotenv import load_dotenv

# 🔐 Load the API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# ✅ Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# 🎓 Smart Student Agent Function
def smart_student_agent(prompt):
    if prompt.startswith("summarize:"):
        text = prompt[len("summarize:"):].strip()
        return model.generate_content(f"Please summarize this text: {text}").text
    
    elif prompt.startswith("tips:"):
        topic = prompt[len("tips:"):].strip()
        return model.generate_content(f"Give 3 study tips for: {topic}").text
    
    elif prompt.startswith("ask:"):
        question = prompt[len("ask:"):].strip()
        return model.generate_content(f"Answer this academic question: {question}").text

    else:
        return model.generate_content(prompt).text

# 💬 Simple Command-Line Chat Loop
print("🎓 Smart Student Agent (Gemini) is ready! Type 'exit' to quit.\n")
print("Examples:\n- ask: What is gravity?\n- tips: time management\n- summarize: Plants need water to grow...\n")

while True:
    user_input = input("👩‍🎓 You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    try:
        answer = smart_student_agent(user_input)
        print("\n🤖 Answer:\n" + answer + "\n")
    except Exception as e:
        print("⚠️ Error:", e)
