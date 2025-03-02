# chat.py
from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from database.query_functions import get_user_interactions_by_email
from langchain_groq import ChatGroq
from core.retrieve_input_data import retrieve_input_data
from shopsense_llm.chains import retireve_answer

router = APIRouter()
templates = Jinja2Templates(directory="templates")


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_retries=2,
)


@router.get("/chat")
async def chat_page(request: Request):
    """Handle chat page access, ensuring user authentication"""
    user: str | None = request.session.get("user")

    if not user:
        return RedirectResponse(url="/login", status_code=303)

    # Fetch user interactions
    user_interaction = await get_user_interactions_by_email(user)
    if not user_interaction:
        user_interaction = {"view": [], "wishlist": []}

    return templates.TemplateResponse(
        "chat.html",
        {"request": request, "user": user, "user_interaction": user_interaction},
    )


@router.post("/api/chat")
async def chat_message(request: Request, message: dict) -> dict:
    """Process authenticated chat messages"""
    user: str | None = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401)
    question = message["message"]
    user: str | None = request.session.get("user")
    input_data = await retrieve_input_data(user, question, llm)
    answer = await retireve_answer(input_data, llm)

    return {"response": answer}


