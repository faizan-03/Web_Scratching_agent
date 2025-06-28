import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

def summarize_with_gemini(prompt: str) -> str:
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"[Gemini Error] summarize_with_gemini: {e}")
        return "Summary unavailable due to an error."

def expand_with_gemini(subtopic: str, summary: str = "") -> str:
    try:
        prompt = f"""
        Write a detailed, academic-style report section on the topic: "{subtopic}".
        {'Here is a short summary to base your expansion on:\n' + summary if summary else ''}
        
        Please include:
        - A brief introduction
        - In-depth explanation
        - Real-world examples
        - Statistics or citations if applicable
        - Clear transitions and good structure

        Length: At least 700–1000 words.
        """
        response = gemini_model.generate_content(prompt.strip())
        return response.text
    except Exception as e:
        print(f"[Gemini Error] expand_with_gemini: {e}")
        return "Expansion unavailable due to an error."
