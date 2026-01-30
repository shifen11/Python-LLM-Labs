# lab-05-magic-methods

**魔术方法（协议）**

## 知识点

- `__init__`：构造（类似 Java 构造函数）
- `__str__` / `__repr__`：字符串表示（`__str__` 面向用户，`__repr__` 面向开发者）
- `__call__`：让实例像函数一样可被调用，即 `obj()`
- `__len__`、`__getitem__`：支持 `len(obj)`、`obj[i]`、切片
- `__iter__`：支持 `for x in obj`、`list(obj)` 等迭代
- Python 的「协议」：实现特定方法即支持相应语法，无需继承基类

## 运行

```bash
python main.py
```

运行时会打印各魔术方法被触发的时机，便于理解调用顺序。

## 练习题

练习题见 [exercises.py](./exercises.py)，在 lab 目录下运行 `python exercises.py` 完成并自测。
