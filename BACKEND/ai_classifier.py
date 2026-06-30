import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")


def classify_issue(description):

    prompt = f"""
You are an AI assistant for a civic issue reporting platform.

Classify this issue:

{description}

Return ONLY valid JSON in this exact format:

{{
    "category": "Pothole",
    "severity": "High"
}}

Do not add explanations.
Do not use markdown.
Do not use ```json.
Return only pure JSON.
"""

    response = model.generate_content(prompt)

    print("\n===== GEMINI RAW RESPONSE =====")
    print(response.text)
    print("===============================\n")

    text = response.text.strip()

    # Remove markdown if Gemini adds it
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)