#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-00-09-oop-basics - 面向对象基础

本脚本演示 Python 面向对象编程的核心概念。
"""

# >>> [说明] 类是对象的模板，定义了对象的属性和行为


# ========== 1. 类的定义和对象的创建 ==========

print("=" * 50)
print("1. 类的定义和对象的创建")
print("=" * 50)

# >>> [说明] 使用 class 关键字定义类，类名遵循大驼峰命名法
class Dog:
    """这是一个简单的 Dog 类"""

    # >>> [说明] __init__ 是构造方法，创建对象时自动调用
    def __init__(self, name, age):
        # >>> [说明] self 代表对象本身，通过 self. 来定义实例属性
        self.name = name  # 实例属性：名字
        self.age = age    # 实例属性：年龄

    def bark(self):
        """实例方法：狗叫"""
        return f"{self.name} 汪汪叫！"

    def introduce(self):
        """实例方法：自我介绍"""
        return f"我是 {self.name}，今年 {self.age} 岁了。"


# >>> [说明] 创建对象（类的实例化）
# >>> [触发] 输出对象信息
dog1 = Dog("旺财", 3)
print(f"创建了一只狗: {dog1.name}")
# >>> [预期输出] 创建了一只狗: 旺财

# >>> [触发] 调用对象的方法
print(dog1.bark())
# >>> [预期输出] 旺财 汪汪叫！

print(dog1.introduce())
# >>> [预期输出] 我是 旺财，今年 3 岁了。

# 创建另一个对象
dog2 = Dog("小白", 2)
print(f"\n另一只狗: {dog2.name}, {dog2.age}岁")
# >>> [预期输出] 另一只狗: 小白, 2岁


# ========== 2. 属性（实例属性 vs 类属性）==========

print("\n" + "=" * 50)
print("2. 属性（实例属性 vs 类属性）")
print("=" * 50)

class Cat:
    # >>> [说明] 类属性：所有实例共享的属性
    species = "猫科动物"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性：每个对象独有

    def show_info(self):
        return f"{self.name} 是 {Cat.species}"


cat1 = Cat("喵喵")
cat2 = Cat("咪咪")

# >>> [触发] 类属性对所有实例都是一样的
print(cat1.show_info())
# >>> [预期输出] 喵喵 是 猫科动物

print(cat2.show_info())
# >>> [预期输出] 咪咪 是 猫科动物

# >>> [说明] 修改类属性会影响所有实例
Cat.species = "家猫"
print(f"\n修改类属性后: {cat1.show_info()}")
# >>> [预期输出] 修改类属性后: 喵喵 是 家猫


# ========== 3. 方法（实例方法 vs 类方法 vs 静态方法）==========

print("\n" + "=" * 50)
print("3. 方法（实例方法 vs 类方法 vs 静态方法）")
print("=" * 50)

class MathUtils:
    """数学工具类"""

    # >>> [说明] 实例方法：第一个参数是 self
    def __init__(self, value):
        self.value = value

    def square(self):
        """实例方法：计算平方"""
        return self.value ** 2

    # >>> [说明] 类方法：使用 @classmethod 装饰器，第一个参数是 cls（类本身）
    @classmethod
    def add(cls, a, b):
        """类方法：加法"""
        return a + b

    # >>> [说明] 静态方法：使用 @staticmethod 装饰器，不需要 self 或 cls
    @staticmethod
    def multiply(a, b):
        """静态方法：乘法"""
        return a * b


# 实例方法需要先创建对象
m = MathUtils(5)
print(f"实例方法 square(5) = {m.square()}")
# >>> [预期输出] 实例方法 square(5) = 25

# 类方法直接通过类调用
print(f"类方法 add(3, 4) = {MathUtils.add(3, 4)}")
# >>> [预期输出] 类方法 add(3, 4) = 7

# 静态方法直接通过类调用
print(f"静态方法 multiply(3, 4) = {MathUtils.multiply(3, 4)}")
# >>> [预期输出] 静态方法 multiply(3, 4) = 12


# ========== 4. 继承 ==========

print("\n" + "=" * 50)
print("4. 继承")
print("=" * 50)

# >>> [说明] 定义父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """父类方法"""
        return f"{self.name} 发出声音"

    def eat(self):
        """父类方法"""
        return f"{self.name} 在吃东西"

# >>> [说明] 定义子类，继承自 Animal
class Dog2(Animal):
    def __init__(self, name, breed):
        # >>> [说明] 使用 super() 调用父类的 __init__ 方法
        super().__init__(name)
        self.breed = breed  # 子类特有的属性

    # >>> [说明] 方法重写（Override）：子类重新定义父类的方法
    def speak(self):
        return f"{self.name}（{self.breed}）汪汪叫！"

# >>> [说明] 另一个子类
class Cat2(Animal):
    def speak(self):
        return f"{self.name} 喵喵叫！"

# 创建子类对象
dog = Dog2("大黄", "金毛")
cat = Cat2("小花")

# >>> [触发] 子类继承父类的 eat 方法
print(dog.eat())
# >>> [预期输出] 大黄 在吃东西

# >>> [触发] 子类重写的 speak 方法
print(dog.speak())
# >>> [预期输出] 大黄（金毛）汪汪叫！

print(cat.speak())
# >>> [预期输出] 小花 喵喵叫！


# ========== 5. 多态 ==========

print("\n" + "=" * 50)
print("5. 多态")
print("=" * 50)

# >>> [说明] 多态：同一方法在不同对象上有不同的行为
# 即使是不同的子类，只要有相同的方法名，就可以统一调用

animals = [
    Animal("动物"),
    Dog2("旺财", "泰迪"),
    Cat2("小白"),
]

print("多态演示 - 不同动物的声音：")
for animal in animals:
    print(f"  {animal.speak()}")
# >>> [预期输出]
# 多态演示 - 不同动物的声音：
#   动物 发出声音
#   旺财（泰迪）汪汪叫！
#   小白 喵喵叫！


# ========== 6. 属性访问控制（封装）==========

print("\n" + "=" * 50)
print("6. 属性访问控制（封装）")
print("=" * 50)

class BankAccount:
    """银行账户类，演示封装"""

    def __init__(self, owner, balance):
        self.owner = owner  # 公有属性
        self.__balance = balance  # 私有属性（以双下划线开头）

    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"存款 {amount} 元成功")
        else:
            print("存款金额必须大于 0")

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取款 {amount} 元成功")
        else:
            print("取款失败：余额不足或金额无效")

    def get_balance(self):
        """获取余额（只读访问）"""
        return self.__balance


account = BankAccount("张三", 1000)
print(f"账户: {account.owner}")
# >>> [预期输出] 账户: 张三

# >>> [说明] 不能直接访问私有属性
# print(account.__balance)  # 这会报错

account.deposit(500)
# >>> [预期输出] 存款 500 元成功

account.withdraw(200)
# >>> [预期输出] 取款 200 元成功

print(f"当前余额: {account.get_balance()} 元")
# >>> [预期输出] 当前余额: 1300 元


print("\n" + "=" * 50)
print("实验室演示完成！")
print("=" * 50)
