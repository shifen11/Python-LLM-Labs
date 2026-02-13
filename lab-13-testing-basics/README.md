# lab-13-testing-basics - 测试基础

## 简介

本实验室介绍 Python 的单元测试基础，重点讲解 pytest 测试框架。pytest 是 Python 生态中最流行的测试框架之一，语法简洁，功能强大。

## 学习目标

- 理解单元测试的基本概念
- 掌握 pytest 的基本使用方法
- 理解断言（assert）的使用
- 掌握 fixture 的使用
- 理解参数化测试

## 运行方法

### 交互式演示

```bash
python main.py
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行指定文件
pytest test_example.py

# 显示详细输出
pytest -v

# 显示打印输出
pytest -s

# 运行特定测试
pytest test_example.py::test_add
```

## 核心概念

### 断言（assert）

```python
def test_add():
    result = add(1, 2)
    assert result == 3  # 如果条件不成立，测试失败
```

### Fixture

Fixture 是 pytest 提供的一种共享测试资源的方式：

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "张三", "age": 20}

def test_use_fixture(sample_data):
    assert sample_data["age"] == 20
```

### 参数化测试

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## 安装 pytest

```bash
pip install pytest
```

## 内容概览

### main.py 演示内容

1. **pytest 简介**
   - 测试文件的命名规则
   - 测试函数的命名规则
   - 基本的测试写法

2. **断言方法**
   - assert 语句的使用
   - 常见的断言模式

3. **fixture**
   - fixture 的定义和使用
   - fixture 的作用域
   - fixture 的参数化

4. **参数化测试**
   - 使用 @pytest.mark.parametrize
   - 减少重复代码

### exercises.py 练习题

1. 编写简单的单元测试
2. 使用 fixture
3. 参数化测试

## 测试最佳实践

1. **测试命名**：使用 `test_` 前缀，描述性命名
2. **独立性**：每个测试应该独立运行
3. **可读性**：测试代码应该清晰易懂
4. **边界情况**：测试边界条件和异常情况
