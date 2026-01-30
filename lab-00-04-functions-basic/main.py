"""
lab-00-04-functions-basic: 函数基础

运行时会展示：定义、调用、参数、默认参数、返回值、多返回值、无返回值（None）及函数间调用。
"""

print("=== 1. 无参数函数 ===\n")
print("  >>> [说明] def 函数名(): 下一行缩进即函数体")


def greet():
    """打印问候语（文档字符串，可用 函数名.__doc__ 查看）"""
    print("  Hello, World!")


print("  调用: greet()")
greet()
print()

print("=== 2. 有参数函数 ===\n")
print("  >>> [说明] def 函数名(参数1, 参数2): 调用时按位置传入")


def greet_person(name):
    """向指定的人打招呼"""
    print(f"  Hello, {name}!")


print("  调用: greet_person('Alice')")
greet_person("Alice")
print("  调用: greet_person('Bob')")
greet_person("Bob")
print()

print("=== 3. 返回值 return ===\n")
print("  >>> [说明] return 值 会结束函数并把值交给调用方")


def add(a, b):
    """计算两数之和"""
    return a + b


print("  调用: result = add(3, 5)")
result = add(3, 5)
print(f"  返回值: {result}\n")

print("=== 4. 默认参数 ===\n")
print("  >>> [说明] 形参 = 默认值，调用时可省略，省略则用默认值")


def greet_with_title(name, title="先生"):
    """打招呼，可指定称呼"""
    print(f"  你好，{title}{name}！")


print("  调用: greet_with_title('张三')  -> 使用默认 title='先生'")
greet_with_title("张三")
print("  调用: greet_with_title('李四', '女士')  -> 传入 title")
greet_with_title("李四", "女士")
print()

print("=== 5. 多返回值（实际返回一个元组，自动解包）===\n")


def get_name_and_age():
    """返回多个值"""
    return "Alice", 25


print("  调用: name, age = get_name_and_age()")
name, age = get_name_and_age()
print(f"  解包后: name={name}, age={age}\n")

print("=== 6. 无 return 时返回 None ===\n")


def print_info(name, age):
    """只打印，不写 return"""
    print(f"  姓名：{name}，年龄：{age}")


print("  调用: result = print_info('Bob', 30)")
result = print_info("Bob", 30)
print(f"  >>> [触发] 函数无 return，result = {result}\n")

print("=== 7. 函数内调用其他函数 ===\n")
print("  >>> [说明] print_circle_info 内部会调用 calculate_area")


def calculate_area(radius):
    """计算圆的面积"""
    pi = 3.14159
    return pi * radius ** 2


def print_circle_info(radius):
    """打印圆的信息"""
    area = calculate_area(radius)
    print(f"  半径：{radius}，面积：{area:.2f}")


print("  调用: print_circle_info(5)")
print_circle_info(5)
