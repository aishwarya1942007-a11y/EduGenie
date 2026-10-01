import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from the .env file.")

client = genai.Client(api_key=API_KEY)


def generate_response(prompt: str) -> str:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(
                        thinking_level="low"
                    ),
                    max_output_tokens=500
                )
            )

            return (response.text or "").strip()

        except Exception as e:
            error = str(e)

            if "503" in error and attempt < 2:
                time.sleep(3)
                continue

            return f"Error generating response: {error}"

    return "Gemini is temporarily unavailable. Please try again."