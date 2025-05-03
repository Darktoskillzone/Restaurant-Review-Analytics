from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import get_all_reviews

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/reviews/html", response_class=HTMLResponse)
def show_reviews_page(request: Request):
    reviews = get_all_reviews()
    return templates.TemplateResponse("reviews.html", {
        "request": request,
        "reviews": reviews
    })