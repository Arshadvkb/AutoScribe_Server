from fastapi import HTTPException, UploadFile
import fitz  # PyMuPDF
from src.app.ai_services import ai

def generate_analysis_prompt(text: str) -> str:
    return f""" 
        
        You are an expert study assistant.
        Your task is to analyze the given text and convert it into clear study material.

        Instructions:

        1. Carefully read and understand the provided text.
        2. Create well-structured **study notes** that simplify the content while preserving the important ideas.
        3. Extract the **most important key points** in bullet format.
        4. Generate a **brain map (mind map)** that visually represents the relationships between concepts. 
        - Use a hierarchical structure.
        - Show the main topic at the center and branches for subtopics.

        Output Format:

        1. Title of the Topic

        2. Summary
        Provide a short 3-5 sentence explanation of the topic.

        3. Detailed Notes
        Create structured notes with headings and subheadings.

        4. Key Points
        - Point 1
        - Point 2
        - Point 3
        - etc.

        5. Brain Map (Text Format)

        Main Topic
        - Subtopic 1
          - Key idea
          - Key idea
        - Subtopic 2
          - Key idea
          - Key idea
        - Subtopic 3
          - Key idea
          - Key idea

        Rules:
        - Keep explanations simple and concise.
        - Do not include unnecessary information.
        - If the text contains complex concepts, simplify them for easier understanding.
        - Maintain logical structure.

        Text to Analyze:
        {text}
        """


def analyze_text_controller(text: str):
    try:
        prompt = generate_analysis_prompt(text)
        res = ai(prompt)
        print(f"AI analysis result: {res}")
        return {"text": text, "analysis": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def analyze_document_controller(file: UploadFile):
    try:
        content = await file.read()
        filename = file.filename
        ext = filename.split(".")[-1].lower() if "." in filename else ""

        text = ""
        if ext == "pdf":
            doc = fitz.open(stream=content, filetype="pdf")
            for page in doc:
                text += page.get_text()
        elif ext in ["txt", "md", "csv"]:
            text = content.decode("utf-8")
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format. Please upload a PDF, TXT, MD, or CSV.")

        if not text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from document or document is empty.")

        prompt = generate_analysis_prompt(text)
        res = ai(prompt)
        print(f"AI document analysis result: {res}")
        return {"filename": filename, "analysis": res}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
