from .gemini_generator import generate_response


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a structured learning path for the following topic.

Organize it into:
1. Beginner level
2. Intermediate level
3. Advanced level

For each level include:
- Topics to learn
- Suggested learning resources
- Practical activities or exercises

Also provide a simple suggested timeline.

Topic:
{topic}
"""

    return generate_response(prompt)