from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib

from database import get_connection

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = joblib.load("model.pkl")


@app.get("/")
def read_root():
    return {"message": "AI Backend Running"}


@app.get("/predict")
def predict(marks: int):

    prediction = model.predict([[marks]])

    if prediction[0] == 1:
        result = "Pass"
    else:
        result = "Fail"

    # Save to MySQL
    connection = get_connection()

    if connection:
        cursor = connection.cursor()

        query = """
        INSERT INTO predictions (marks, result)
        VALUES (%s, %s)
        """

        cursor.execute(query, (marks, result))

        connection.commit()

        cursor.close()
        connection.close()

    return {"prediction": result}