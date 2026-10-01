from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .qna import answer_question
from .explanation_module import explain_topic
from .quiz_module import generate_quiz
from .summary_module import summarize_text
from .learning_path import get_learning_recommendations


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post("/process", response_class=HTMLResponse)
async def process(
    request: Request,
    task: str = Form(...),
    text: str = Form(...)
):
    if task == "qa":
        result = answer_question(text)

    elif task == "explain":
        result = explain_topic(text)

    elif task == "quiz":
        result = generate_quiz(text)

    elif task == "summarize":
        result = summarize_text(text)

    elif task == "learning":
        result = get_learning_recommendations(text)

    else:
        result = "Please select a valid task."

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result,
            "selected_task": task,
            "user_text": text
        }
    )