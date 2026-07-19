import os
from dotenv import load_dotenv
import google.generativeai as genai

from prompt import build_prompt

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

NO_RESEARCH_MSG = "No trustworthy recent news was found for this company."


def generate_email(resume, company, role, sources, recipient_name=""):
    if sources:
        research_text = ""
        for s in sources:
            research_text += f"- {s['title']}\n{s['summary']}\n\n"
    else:
        research_text = NO_RESEARCH_MSG

    prompt = build_prompt(
        resume=resume,
        company=company,
        role=role,
        research=research_text,
        recipient_name=recipient_name,
    )

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        if text.upper().startswith("SUBJECT:"):
            subject_line, _, body = text.partition("\n")
            subject = subject_line.split(":", 1)[1].strip()
            body = body.strip()
        else:
            subject = ""
            body = text

        return {"subject": subject, "email": body}

    except Exception as e:
        print("Gemini Error:", e)
        raise