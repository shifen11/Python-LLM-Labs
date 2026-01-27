"""
lab-00-02-variables-types: 变量与基本数据类型
"""

# ========== 整数 int ==========
age = 25
count = -10
print(f"age = {age}, type = {type(age).__name__}")  # int

# ========== 浮点数 float ==========
price = 99.99
pi = 3.14159
print(f"price = {price}, type = {type(price).__name__}")  # float

# ========== 字符串 str ==========
name = "Alice"
greeting = 'Hello'
# 可以用单引号或双引号，但要配对
message = "她说：'你好'"
print(f"name = {name}, type = {type(name).__name__}")  # str

# ========== 布尔值 bool ==========
is_student = True
is_working = False
print(f"is_student = {is_student}, type = {type(is_student).__name__}")  # bool

# ========== 类型转换 ==========
# 字符串转整数
num_str = "123"
num_int = int(num_str)
print(f"'{num_str}' -> {num_int}")

# 整数转字符串
age_str = str(age)
print(f"{age} -> '{age_str}'")

# 字符串转浮点数
price_str = "99.99"
price_float = float(price_str)
print(f"'{price_str}' -> {price_float}")

# 其他类型转布尔值
print(f"bool(0) = {bool(0)}")      # False
print(f"bool(1) = {bool(1)}")      # True
print(f"bool('') = {bool('')}")    # False（空字符串）
print(f"bool('hello') = {bool('hello')}")  # True

# ========== 变量可以重新赋值（改变类型）==========
x = 42
print(f"x = {x}, type = {type(x).__name__}")
x = "现在是字符串"
print(f"x = {x}, type = {type(x).__name__}")
