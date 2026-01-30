"""
lab-00-06-string-operations: 字符串操作

运行时会展示：三种格式化方式、常用方法（大小写、strip、split、join、replace、find）及「字符串不可变」。
"""

print("=== 1. 字符串格式化 ===\n")
print("  >>> [说明] 推荐 f-string；format() 和 % 为旧式，了解即可")
name, age = "Alice", 25
message1 = f"我的名字是 {name}，今年 {age} 岁"
print(f"  f-string: {message1}")
message2 = "我的名字是 {}，今年 {} 岁".format(name, age)
print(f"  format(): {message2}")
message3 = "我的名字是 %s，今年 %d 岁" % (name, age)
print(f"  %% 格式化: {message3}\n")

print("=== 2. 大小写转换 ===\n")
text = "Hello World"
print(f"  原字符串: {text}")
print(f"  .upper() -> {text.upper()}")
print(f"  .lower() -> {text.lower()}")
print(f"  .capitalize() -> {text.capitalize()}\n")

print("=== 3. 去除空白 ===\n")
text_with_spaces = "  Python  "
print(f"  原字符串: '{text_with_spaces}'")
print(f"  .strip()  -> '{text_with_spaces.strip()}'")
print(f"  .lstrip() -> '{text_with_spaces.lstrip()}'")
print(f"  .rstrip() -> '{text_with_spaces.rstrip()}'\n")

print("=== 4. 分割与连接 ===\n")
print("  >>> [说明] split(分隔符) 得到列表；分隔符.join(列表) 连接成字符串")
sentence = "苹果,香蕉,橙子"
fruits = sentence.split(",")
print(f"  '苹果,香蕉,橙子'.split(',') -> {fruits}")
fruits_list = ["苹果", "香蕉", "橙子"]
joined = ",".join(fruits_list)
print(f"  ','.join(...) -> {joined}\n")

print("=== 5. 替换与查找 ===\n")
text = "我喜欢Java"
new_text = text.replace("Java", "Python")
print(f"  .replace('Java', 'Python') -> {new_text}")
text = "Python is great"
print(f"  .find('is') -> {text.find('is')}（找不到返回 -1）")
print(f"  'Python' in text -> {'Python' in text}\n")

print("=== 6. 字符串拼接 ===\n")
print("  >>> [说明] 用 + 拼接少量字符串；大量片段用 join 更高效")
greeting = "Hello" + " " + "World"
print(f"  '+' 拼接: {greeting}")
greeting2 = " ".join(["Hello", "World"])
print(f"  join: {greeting2}\n")

print("=== 7. 字符串不可变 ===\n")
print("  >>> [说明] 不能写 s[0]='x'，要「修改」只能生成新字符串")
text = "Hello"
# text[0] = "h"  # 会报错
new_text = "h" + text[1:]
print(f"  原字符串: {text}")
print(f"  新字符串（首字母改小写）: {new_text}")
