# lab-06-typing-hints - 类型注解

## 简介

本实验室介绍 Python 的类型注解（Type Hints）功能。类型注解是 Python 3.5+ 引入的特性，可以帮助开发者更清晰地理解代码意图，提高代码的可维护性。

## 学习目标

- 理解类型注解的作用和意义
- 掌握基本类型的注解方式
- 理解 Optional 和 Union 类型的使用
- 掌握 List、Dict 等泛型类型的使用
- 了解类型别名和自定义类型

## 运行方法

### 交互式演示

```bash
python main.py
```

### 练习题

```bash
python exercises.py
```

## 核心概念

### 基本类型注解

```python
def add(a: int, b: int) -> int:
    return a + b
```

### Optional 类型

表示值可以是 None：

```python
from typing import Optional

def get_name(user_id: int) -> Optional[str]:
    # 可能返回 str 或 None
    pass
```

### Union 类型

表示值可以是多种类型之一：

```python
from typing import Union

def process(value: Union[int, str]) -> str:
    return str(value)
```

### 泛型类型

使用 List、Dict 等泛型：

```python
from typing import List, Dict

def get_scores() -> List[int]:
    return [85, 90, 78]

def get_info() -> Dict[str, int]:
    return {"age": 20, "score": 90}
```

### Python 3.10+ 新语法

Python 3.10+ 支持更简洁的类型注解语法：

```python
# Python 3.10+
def get_scores() -> list[int]:
    return [85, 90, 78]

def get_info() -> dict[str, int]:
    return {"age": 20, "score": 90}
```

## 内容概览

### main.py 演示内容

1. **基本类型注解**
   - int, str, float, bool
   - 函数参数和返回值注解
   - 变量注解

2. **Optional 和 Union**
   - Optional 的使用
   - Union 的使用
   - 处理多种可能的类型

3. **泛型类型**
   - List, Dict, Set, Tuple
   - 嵌套类型

4. **类型别名**
   - 使用 `TypeAlias` 定义类型别名

### exercises.py 练习题

1. 为函数添加基本类型注解
2. 使用 Optional 和 Union
3. 定义类型别名和泛型

## 类型检查工具

类型注解本身不会影响程序运行，但可以配合类型检查工具使用：

```bash
# 安装 mypy 类型检查工具
pip install mypy

# 运行类型检查
mypy main.py
```

类型检查不是必须的，但对于大型项目非常有帮助。
