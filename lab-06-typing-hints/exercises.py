#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-06-typing-hints - 练习题

请完成以下练习题，完成后运行本文件验证你的答案。
"""

from typing import List, Dict, Set, Tuple, Optional, Union


# ========== 练习 1: 为函数添加基本类型注解 ==========

print("=" * 50)
print("练习 1: 基本类型注解")
print("=" * 50)

# TODO: 为以下函数添加类型注解：
# 1. multiply 函数：接收两个 int 参数，返回 int
# 2. get_first_char 函数：接收一个 str 参数，返回 str
# 3. is_positive 函数：接收一个 float 参数，返回 bool

# 在这里完成练习 1 的代码
def multiply(a: int, b: int) -> int:
    return a * b


def get_first_char(text: str) -> str:
    return text[0] if text else ""


def is_positive(number: float) -> bool:
    return number > 0


# 验证练习 1
print(f"multiply(3, 4) = {multiply(3, 4)}")
print(f"get_first_char('hello') = '{get_first_char('hello')}'")
print(f"is_positive(3.14) = {is_positive(3.14)}")

# 验证
assert multiply(3, 4) == 12
assert get_first_char("hello") == "h"
assert is_positive(3.14) == True
assert is_positive(-1.5) == False
print("✓ 练习 1 通过!\n")


# ========== 练习 2: 使用 Optional 和 Union ==========

print("=" * 50)
print("练习 2: Optional 和 Union")
print("=" * 50)

# TODO: 为以下函数添加类型注解：

# 1. get_element 函数：
#    - 参数：index: int, data: List[str]
#    - 返回：Optional[str]（如果索引越界返回 None）

# 2. parse_number 函数：
#    - 参数：text: str
#    - 返回：Union[int, float, str]（尝试解析为 int，失败解析为 float，都失败返回原字符串）

# 3. safe_divide 函数：
#    - 参数：a: float, b: float
#    - 返回：Optional[float]（除数为 0 返回 None）

# 在这里完成练习 2 的代码
def get_element(index: int, data: List[str]) -> Optional[str]:
    if 0 <= index < len(data):
        return data[index]
    return None


def parse_number(text: str) -> Union[int, float, str]:
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text


def safe_divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


# 验证练习 2
print(f"get_element(0, ['a', 'b', 'c']) = {get_element(0, ['a', 'b', 'c'])}")
print(f"get_element(5, ['a', 'b', 'c']) = {get_element(5, ['a', 'b', 'c'])}")
print(f"parse_number('123') = {parse_number('123')} (type: {type(parse_number('123')).__name__})")
print(f"parse_number('3.14') = {parse_number('3.14')} (type: {type(parse_number('3.14')).__name__})")
print(f"parse_number('hello') = {parse_number('hello')} (type: {type(parse_number('hello')).__name__})")
print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")

# 验证
assert get_element(0, ["a", "b", "c"]) == "a"
assert get_element(5, ["a", "b", "c"]) is None
assert parse_number("123") == 123
assert parse_number("3.14") == 3.14
assert parse_number("hello") == "hello"
assert safe_divide(10, 2) == 5.0
assert safe_divide(10, 0) is None
print("✓ 练习 2 通过!\n")


# ========== 练习 3: 定义类型别名和泛型 ==========

print("=" * 50)
print("练习 3: 类型别名和泛型")
print("=" * 50)

# TODO: 定义类型别名并完成函数：

# 1. 定义类型别名：
#    - Point: Tuple[float, float]  # 二维坐标点
#    - Student: Dict[str, Union[str, int]]  # 学生信息
#    - StudentList: List[Student]  # 学生列表

# 2. 实现 calculate_distance 函数：
#    - 参数：p1: Point, p2: Point
#    - 返回：float（两点之间的距离）
#    - 公式：sqrt((x2-x1)^2 + (y2-y1)^2)

# 3. 实现 get_adult_students 函数：
#    - 参数：students: StudentList
#    - 返回：StudentList（年龄 >= 18 的学生）

# 在这里完成练习 3 的代码
Point = Tuple[float, float]
Student = Dict[str, Union[str, int]]
StudentList = List[Student]

import math

def calculate_distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def get_adult_students(students: StudentList) -> StudentList:
    return [s for s in students if s.get("age", 0) >= 18]


# 验证练习 3
p1 = (0.0, 0.0)
p2 = (3.0, 4.0)
distance = calculate_distance(p1, p2)
print(f"distance between {p1} and {p2} = {distance}")

students = [
    {"name": "张三", "age": 20, "class": "1班"},
    {"name": "李四", "age": 17, "class": "1班"},
    {"name": "王五", "age": 19, "class": "2班"},
]
adults = get_adult_students(students)
print(f"adult students = {[s['name'] for s in adults]}")

# 验证
assert abs(distance - 5.0) < 0.01
assert len(adults) == 2
assert adults[0]["name"] == "张三"
assert adults[1]["name"] == "王五"
print("✓ 练习 3 通过!\n")


print("=" * 50)
print("所有练习完成！")
print("=" * 50)
