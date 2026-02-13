"""
lab-00-02-variables-types: 变量与基本数据类型

运行时会展示：四种基本类型、type() 与类型转换，以及「同一变量可先后指向不同类型」。
"""

print("=== 1. 整数 int ===\n")
print("  >>> [说明] 整数无大小限制（仅受内存限制），与 Java 的 int/long 不同")
age = 25
count = -10
var = {type(age).__name__}
print(f"  age = {age}, type(age) = {type(age).__name__}")
print(f"  count = {count}\n")

print("=== 2. 浮点数 float ===\n")
print("  >>> [说明] 带小数点的数，双精度")
price = 99.99
pi = 3.14159
print(f"  price = {price}, type(price) = {type(price).__name__}\n")

print("=== 3. 字符串 str ===\n")
print("  >>> [说明] 单引号、双引号等价；嵌套时交替使用")
name = "Alice"
greeting = "Hello"
message = "她说：'你好'"
print(f"  name = {name}, type(name) = {type(name).__name__}")
print(f"  message = {message}\n")

print("=== 4. 布尔值 bool ===\n")
print("  >>> [说明] True / False 首字母大写（与 Java 的 true/false 不同）")
is_student = True
is_working = False
print(f"  is_student = {is_student}, type = {type(is_student).__name__}\n")

print("=== 5. 类型转换 ===\n")
print("  >>> [说明] int() / float() / str() / bool() 用于显式转换")
num_str = "123"
num_int = int(num_str)
print(f"  int('123') -> {num_int}")
age_str = str(age)
print(f"  str(25) -> '{age_str}'")
price_str = "99.99"
price_float = float(price_str)
print(f"  float('99.99') -> {price_float}")
print("  >>> [小结] 布尔转换：0、空字符串 '' 为 False，其余为 True")
print(f"  bool(0) = {bool(0)}, bool(1) = {bool(1)}, bool('') = {bool('')}, bool('hello') = {bool('hello')}\n")

print("=== 6. 变量可重新赋值（甚至改类型）===\n")
print("  >>> [说明] 变量是「名字绑定到对象」，重新赋值即绑定到新对象")
x = 42
print(f"  x = 42  -> x = {x}, type = {type(x).__name__}")
x = "现在是字符串"
print(f"  x = '...'  -> x = {x}, type = {type(x).__name__}")
