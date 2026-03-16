from fastapi import APIRouter, File, UploadFile
from src.app.schemas import TextRequest
from src.app.controllers import analyze_text_controller, analyze_document_controller

router = APIRouter()


@router.get("/ping")
def ping():
    return {"ping": "pong"}


@router.post("/analyze/text")
def analyze_text(request: TextRequest):
    return analyze_text_controller(request.text)


@router.post("/analyze/document")
async def analyze_document(file: UploadFile = File(...)):
    return await analyze_document_controller(file)
