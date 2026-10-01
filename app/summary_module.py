from .gemini_generator import generate_response


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following passage into a concise,
easy-to-understand version.

Keep the important information.
Remove unnecessary repetition.
Use bullet points when useful.

Passage:
{text}
"""

    return generate_response(prompt)