# lab-12-fastapi-service

**高性能 Web 接口（类似 Spring Boot 控制层）**

## 知识点

- FastAPI 路由、请求体、响应模型
- Pydantic 集成、自动 OpenAPI 文档
- `uvicorn` 启动 ASGI 应用

## 运行

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

然后访问：

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## 练习题

练习题见 [exercises.py](./exercises.py)，在 lab 目录下实现路由后运行 `uvicorn exercises:app --reload` 自测。
