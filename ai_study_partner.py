import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz(notes_text, num_questions=5):
    prompt = f"""
    You are an AI Study Partner. Read these notes and create {num_questions} quiz questions 
    with clear answers to help the user learn effectively.
    Notes:
    {notes_text}
    """
    
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)

    return response.text

if __name__ == "__main__":
    print("Welcome to AI Study Partner !")
    notes = input("Paste your study notes below:\n\n")
    num_q = input("\nHow many quiz questions do you want? (default: 5): ")
    num_q = int(num_q) if num_q.strip() else 5

    print("\n Generating your quiz...\n")
    quiz = generate_quiz(notes, num_q)
    print("Here’s your personalized quiz:\n")
    print(quiz)
