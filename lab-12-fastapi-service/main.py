"""
lab-12-fastapi-service: 高性能 Web 接口
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Python-LLM-Labs FastAPI Demo")


class EchoBody(BaseModel):
    message: str
    repeat: int = 1


@app.get("/")
def root():
    return {"hello": "Python-LLM-Labs", "docs": "/docs"}


@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/echo")
def echo(body: EchoBody):
    return {"echo": (body.message + " ") * body.repeat, "repeat": body.repeat}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
