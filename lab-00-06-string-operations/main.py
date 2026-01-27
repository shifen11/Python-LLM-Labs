"""
lab-00-06-string-operations: 字符串操作
"""

# ========== 字符串格式化 ==========
print("=== 字符串格式化 ===")
name = "Alice"
age = 25

# 方法1：f-string（推荐，Python 3.6+）
message1 = f"我的名字是 {name}，今年 {age} 岁"
print(message1)

# 方法2：format()
message2 = "我的名字是 {}，今年 {} 岁".format(name, age)
print(message2)

# 方法3：% 格式化（旧式）
message3 = "我的名字是 %s，今年 %d 岁" % (name, age)
print(message3)

# ========== 字符串方法 ==========
print("\n=== 大小写转换 ===")
text = "Hello World"
print(f"原字符串：{text}")
print(f"转大写：{text.upper()}")
print(f"转小写：{text.lower()}")
print(f"首字母大写：{text.capitalize()}")

print("\n=== 去除空白 ===")
text_with_spaces = "  Python  "
print(f"原字符串：'{text_with_spaces}'")
print(f"去除首尾空白：'{text_with_spaces.strip()}'")
print(f"去除左侧空白：'{text_with_spaces.lstrip()}'")
print(f"去除右侧空白：'{text_with_spaces.rstrip()}'")

print("\n=== 分割字符串 ===")
sentence = "苹果,香蕉,橙子"
fruits = sentence.split(",")
print(f"原字符串：{sentence}")
print(f"分割后：{fruits}")

print("\n=== 连接字符串 ===")
fruits_list = ["苹果", "香蕉", "橙子"]
joined = ",".join(fruits_list)
print(f"列表：{fruits_list}")
print(f"连接后：{joined}")

print("\n=== 替换 ===")
text = "我喜欢Java"
new_text = text.replace("Java", "Python")
print(f"原字符串：{text}")
print(f"替换后：{new_text}")

print("\n=== 查找 ===")
text = "Python is great"
print(f"原字符串：{text}")
print(f"'is' 的位置：{text.find('is')}")
print(f"'Java' 的位置：{text.find('Java')}")  # 找不到返回 -1

if "Python" in text:
    print("找到了 'Python'")

print("\n=== 字符串拼接 ===")
# 方法1：使用 +
greeting = "Hello" + " " + "World"
print(f"拼接结果：{greeting}")

# 方法2：使用 join（更高效）
words = ["Hello", "World"]
greeting2 = " ".join(words)
print(f"join 结果：{greeting2}")

# ========== 字符串是不可变的 ==========
print("\n=== 字符串不可变 ===")
text = "Hello"
# text[0] = "h"  # 这行会报错！字符串不能修改

# 要修改，需要创建新字符串
new_text = "h" + text[1:]
print(f"原字符串：{text}")
print(f"新字符串：{new_text}")
