# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is an AI-powered educational assistant designed to help students understand, practice, and learn concepts more effectively using Google Gemini.

## Features

- Ask questions and receive concise AI-powered answers
- Explain complex concepts in simple language
- Generate multiple-choice quizzes
- Summarize educational passages
- Generate personalized learning paths and recommendations

## Technology Stack

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- Jinja2
- Uvicorn

## Project Structure

```text
EduGenie/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── gemini_generator.py
│   ├── qna.py
│   ├── explanation_module.py
│   ├── quiz_module.py
│   ├── summary_module.py
│   ├── learning_path.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── tests/
│   └── test_app.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
└── README.md