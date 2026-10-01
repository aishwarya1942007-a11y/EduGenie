from .gemini_generator import generate_response


def generate_quiz(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly 3 multiple-choice questions based on the given text.

For each question provide:
- Question
- Four options labeled A, B, C, D
- Correct answer
- A short explanation

Make the questions educational and relevant to the provided content.

Text:
{text}
"""

    return generate_response(prompt)