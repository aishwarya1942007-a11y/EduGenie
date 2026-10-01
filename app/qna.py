from .gemini_generator import generate_response


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.
Keep the explanation concise and easy to understand.

Student question:
{question}
"""

    return generate_response(prompt)