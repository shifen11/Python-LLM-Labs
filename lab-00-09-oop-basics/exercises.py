#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-00-09-oop-basics - 练习题

请完成以下练习题，完成后运行本文件验证你的答案。
"""

# ========== 练习 1: 定义一个简单的 Person 类 ==========

print("=" * 50)
print("练习 1: 定义 Person 类")
print("=" * 50)

# TODO: 定义一个 Person 类，包含以下内容：
# - 构造方法 __init__，接收 name 和 age 两个参数
# - 一个 say_hello 方法，返回 "你好，我是 {name}" 的字符串
# - 一个 introduce 方法，返回 "我是 {name}，今年 {age} 岁了" 的字符串

# 在这里完成练习 1 的代码
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"你好，我是 {self.name}"

    def introduce(self):
        return f"我是 {self.name}，今年 {self.age} 岁了"


# 验证练习 1
person = Person("小明", 20)
print(f"测试 say_hello: {person.say_hello()}")
print(f"测试 introduce: {person.introduce()}")

# 预期输出:
# 测试 say_hello: 你好，我是 小明
# 测试 introduce: 我是 小明，今年 20 岁了

# 验证
assert person.say_hello() == "你好，我是 小明", "say_hello 方法返回值不正确"
assert person.introduce() == "我是 小明，今年 20 岁了", "introduce 方法返回值不正确"
print("✓ 练习 1 通过!\n")


# ========== 练习 2: 实现继承关系 ==========

print("=" * 50)
print("练习 2: 实现继承关系")
print("=" * 50)

# 定义父类 Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} 在移动"


# TODO: 定义一个 Dog 类，继承自 Animal，要求：
# - 构造方法接收 name 和 breed（品种）两个参数
# - 使用 super() 调用父类的构造方法
# - 重写 move 方法，返回 "{name}（{breed}）在奔跑"
# - 添加一个 bark 方法，返回 "汪汪！"

# 在这里完成练习 2 的代码
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def move(self):
        return f"{self.name}（{self.breed}）在奔跑"

    def bark(self):
        return "汪汪！"


# 验证练习 2
dog = Dog("旺财", "金毛")
print(f"测试 move: {dog.move()}")
print(f"测试 bark: {dog.bark()}")

# 预期输出:
# 测试 move: 旺财（金毛）在奔跑
# 测试 bark: 汪汪！

# 验证
assert dog.move() == "旺财（金毛）在奔跑", "move 方法返回值不正确"
assert dog.bark() == "汪汪！", "bark 方法返回值不正确"
print("✓ 练习 2 通过!\n")


# ========== 练习 3: 方法重写和多态 ==========

print("=" * 50)
print("练习 3: 方法重写和多态")
print("=" * 50)

# 定义形状基类
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        """计算面积"""
        return 0

    def perimeter(self):
        """计算周长"""
        return 0


# TODO: 定义两个子类 Rectangle（矩形）和 Circle（圆形）：

# Rectangle 类要求：
# - 构造方法接收 name, width（宽）, height（高）三个参数
# - area 方法返回 width * height
# - perimeter 方法返回 (width + height) * 2

# Circle 类要求：
# - 构造方法接收 name, radius（半径）两个参数
# - area 方法返回 3.14 * radius * radius
# - perimeter 方法返回 2 * 3.14 * radius

# 在这里完成练习 3 的代码
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# 验证练习 3 - 多态演示
shapes = [
    Rectangle("矩形", 5, 3),
    Circle("圆形", 4),
]

print("多态演示 - 不同形状的面积和周长：")
for shape in shapes:
    print(f"  {shape.name}: 面积 = {shape.area():.2f}, 周长 = {shape.perimeter():.2f}")

# 预期输出:
# 多态演示 - 不同形状的面积和周长：
#   矩形: 面积 = 15.00, 周长 = 16.00
#   圆形: 面积 = 50.24, 周长 = 25.12

# 验证
assert abs(Rectangle("矩形", 5, 3).area() - 15) < 0.01, "Rectangle 面积计算不正确"
assert abs(Rectangle("矩形", 5, 3).perimeter() - 16) < 0.01, "Rectangle 周长计算不正确"
assert abs(Circle("圆形", 4).area() - 50.24) < 0.01, "Circle 面积计算不正确"
assert abs(Circle("圆形", 4).perimeter() - 25.12) < 0.01, "Circle 周长计算不正确"
print("✓ 练习 3 通过!\n")


print("=" * 50)
print("所有练习完成！")
print("=" * 50)
