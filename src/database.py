import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def get_all_reviews():
    conn = get_connection() 
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reviews;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def insert_review(review_text, stars):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reviews (review_text, stars) VALUES (%s, %s);",
        (review_text, stars)
    )
    conn.commit()

    cursor.close()
    conn.close()