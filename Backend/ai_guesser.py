import os
from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("GOOGLE_API_KEY", "")

_client = None


def _get_client():
    """Create the Gemini client on first use so the server can boot without a key."""
    global _client
    if _client is None:
        if not api_key:
            raise RuntimeError(
                "GOOGLE_API_KEY is not set; create Backend/.env with your key."
            )
        _client = genai.Client(api_key=api_key)
    return _client


if not api_key:
    print("WARNING: GOOGLE_API_KEY missing - /api/guess-word will return the fallback message.")

async def guess_object(description: str) -> str:
    if not description or len(description.strip()) < 3:
        return "Description too short."

    try:
        response = _get_client().models.generate_content(
            model="models/gemini-2.5-flash-lite",
            contents=f"Guess: '{description}'. Two words only, comma separated."
        )
        
        if response and response.text:
            return response.text.strip()
        return "AI could not provide a response."

    except Exception as e:
        print(f"Cost-Oriented AI Error: {e}")
        try:
            alt = _get_client().models.generate_content(
                model="models/gemini-flash-lite-latest",
                contents=f"Guess: '{description}'. Two words."
            )
            return alt.text.strip()
        except Exception as fallback_error:
            print(f"Fallback AI Error: {fallback_error}")
            return "Guess could not be retrieved."