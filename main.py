from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

class Task(BaseModel):
    title: str
    done: bool = False


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.dict())
    return task.dict()
