from fastapi import APIRouter, File, UploadFile, Query
from fastapi.responses import Response
from src.app.schemas import TextRequest
from src.app.controllers import analyze_text_controller, analyze_document_controller
from src.app.pdf_generator import generate_pdf_from_markdown

router = APIRouter()


@router.get("/ping")
def ping():
    return {"ping": "pong"}


@router.post(
    "/analyze/text",
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Returns a JSON analysis or a downloadable PDF file depending on the format query.",
        }
    },
)
def analyze_text(request: TextRequest, format: str = Query("json", description="Output format: json or pdf")):
    result = analyze_text_controller(request.text)
    if format.lower() == "pdf":
        pdf_bytes = generate_pdf_from_markdown(result["analysis"])
        return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=analysis.pdf"})
    return result


@router.post(
    "/analyze/document",
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Returns a JSON analysis or a downloadable PDF file depending on the format query.",
        }
    },
)
async def analyze_document(file: UploadFile = File(...), format: str = Query("json", description="Output format: json or pdf")):
    result = await analyze_document_controller(file)
    if format.lower() == "pdf":
        pdf_bytes = generate_pdf_from_markdown(result["analysis"])
        pdf_filename = f"{result['filename']}_analysis.pdf"
        return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename={pdf_filename}"})
    return result
