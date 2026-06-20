from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
app = FastAPI()

tasks = []


class Task(BaseModel):
    title: str
    done: bool = False


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.dict())
    return task
