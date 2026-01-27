"""
lab-09-pydantic-validation: 类型校验与模型定义
"""
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)
    email: str | None = None


class Config(BaseModel):
    host: str = "localhost"
    port: int = Field(default=8080, ge=1, le=65535)


if __name__ == "__main__":
    u = User(name="Alice", age=25)
    print("User:", u.model_dump())
    u2 = User(name="Bob", age=30, email="bob@example.com")
    print("User with email:", u2.model_dump())

    c = Config()
    print("Config default:", c.model_dump())
    c2 = Config(host="0.0.0.0", port=9000)
    print("Config custom:", c2.model_dump())

    # 校验失败示例
    try:
        User(name="X", age=200)
    except Exception as e:
        print("Validation error:", e)
