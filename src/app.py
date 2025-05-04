import os
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .vader import vader_to_stars  # your existing function
from .database import get_all_reviews

BASE_DIR = Path(__file__).resolve().parent

# Initialize app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Jinja2 templates folder
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to render the form page
@app.get("/sentiment", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("sentiment.html", {"request": request})

# Route to handle form submission
@app.post("/sentiment/predict", response_class=HTMLResponse)
async def predict_sentiment(request: Request, review: str = Form(...)):
    stars, scores = vader_to_stars(review)
    return templates.TemplateResponse("sentiment.html", {
        "request": request,
        "review": review,
        "stars": stars,
        "scores": scores
    })

@app.get("/reviews/show", response_class=HTMLResponse)
def show_reviews_page(request: Request):
    reviews = get_all_reviews()
    return templates.TemplateResponse("reviews.html", {
        "request": request,
        "reviews": reviews
    })