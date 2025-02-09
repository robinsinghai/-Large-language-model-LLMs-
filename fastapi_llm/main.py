from fastapi import FastAPI, Query
from models import load_text_model, generate_text

def check_age(age: int) -> bool:
    return age>= 18

app = FastAPI()


@app.get("/generate/text")
def serve_language_model_controller(prompt=Query(...)):
    pipe = load_text_model()
    output = generate_text(pipe, prompt)
    return output

