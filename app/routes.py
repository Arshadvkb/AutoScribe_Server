from fastapi import APIRouter

from app.ai_services import ai

router = APIRouter()


@router.get("/ping")
def ping():
    return {"ping": "pong"}

@router.post("/analyze/text")
def analyze_text(text: str):
    try:
        prompt = f"Analyze the following text and provide insights: {text}"
        res = ai(prompt)

        return {"text": text, "analysis":res}
    except Exception as e:
        return {"error in ai analysis": str(e)}