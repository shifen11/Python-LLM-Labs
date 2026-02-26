#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-13-testing-basics - 练习题

请完成以下练习题，运行 'pytest' 验证你的答案。
"""

import pytest


# ========== 被测试的函数 ==========

def calculate_average(numbers: list) -> float:
    """计算平均值"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def find_max(numbers: list) -> int:
    """找出最大值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return max(numbers)


def is_palindrome(text: str) -> bool:
    """判断是否为回文"""
    return text == text[::-1]


# ========== 练习 1: 编写简单的单元测试 ==========

# TODO: 为 calculate_average 函数编写测试
# 测试以下情况：
# 1. 正常情况：计算 [1, 2, 3, 4, 5] 的平均值
# 2. 空列表：返回 0.0
# 3. 单个元素：[10] 返回 10.0
# 4. 负数：[-5, -3, -1] 返回 -3.0

# 在这里完成练习 1 的代码
def test_calculate_average_normal():
    """测试正常情况"""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0


def test_calculate_average_empty():
    """测试空列表"""
    assert calculate_average([]) == 0.0


def test_calculate_average_single():
    """测试单个元素"""
    assert calculate_average([10]) == 10.0


def test_calculate_average_negative():
    """测试负数"""
    assert calculate_average([-5, -3, -1]) == -3.0


# ========== 练习 2: 测试异常 ==========

# TODO: 为 find_max 函数编写测试
# 测试以下情况：
# 1. 正常情况：找出 [1, 5, 3, 9, 2] 的最大值
# 2. 单个元素：[42] 返回 42
# 3. 空列表：抛出 ValueError 异常

# 在这里完成练习 2 的代码
def test_find_max_normal():
    """测试正常情况"""
    assert find_max([1, 5, 3, 9, 2]) == 9


def test_find_max_single():
    """测试单个元素"""
    assert find_max([42]) == 42


def test_find_max_empty():
    """测试空列表应该抛出异常"""
    with pytest.raises(ValueError):
        find_max([])


# ========== 练习 3: 参数化测试 ==========

# TODO: 使用参数化测试 is_palindrome 函数
# 测试以下案例：
# - ("level", True)
# - ("radar", True)
# - ("hello", False)
# - ("A", True)
# - ("", True)

# 在这里完成练习 3 的代码
@pytest.mark.parametrize("text,expected", [
    ("level", True),
    ("radar", True),
    ("hello", False),
    ("A", True),
    ("", True),
])
def test_is_palindrome(text, expected):
    """参数化测试回文判断"""
    assert is_palindrome(text) == expected


# ========== 练习 4: 使用 fixture ==========

# TODO: 定义一个 fixture 返回示例学生数据
# 学生数据格式：{"name": "张三", "age": 20, "score": 90}
# 然后编写测试验证这个 fixture

# 在这里完成练习 4 的代码
@pytest.fixture
def sample_student():
    """返回示例学生数据"""
    return {"name": "张三", "age": 20, "score": 90}


def test_sample_student_fixture(sample_student):
    """测试学生数据 fixture"""
    assert sample_student["name"] == "张三"
    assert sample_student["age"] == 20
    assert sample_student["score"] == 90
