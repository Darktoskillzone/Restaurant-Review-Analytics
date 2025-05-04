import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .vader import vader_to_stars  # your existing function
from .database import get_all_reviews

# Initialize app
app = FastAPI()

# Jinja2 templates folder
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

# Route to render the form page
@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to handle form submission
@app.post("/predict", response_class=HTMLResponse)
async def predict_sentiment(request: Request, review: str = Form(...)):
    stars, scores = vader_to_stars(review)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "review": review,
        "stars": stars,
        "scores": scores
    })

@app.get("/reviews/html", response_class=HTMLResponse)
def show_reviews_page(request: Request):
    reviews = get_all_reviews()
    return templates.TemplateResponse("reviews.html", {
        "request": request,
        "reviews": reviews
    })