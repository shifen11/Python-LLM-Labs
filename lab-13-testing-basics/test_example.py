#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-13-testing-basics - pytest 示例测试文件

这是一个示例测试文件，展示 pytest 的基本用法。
"""

import pytest


# ========== 被测试的函数 ==========

def add(a: int, b: int) -> int:
    """两数相加"""
    return a + b


def multiply(a: int, b: int) -> int:
    """两数相乘"""
    return a * b


def is_positive(num: int) -> bool:
    """判断是否为正数"""
    return num > 0


def divide(a: float, b: float) -> float:
    """除法"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def get_grade(score: int) -> str:
    """根据分数获取等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


# ========== 1. 基本断言测试 ==========

def test_add():
    """测试加法函数"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_multiply():
    """测试乘法函数"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_is_positive():
    """测试正数判断函数"""
    assert is_positive(5) == True
    assert is_positive(1) == True
    assert is_positive(0) == False
    assert is_positive(-1) == False


# ========== 2. 测试异常 ==========

def test_divide_normal():
    """测试正常除法"""
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    """测试除数为 0 时是否抛出异常"""
    with pytest.raises(ValueError):
        divide(1, 0)


def test_divide_by_zero_message():
    """测试除数为 0 时的异常消息"""
    with pytest.raises(ValueError, match="除数不能为 0"):
        divide(1, 0)


# ========== 3. 参数化测试 ==========

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    """参数化测试加法"""
    assert add(a, b) == expected


@pytest.mark.parametrize("input,expected", [
    (5, True),
    (1, True),
    (0, False),
    (-1, False),
    (-5, False),
])
def test_is_positive_parametrized(input, expected):
    """参数化测试正数判断"""
    assert is_positive(input) == expected


@pytest.mark.parametrize("score,expected", [
    (95, "A"),
    (90, "A"),
    (85, "B"),
    (80, "B"),
    (75, "C"),
    (60, "C"),
    (59, "F"),
    (0, "F"),
])
def test_get_grade(score, expected):
    """参数化测试分数等级"""
    assert get_grade(score) == expected


# ========== 4. 使用 ==========

@pytest.fixture
def sample_data():
    """返回示例数据"""
    return {"name": "张三", "age": 20, "city": "北京"}


@pytest.fixture
def sample_numbers():
    """返回示例数字列表"""
    return [1, 2, 3, 4, 5]


def test_use_fixture(sample_data):
    """测试使用 fixture"""
    assert sample_data["name"] == "张三"
    assert sample_data["age"] == 20
    assert sample_data["city"] == "北京"


def test_sample_numbers(sample_numbers):
    """测试数字列表 fixture"""
    assert len(sample_numbers) == 5
    assert sum(sample_numbers) == 15
    assert sample_numbers[0] == 1
    assert sample_numbers[-1] == 5


# ========== 5. 集合测试 ==========

@pytest.fixture
def empty_list():
    """返回空列表"""
    return []


@pytest.fixture
def sample_list():
    """返回示例列表"""
    return ["apple", "banana", "cherry"]


def test_empty_list_length(empty_list):
    """测试空列表长度"""
    assert len(empty_list) == 0


def test_empty_list_membership(empty_list):
    """测试空列表包含"""
    assert "apple" not in empty_list


def test_sample_list_length(sample_list):
    """测试示例列表长度"""
    assert len(sample_list) == 3


def test_sample_list_membership(sample_list):
    """测试示例列表包含"""
    assert "apple" in sample_list
    assert "banana" in sample_list
    assert "cherry" in sample_list
    assert "orange" not in sample_list


# ========== 6. 边界条件测试 ==========

@pytest.mark.parametrize("n,factorial", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_factorial(n, factorial):
    """测试阶乘函数（使用参数化）"""
    # 计算阶乘
    result = 1
    for i in range(1, n + 1):
        result *= i
    assert result == factorial


def test_factorial_negative():
    """测试负数阶乘应该返回 1 或抛出异常"""
    # 这个测试展示了如何处理特殊情况
    # 阶乘对于负数通常没有定义
    n = -1
    result = 1
    for i in range(1, n + 1):  # range(1, 0) 是空的，不会循环
        result *= i
    assert result == 1  # 当前实现返回 1


# ========== 7. 测试类 ==========

class TestCalculator:
    """计算器测试类"""

    def test_add_positive_numbers(self):
        """测试正数加法"""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """测试负数加法"""
        assert add(-2, -3) == -5

    def test_mixed_numbers(self):
        """测试混合符号加法"""
        assert add(-2, 3) == 1
        assert add(2, -3) == -1
