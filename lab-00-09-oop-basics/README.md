# lab-00-09-oop-basics - 面向对象基础

## 简介

本实验室介绍 Python 的面向对象编程（OOP）基础概念，包括类、对象、继承和多态。

## 学习目标

- 理解类和对象的概念
- 掌握类的定义和 `__init__` 构造方法
- 理解属性和方法的区别
- 掌握单继承的基本用法
- 理解方法重写和多态的基础概念

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

### 类（Class）

类是对象的模板，定义了对象的属性和行为。

```python
class Dog:
    def __init__(self, name):
        self.name = name  # 属性

    def bark(self):  # 方法
        return f"{self.name} 汪汪叫！"
```

### 对象（Object）

对象是类的实例。

```python
dog = Dog("旺财")  # 创建对象
print(dog.bark())  # 调用方法
```

### 继承（Inheritance）

子类可以继承父类的属性和方法。

```python
class Animal:
    def speak(self):
        return "动物在叫"

class Cat(Animal):  # 继承自 Animal
    def speak(self):  # 方法重写
        return "猫喵喵叫"
```

## 内容概览

### main.py 演示内容

1. **类的定义和对象的创建**
   - `class` 关键字
   - `__init__` 构造方法
   - `self` 参数的含义

2. **属性和方法**
   - 实例属性 vs 类属性
   - 实例方法 vs 类方法 vs 静态方法

3. **继承**
   - 单继承语法
   - `super()` 调用父类方法
   - 方法重写

4. **多态基础**
   - 同一方法在不同类中的不同实现

### exercises.py 练习题

1. 定义一个简单的 `Person` 类
2. 实现继承关系（`Student` 继承自 `Person`）
3. 实现方法重写
