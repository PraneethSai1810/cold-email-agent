from unittest import result
from urllib import request

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from search import search_company
from llm import generate_email
from resume_extract import extract_resume_text

app = FastAPI(title="Cold Email Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):
    resume: str
    company: str
    role: str = ""
    recipient_name: str = ""


@app.get("/")
def root():
    return {"message": "Cold Email Agent API is running 🚀"}


@app.post("/extract-resume")
async def extract_resume(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        text = extract_resume_text(file.filename, file_bytes)

        if not text.strip():
            raise HTTPException(status_code=400, detail="Couldn't extract text. Try pasting manually.")

        return {"resume_text": text}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Resume extraction error: {e}")
        raise HTTPException(status_code=500, detail="Failed to process file.")


@app.post("/generate-email")
def generate(request: EmailRequest):
    if not request.resume.strip():
        raise HTTPException(status_code=400, detail="Resume is required.")

    if not request.company.strip():
        raise HTTPException(status_code=400, detail="Company name is required.")

    sources = search_company(request.company)

    result = generate_email(
        resume=request.resume,
        company=request.company,
        role=request.role,
        sources=sources,
        recipient_name=request.recipient_name,
    )

    display_sources = [s for s in sources if s["quality"] >= 2]
    result["sources"] = display_sources

    return result