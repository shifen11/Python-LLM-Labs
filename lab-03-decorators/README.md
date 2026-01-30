# lab-03-decorators

**装饰器（Python 版 AOP）**

## 知识点

- 装饰器 = 接收函数、返回新函数的可调用对象
- `@deco` 等价于 `f = deco(f)`
- 带参数的装饰器、`functools.wraps` 保留元信息
- 常用场景：日志、计时、鉴权、重试

## 运行

```bash
python main.py
```

## 练习题

练习题见 [exercises.py](./exercises.py)，在 lab 目录下运行 `python exercises.py` 完成并自测。
