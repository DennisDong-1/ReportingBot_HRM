# ===========================================
# 📄 agent.py
# AI Agent layer for HR Reporting Bot
# Handles reasoning + Hugging Face model connection
# ===========================================

import os
import requests
from dotenv import load_dotenv
from db import get_employee_info

# Load environment variables
load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not HF_API_KEY:
    raise ValueError("❌ Missing Hugging Face API key in .env file!")

# Model from Hugging Face
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"  # You can switch to "tiiuae/falcon-7b-instruct"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}


def query_huggingface(prompt: str) -> str:
    """Send text to Hugging Face model and get AI-generated response."""
    payload = {"inputs": prompt}
    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HF_MODEL}",
            headers=HEADERS,
            json=payload,
        )

        if response.status_code != 200:
            print("Hugging Face API Error:", response.text)
            return "Sorry, I couldn’t reach the AI model right now."

        data = response.json()
        if isinstance(data, list):
            return data[0].get("generated_text", "No response generated.")
        return data.get("generated_text", "No response generated.")

    except Exception as e:
        print("❌ HF Request Error:", e)
        return "There was a problem reaching the AI model."


def process_query(user_input: str) -> str:
    """Decides if the query needs DB info or AI reasoning."""
    user_input_lower = user_input.lower()

    # --- If it’s about HR data, query DB ---
    if any(word in user_input_lower for word in ["employee", "salary", "department", "attrition"]):
        db_response = get_employee_info(user_input_lower)
        if db_response:
            return db_response

    # --- Otherwise, ask the Hugging Face model ---
    prompt = f"You are an HR assistant bot. Answer this HR-related question clearly:\n\n{user_input}"
    return query_huggingface(prompt)
