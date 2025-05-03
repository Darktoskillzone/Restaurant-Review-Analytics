from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from vader import vader_to_stars  # your existing function
from reviews_api import router as reviews_router

# Initialize app
app = FastAPI()

# Mount the review APIs
app.include_router(reviews_router)

# Jinja2 templates folder
templates = Jinja2Templates(directory="templates")

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