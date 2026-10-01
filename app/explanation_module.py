from .gemini_generator import generate_response


def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.

Explain the following topic in simple language for a beginner.
Use short sections or bullet points where helpful.
Avoid unnecessary technical jargon.

Topic:
{topic}
"""

    return generate_response(prompt)