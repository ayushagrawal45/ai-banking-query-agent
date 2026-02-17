import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_data():
    data = ""
    for file in ["data/faqs.txt", "data/policies.txt", "data/branches.txt"]:
        with open(file, "r", encoding="utf-8") as f:
            data += f.read() + "\n"
    return data

BANK_DATA = load_data()

def get_response(user_query):
    prompt = f"""
You are an AI banking customer support assistant.

Answer ONLY using the banking data below.
If the question is not answerable or is complex, reply exactly with:
"This query requires human assistance."

BANK DATA:
{BANK_DATA}

USER QUESTION:
{user_query}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=300
    )

    return completion.choices[0].message.content.strip()
