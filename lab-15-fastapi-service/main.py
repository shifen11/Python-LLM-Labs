"""
lab-12-fastapi-service: 高性能 Web 接口（FastAPI）

运行方式: uvicorn main:app --reload
然后访问 http://127.0.0.1:8000 与 http://127.0.0.1:8000/docs

本文件展示：路由、路径参数、查询参数、请求体（Pydantic）、以及自动 OpenAPI 文档。
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Python-LLM-Labs FastAPI Demo")

# 请求体模型：自动校验 + 文档
class EchoBody(BaseModel):
    message: str
    repeat: int = 1


# GET /  -> 根路径
@app.get("/")
def root():
    """根路径，返回欢迎与文档链接"""
    return {"hello": "Python-LLM-Labs", "docs": "/docs"}


# GET /items/{item_id}  -> 路径参数 item_id；q 为查询参数（可选）
@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    """路径参数 + 查询参数；类型注解会自动校验与文档"""
    return {"item_id": item_id, "q": q}


# POST /echo  -> 请求体为 JSON，自动反序列化为 EchoBody
@app.post("/echo")
def echo(body: EchoBody):
    """请求体校验由 Pydantic 完成；无效类型会返回 422"""
    return {"echo": (body.message + " ") * body.repeat, "repeat": body.repeat}


if __name__ == "__main__":
    import uvicorn
    # 直接运行 python main.py 时启动服务
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
