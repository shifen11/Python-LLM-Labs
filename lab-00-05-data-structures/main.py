"""
lab-00-05-data-structures: 数据结构基础（list / tuple / dict / set）

运行时会展示：四种结构的创建、访问、增删改、以及「何时用哪种」的小结。
"""

print("=== 1. 列表 list（可变、有序）===\n")
print("  >>> [说明] 用 [] 创建，索引从 0 开始，负数索引从右往左")
fruits = ["苹果", "香蕉", "橙子"]
print(f"  fruits = {fruits}")
print(f"  第一个: fruits[0] = {fruits[0]}, 最后一个: fruits[-1] = {fruits[-1]}")

print("  >>> [说明] append 在末尾添加，insert(i, x) 在索引 i 处插入")
fruits.append("葡萄")
print(f"  append('葡萄') 后: {fruits}")
fruits.insert(1, "草莓")
print(f"  insert(1, '草莓') 后: {fruits}")

print("  >>> [说明] remove(值) 删第一个匹配项，del 列表[i] 删索引")
fruits.remove("香蕉")
print(f"  remove('香蕉') 后: {fruits}")
del fruits[0]
print(f"  del fruits[0] 后: {fruits}")
print(f"  长度 len(fruits) = {len(fruits)}\n")

print("=== 2. 元组 tuple（不可变、有序）===\n")
print("  >>> [说明] 用 () 创建，创建后不能改元素，适合「固定组合」")
point = (3, 4)
print(f"  point = {point}")
print(f"  point[0] = {point[0]}, point[1] = {point[1]}")
x, y = point
print(f"  解包: x, y = point -> x={x}, y={y}\n")

print("=== 3. 字典 dict（键值对、可变）===\n")
print("  >>> [说明] 用 {} 或 dict() 创建，键唯一，通过键访问值")
student = {"name": "Alice", "age": 20, "grade": "A"}
print(f"  student = {student}")
print(f"  访问: student['name'] = {student['name']}, student.get('age') = {student.get('age')}")

print("  >>> [说明] 直接赋值可新增或修改键值对")
student["city"] = "北京"
student["age"] = 21
print(f"  更新后: {student}")
del student["grade"]
print(f"  del student['grade'] 后: {student}")
print("  遍历 .items():")
for k, v in student.items():
    print(f"    {k}: {v}")
print()

print("=== 4. 集合 set（无序、不重复）===\n")
print("  >>> [说明] 用 {} 且无键值对，或 set(可迭代)，自动去重")
numbers = {1, 2, 3, 4, 5}
print(f"  numbers = {numbers}")
numbers.add(6)
print(f"  add(6) 后: {numbers}")
duplicates = {1, 2, 2, 3, 3, 3}
print(f"  去重示例: {{1,2,2,3,3,3}} -> {duplicates}")
print("  >>> [小结] 集合运算: & 交集 | 并集 - 差集")
set1, set2 = {1, 2, 3, 4}, {3, 4, 5, 6}
print(f"  交集 set1 & set2 = {set1 & set2}")
print(f"  并集 set1 | set2 = {set1 | set2}")
print(f"  差集 set1 - set2 = {set1 - set2}")
