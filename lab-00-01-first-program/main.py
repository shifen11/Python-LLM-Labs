"""
lab-00-01-first-program: 第一个 Python 程序
这是多行注释，用三个双引号或单引号包裹
"""

# 这是单行注释，用 # 开头

# 第一个 Python 程序
print("Hello, World!")
print("欢迎来到 Python 学习之旅！")

# print 可以输出多个值，用逗号分隔
print("我的名字是", "Python", "，版本是", 3.11)

# 使用 f-string 格式化输出（Python 3.6+）
name = "Python"
version = 3.11
print(f"语言：{name}，版本：{version}")

# Python 使用缩进表示代码块（通常 4 个空格）
if True:
    print("这是 if 语句块内的代码")
    print("注意缩进！")

print("这是 if 语句块外的代码")
