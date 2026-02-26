"""
lab-12 练习题：FastAPI
运行: 先完成下方代码，再在终端执行 uvicorn exercises:app --reload，用浏览器或 curl 测试
需安装: pip install fastapi uvicorn
"""

# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()


# ========== 练习 1 ==========
# 添加 GET /hello 路由，返回 {"message": "Hello"}。启动服务后访问 http://127.0.0.1:8000/hello 验证
# 期望输出: 浏览器或 curl 得到 {"message":"Hello"}
def exercise_1_instruction():
    print("在 exercises.py 中取消注释并实现：app = FastAPI()；@app.get('/hello') 返回 {'message': 'Hello'}")


# ========== 练习 2 ==========
# 添加 GET /items/{item_id}，路径参数 item_id: int，返回 {"item_id": item_id}
# 期望输出: 访问 /items/42 得到 {"item_id":42}
def exercise_2_instruction():
    print("添加 @app.get('/items/{item_id}')，返回 {\"item_id\": item_id}")


# ========== 练习 3 ==========
# 定义 Pydantic 模型 GreetBody(name: str)，添加 POST /greet，请求体为 GreetBody，返回 {"greeting": "Hello, " + name}
# 期望输出: POST {"name":"Alice"} 得到 {"greeting":"Hello, Alice"}
def exercise_3_instruction():
    print("定义 GreetBody；@app.post('/greet') 接收 body: GreetBody，返回 greeting")


if __name__ == "__main__":
    print("本 lab 练习题需在 exercises.py 中实现 FastAPI 路由，然后运行: uvicorn exercises:app --reload\n")
    exercise_1_instruction()
    print()
    exercise_2_instruction()
    print()
    exercise_3_instruction()
