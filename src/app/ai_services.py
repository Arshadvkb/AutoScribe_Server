import google.genai as genai
import os

api_key=os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=api_key)

def ai(prompt: str):
        try:
            
            response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
            )

       
            if response.text:
                return response.text
            else:
                return "The model returned an empty response."
                
        except Exception as e:
      
            print(f"GenAI Error: {e}")
            return f"AI Service Error: {str(e)}"