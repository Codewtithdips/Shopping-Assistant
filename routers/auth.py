from fastapi import APIRouter, Form, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.templating import _TemplateResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

USERS = {
    "debnathdpankar27@gmail.com": {
        "password": "12345612",  # In real app, use hashed passwords
        "user_id": 1,
    }
}


@router.get("/login")
def login_page(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(request: Request, email: str = Form(), password: str = Form()):
    if email not in USERS or USERS[email]["password"] != password:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Invalid email or password"},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    request.session["user"] = email
    return RedirectResponse(url="/chat", status_code=303)


@router.get("/logout")
async def logout(request: Request) -> RedirectResponse:
    request.session.clear()
    return RedirectResponse(url="/login")
