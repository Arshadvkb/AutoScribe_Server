from fastapi import APIRouter

from app.ai_services import ai
from app.schemas import TextRequest

router = APIRouter()


@router.get("/ping")
def ping():
    return {"ping": "pong"}

@router.post("/analyze/text")
def analyze_text(text:TextRequest):
    print(f"Received text for analysis: {text}")


    try:
        prompt = f""" 
        
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
        Provide a short 3–5 sentence explanation of the topic.

        3. Detailed Notes
        Create structured notes with headings and subheadings.

        4. Key Points
        - Point 1
        - Point 2
        - Point 3
        - etc.

        5. Brain Map (Text Format)

        Main Topic
        ├── Subtopic 1
        │   ├── Key idea
        │   └── Key idea
        ├── Subtopic 2
        │   ├── Key idea
        │   └── Key idea
        └── Subtopic 3
            ├── Key idea
            └── Key idea

        Rules:
        - Keep explanations simple and concise.
        - Do not include unnecessary information.
        - If the text contains complex concepts, simplify them for easier understanding.
        - Maintain logical structure.

        Text to Analyze:
        {text}
        """

        res = ai(prompt)
        print(f"AI analysis result: {res}")

        return {"text": text, "analysis":res}
    except Exception as e:
        return {"error in ai analysis": str(e)}