import os

import google.genai as genai

_API_KEY_ENV = "GENAI_API_KEY"
_client = None


def _get_client():
    global _client
    if _client is not None:
        return _client

    api_key = os.getenv(_API_KEY_ENV)
    if not api_key:
        raise RuntimeError(f"Missing {_API_KEY_ENV} environment variable.")

    _client = genai.Client(api_key=api_key)
    return _client

def ai(prompt: str):
    try:
        client = _get_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text

        return "The model returned an empty response."
    except Exception as e:
        print(f"GenAI Error: {e}")
        return f"AI Service Error: {str(e)}"


def models():
    client = _get_client()
    for model in client.models.list():
        print(f"Name: {model.name}")
        print(f"  Display Name: {model.display_name}")
        print(f"  Supported Methods: {model.supported_generation_methods}")
        print("-" * 20)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    models()