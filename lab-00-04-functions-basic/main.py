"""
lab-00-04-functions-basic: 函数基础
"""

# ========== 定义无参数函数 ==========
def greet():
    """打印问候语"""
    print("Hello, World!")


# 调用函数
greet()

# ========== 定义有参数的函数 ==========
def greet_person(name):
    """向指定的人打招呼"""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")

# ========== 函数返回值 ==========
def add(a, b):
    """计算两个数的和"""
    return a + b


result = add(3, 5)
print(f"3 + 5 = {result}")

# ========== 默认参数 ==========
def greet_with_title(name, title="先生"):
    """打招呼，可以指定称呼"""
    print(f"你好，{title}{name}！")


greet_with_title("张三")  # 使用默认值：先生
greet_with_title("李四", "女士")  # 指定值：女士

# ========== 多个返回值 ==========
def get_name_and_age():
    """返回多个值（实际返回一个元组）"""
    return "Alice", 25


name, age = get_name_and_age()
print(f"姓名：{name}，年龄：{age}")

# ========== 无返回值 ==========
def print_info(name, age):
    """只打印，不返回值"""
    print(f"姓名：{name}，年龄：{age}")


result = print_info("Bob", 30)
print(f"函数返回值：{result}")  # None

# ========== 函数内部可以调用其他函数 ==========
def calculate_area(radius):
    """计算圆的面积"""
    pi = 3.14159
    return pi * radius ** 2


def print_circle_info(radius):
    """打印圆的信息"""
    area = calculate_area(radius)
    print(f"半径：{radius}，面积：{area:.2f}")


print_circle_info(5)
