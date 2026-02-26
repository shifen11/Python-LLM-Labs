#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-13-http-protocol - 练习题

请完成以下练习题，完成后运行本文件验证你的答案。
注意：练习需要网络连接。
"""

import json
import httpx

# ========== 练习 1: 发送 HTTP GET 请求 ==========

print("=" * 50)
print("练习 1: 发送 HTTP GET 请求")
print("=" * 50)

# TODO: 使用 httpx 发送 GET 请求到 httpbin.org/get
# 提示：with httpx.Client() as client: client.get(url)
try:
    with httpx.Client(timeout=10) as client:
        response = client.get("https://httpbin.org/get")
        print(f"状态码: {response.status_code}")
        assert response.status_code == 200, "请求失败"
        print("✓ 练习 1 通过!\n")
except Exception as e:
    print(f"练习 1 失败: {e}\n")


# ========== 练习 2: 发送带查询参数的 GET 请求 ==========

print("=" * 50)
print("练习 2: 发送带查询参数的 GET 请求")
print("=" * 50)

# TODO: 发送 GET 请求，并携带查询参数 foo=bar, hello=world
# 提示：client.get(url, params={"foo": "bar", "hello": "world"})
try:
    with httpx.Client(timeout=10) as client:
        response = client.get(
            "https://httpbin.org/get",
            params={"foo": "bar", "hello": "world"}
        )
        data = response.json()
        args = data.get("args", {})
        print(f"查询参数: {args}")

        assert args == {"foo": "bar", "hello": "world"}, "查询参数不正确"
        print("✓ 练习 2 通过!\n")
except Exception as e:
    print(f"练习 2 失败: {e}\n")


# ========== 练习 3: 发送 POST 请求 ==========

print("=" * 50)
print("练习 3: 发送 POST 请求")
print("=" * 50)

# TODO: 发送 POST 请求到 httpbin.org/post，发送 JSON 数据
# 提示：client.post(url, json={"key": "value"})
try:
    payload = {"name": "张三", "age": 25}
    with httpx.Client(timeout=10) as client:
        response = client.post(
            "https://httpbin.org/post",
            json=payload
        )
        data = response.json()
        received_json = data.get("json", {})
        print(f"发送的数据: {payload}")
        print(f"接收到的数据: {received_json}")

        assert received_json == payload, "发送的数据与接收的数据不匹配"
        print("✓ 练习 3 通过!\n")
except Exception as e:
    print(f"练习 3 失败: {e}\n")


# ========== 练习 4: 解析 JSON 响应 ==========

print("=" * 50)
print("练习 4: 解析 JSON 响应")
print("=" * 50)

# TODO: 从 API 响应中解析 JSON 数据并提取特定字段
try:
    with httpx.Client(timeout=10) as client:
        response = client.get("https://httpbin.org/json")
        data = response.json()

        # 提取 slideshow.slides 数组中的第一个 slide 的 title
        # 提示：data["slideshow"]["slides"][0]["title"]
        first_slide_title = data["slideshow"]["slides"][0]["title"]

        print(f"第一个 slide 的标题: {first_slide_title}")

        assert first_slide_title == "Wake up to WonderWidgets!", "title 提取不正确"
        print("✓ 练习 4 通过!\n")
except Exception as e:
    print(f"练习 4 失败: {e}\n")


# ========== 练习 5: 处理不同的 HTTP 状态码 ==========

print("=" * 50)
print("练习 5: 处理不同的 HTTP 状态码")
print("=" * 50)

# TODO: 判断状态码是否为成功（2xx）
def is_success(status_code):
    """判断状态码是否为成功（2xx）"""
    # TODO: 实现这个函数
    # 提示：status_code 是否在 200-299 之间
    return 200 <= status_code < 300

# 测试
test_codes = [200, 201, 204, 301, 400, 404, 500]
for code in test_codes:
    result = is_success(code)
    print(f"  状态码 {code}: {'成功' if result else '失败'}")

# 验证
assert is_success(200) == True
assert is_success(201) == True
assert is_success(204) == True
assert is_success(301) == False
assert is_success(400) == False
assert is_success(404) == False
assert is_success(500) == False
print("✓ 练习 5 通过!\n")


# ========== 练习 6: JSON 序列化和反序列化 ==========

print("=" * 50)
print("练习 6: JSON 序列化和反序列化")
print("=" * 50)

# TODO: 将 Python 对象转换为 JSON 字符串，再转回来
python_obj = {
    "id": 1,
    "name": "张三",
    "skills": ["Python", "JavaScript"]
}

# 1. 序列化：Python 对象 → JSON 字符串
# 提示：json.dumps(obj, ensure_ascii=False)
json_str = json.dumps(python_obj, ensure_ascii=False)
print(f"JSON 字符串: {json_str}")

# 2. 反序列化：JSON 字符串 → Python 对象
# 提示：json.loads(json_str)
python_obj2 = json.loads(json_str)
print(f"Python 对象: {python_obj2}")

# 验证
assert python_obj == python_obj2, "序列化和反序列化结果不一致"
print("✓ 练习 6 通过!\n")


# ========== 练习 7: 设置请求头 ==========

print("=" * 50)
print("练习 7: 设置请求头")
print("=" * 50)

# TODO: 发送请求时设置自定义请求头
try:
    with httpx.Client(timeout=10) as client:
        response = client.get(
            "https://httpbin.org/headers",
            headers={
                "X-Custom-Header": "CustomValue",
                "User-Agent": "MyApp/1.0"
            }
        )
        data = response.json()
        headers = data.get("headers", {})

        print(f"自定义请求头: {headers.get('X-Custom-Header')}")
        print(f"User-Agent: {headers.get('User-Agent')}")

        assert headers.get("X-Custom-Header") == "CustomValue", "自定义请求头设置失败"
        assert "MyApp/1.0" in headers.get("User-Agent", ""), "User-Agent 设置失败"
        print("✓ 练习 7 通过!\n")
except Exception as e:
    print(f"练习 7 失败: {e}\n")


# ========== 练习 8: REST API 路径设计 ==========

print("=" * 50)
print("练习 8: REST API 路径设计")
print("=" * 50)

# TODO: 为以下操作设计 REST API 路径和 HTTP 方法
# 资源：用户（User）
# 操作：获取所有用户、获取单个用户、创建用户、更新用户、删除用户

api_design = {
    "获取所有用户": "GET    /users",
    "获取单个用户": "GET    /users/{id}",
    "创建用户": "POST   /users",
    "更新用户": "PUT    /users/{id}",
    "删除用户": "DELETE /users/{id}",
}

print("REST API 路径设计:")
for operation, path in api_design.items():
    print(f"  {operation}: {path}")

# 验证（检查关键路径）
assert "/users" in api_design["获取所有用户"], "路径不正确"
assert "/users" in api_design["创建用户"], "路径不正确"
assert "DELETE" in api_design["删除用户"], "方法不正确"
print("✓ 练习 8 通过!\n")


print("=" * 50)
print("所有练习完成！")
print("=" * 50)
