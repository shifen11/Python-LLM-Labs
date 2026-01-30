"""
lab-09-pydantic-validation: Pydantic 类型校验与模型定义

运行时会展示：BaseModel 定义、Field 约束、默认值、model_dump()，以及校验失败时抛出的异常。
"""
from pydantic import BaseModel, Field

print("=== 1. 定义模型（类似 Java Bean / 数据类）===\n")
print("  >>> [说明] 继承 BaseModel，用类型注解声明字段；Field(ge=..., le=...) 为范围约束")


class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)  # 年龄 0～150
    email: str | None = None  # 可选，默认 None


print("  class User: name(str), age(0~150), email(可选)\n")

print("=== 2. 创建实例与 model_dump() ===\n")
print("  >>> [触发] User(name='Alice', age=25) 会校验类型与约束")
u = User(name="Alice", age=25)
print(f"  u = {u}")
print(f"  u.model_dump() -> {u.model_dump()}")

u2 = User(name="Bob", age=30, email="bob@example.com")
print(f"  u2.model_dump() -> {u2.model_dump()}\n")

print("=== 3. 默认值与 Field 默认值 ===\n")


class Config(BaseModel):
    host: str = "localhost"
    port: int = Field(default=8080, ge=1, le=65535)


print("  >>> [说明] 未传的字段使用默认值；Field(default=..., ge=..., le=...) 同时约束范围")
c = Config()
print(f"  Config() 默认 -> {c.model_dump()}")
c2 = Config(host="0.0.0.0", port=9000)
print(f"  Config(host='0.0.0.0', port=9000) -> {c2.model_dump()}\n")

print("=== 4. 校验失败（抛出 ValidationError）===\n")
print("  >>> [触发] User(name='X', age=200) 违反 le=150，会抛异常")
try:
    User(name="X", age=200)
except Exception as e:
    print(f"  捕获到: {type(e).__name__}")
    print(f"  信息（部分）: {str(e)[:200]}...")
