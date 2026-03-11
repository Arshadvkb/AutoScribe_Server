import google.generativeai as genai
import os

api_key=os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)

def ai(prompt: str):
        try:
  
          model = genai.GenerativeModel("gemini-2.5-flash-lite")
         
          response = model.generate_content(prompt)
        
       
          if response.text:
                return response.text
          else:
                return "The model returned an empty response."
                
        except Exception as e:
      
            print(f"GenAI Error: {e}")
            return f"AI Service Error: {str(e)}"