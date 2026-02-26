#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-13-http-protocol - HTTP 协议入门

本脚本演示 HTTP 协议的基础概念和 httpx 的使用。
注意：演示需要网络连接。
"""

import json
import httpx

# >>> [说明] HTTP（Hypertext Transfer Protocol）是 Web 应用的基础协议
# 现代应用开发离不开 HTTP API 调用


# ========== 1. HTTP 请求结构 ==========

print("=" * 50)
print("1. HTTP 请求结构")
print("=" * 50)

print("""
HTTP 请求由三部分组成：
  1. 请求行（Request Line）
  2. 请求头（Headers）
  3. 请求体（Body，可选）

示例（GET 请求）:
  GET /api/users HTTP/1.1           ← 请求行
  Host: example.com                 ← 请求头
  User-Agent: Mozilla/5.0           ←
  Content-Type: application/json    ←
  Authorization: Bearer token123     ←

示例（POST 请求）:
  POST /api/users HTTP/1.1          ← 请求行
  Host: example.com                 ← 请求头
  Content-Type: application/json    ←
  Content-Length: 42                ←
                                    ← 空行
  {"name": "张三", "age": 25}      ← 请求体
""")

print("请求行格式:")
print("  方法 路径 HTTP/版本")
print("  示例: GET /api/users HTTP/1.1")

print("\n常见的 HTTP 方法:")
print("  GET    - 获取资源")
print("  POST   - 创建资源")
print("  PUT    - 完整更新资源")
print("  PATCH  - 部分更新资源")
print("  DELETE - 删除资源")


# ========== 2. HTTP 响应结构 ==========

print("\n" + "=" * 50)
print("2. HTTP 响应结构")
print("=" * 50)

print("""
HTTP 响应由三部分组成：
  1. 状态行（Status Line）
  2. 响应头（Headers）
  3. 响应体（Body）

示例:
  HTTP/1.1 200 OK                   ← 状态行
  Content-Type: application/json    ← 响应头
  Content-Length: 42                ←
  Server: nginx/1.18.0              ←
                                    ← 空行
  {"id": 1, "name": "张三"}        ← 响应体
""")

print("状态行格式:")
print("  HTTP/版本 状态码 状态描述")
print("  示例: HTTP/1.1 200 OK")


# ========== 3. HTTP 状态码 ==========

print("\n" + "=" * 50)
print("3. HTTP 状态码")
print("=" * 50)

print("""
状态码分类:
  2xx - 成功
  3xx - 重定向
  4xx - 客户端错误
  5xx - 服务器错误
""")

print("常见状态码:")

status_codes = {
    200: "OK - 请求成功",
    201: "Created - 资源创建成功",
    204: "No Content - 成功但无返回内容",
    301: "Moved Permanently - 永久重定向",
    302: "Found - 临时重定向",
    400: "Bad Request - 请求参数错误",
    401: "Unauthorized - 未认证",
    403: "Forbidden - 无权限访问",
    404: "Not Found - 资源不存在",
    422: "Unprocessable Entity - 请求格式正确但语义错误",
    500: "Internal Server Error - 服务器内部错误",
    502: "Bad Gateway - 网关错误",
    503: "Service Unavailable - 服务暂时不可用",
}

for code, desc in status_codes.items():
    category = "成功" if 200 <= code < 300 else \
               "重定向" if 300 <= code < 400 else \
               "客户端错误" if 400 <= code < 500 else "服务器错误"
    print(f"  {code} - [{category}] {desc}")


# ========== 4. REST API 基础 ==========

print("\n" + "=" * 50)
print("4. REST API 基础")
print("=" * 50)

print("""
REST（Representational State Transfer）是一种软件架构风格。

核心原则:
  1. 无状态（Stateless）- 每个请求包含所有必要信息
  2. 统一接口（Uniform Interface）- 使用标准 HTTP 方法
  3. 资源导向（Resource-Oriented）- 通过 URI 访问资源

RESTful API 设计:
  - 使用名词表示资源（如 /users, /products）
  - 使用 HTTP 方法表示操作（如 GET, POST）
  - 使用合适的状态码表示结果
""")

print("REST API 的 HTTP 方法与 CRUD 对应:")
rest_methods = [
    ("GET", "/users", "获取所有用户"),
    ("GET", "/users/1", "获取 ID 为 1 的用户"),
    ("POST", "/users", "创建新用户"),
    ("PUT", "/users/1", "完整更新 ID 为 1 的用户"),
    ("PATCH", "/users/1", "部分更新 ID 为 1 的用户"),
    ("DELETE", "/users/1", "删除 ID 为 1 的用户"),
]

for method, path, desc in rest_methods:
    print(f"  {method:6s} {path:15s} - {desc}")


# ========== 5. 使用 httpx 发送 GET 请求 ==========

print("\n" + "=" * 50)
print("5. 使用 httpx 发送 GET 请求")
print("=" * 50)

# >>> [说明] httpx 是现代 Python HTTP 客户端，支持同步和异步
# >>> [说明] 它比 requests 更现代，与 FastAPI 生态一致

def get_request_demo():
    """演示 GET 请求"""
    try:
        with httpx.Client(timeout=10) as client:
            # 发送 GET 请求
            print("  >>> [触发] 发送 GET 请求到 httpbin.org/get")
            response = client.get(
                "https://httpbin.org/get",
                params={"foo": "bar", "hello": "world"}
            )

            # 获取响应信息
            print(f"  状态码: {response.status_code}")
            print(f"  响应头: {dict(response.headers)}")

            # 解析 JSON 响应
            data = response.json()
            print(f"  响应数据: {json.dumps(data, indent=2, ensure_ascii=False)}")

            return response

    except httpx.TimeoutException:
        print("  [错误] 请求超时")
        return None
    except Exception as e:
        print(f"  [错误] {e}")
        return None

get_response = get_request_demo()


# ========== 6. 使用 httpx 发送 POST 请求 ==========

print("\n" + "=" * 50)
print("6. 使用 httpx 发送 POST 请求")
print("=" * 50)

def post_request_demo():
    """演示 POST 请求"""
    try:
        with httpx.Client(timeout=10) as client:
            # 准备请求数据
            data = {
                "name": "张三",
                "age": 25,
                "email": "zhangsan@example.com"
            }

            # 发送 POST 请求
            print("  >>> [触发] 发送 POST 请求到 httpbin.org/post")
            response = client.post(
                "https://httpbin.org/post",
                json=data,  # 自动设置 Content-Type: application/json
                headers={"X-Custom-Header": "CustomValue"}
            )

            print(f"  状态码: {response.status_code}")

            # 解析 JSON 响应
            result = response.json()
            print(f"  发送的 JSON 数据: {result['json']}")

            return response

    except Exception as e:
        print(f"  [错误] {e}")
        return None

post_response = post_request_demo()


# ========== 7. 处理响应状态码 ==========

print("\n" + "=" * 50)
print("7. 处理响应状态码")
print("=" * 50)

# >>> [说明] raise_for_status() 会在 4xx/5xx 状态码时抛出异常

def handle_status_codes():
    """演示状态码处理"""
    try:
        with httpx.Client(timeout=10) as client:
            print("  请求成功的情况:")
            response = client.get("https://httpbin.org/status/200")
            response.raise_for_status()
            print(f"    状态码 {response.status_code}: 成功")

            print("\n  请求失败的情况:")
            response = client.get("https://httpbin.org/status/404")
            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                print(f"    状态码 {e.response.status_code}: {e.response.reason_phrase}")

    except Exception as e:
        print(f"  [错误] {e}")

handle_status_codes()


# ========== 8. JSON 数据处理 ==========

print("\n" + "=" * 50)
print("8. JSON 数据处理")
print("=" * 50)

# >>> [说明] JSON（JavaScript Object Notation）是常用的数据交换格式

# JSON 序列化（Python 对象 → JSON 字符串）
python_obj = {
    "id": 1,
    "name": "张三",
    "age": 25,
    "skills": ["Python", "JavaScript"],
    "address": {
        "city": "北京",
        "district": "朝阳区"
    }
}

json_str = json.dumps(python_obj, ensure_ascii=False, indent=2)
print("Python 对象 → JSON 字符串:")
print(json_str)

# JSON 反序列化（JSON 字符串 → Python 对象）
json_data = '{"id": 2, "name": "李四", "age": 30}'
python_obj2 = json.loads(json_data)
print(f"\nJSON 字符串 → Python 对象: {python_obj2}")

# 从 API 响应中提取数据
print("\n从 API 响应中提取数据:")
if get_response:
    data = get_response.json()
    print(f"  请求 URL: {data.get('url')}")
    print(f"  查询参数: {data.get('args')}")


# ========== 9. HTTP 请求头和响应头 ==========

print("\n" + "=" * 50)
print("9. HTTP 请求头和响应头")
print("=" * 50)

# >>> [说明] 请求头包含客户端信息，响应头包含服务器信息

print("常见的 HTTP 请求头:")
common_headers = {
    "User-Agent": "标识客户端类型",
    "Accept": "指定可接受的响应类型",
    "Content-Type": "指定请求体的类型",
    "Authorization": "认证信息",
    "Cookie": "Cookie 数据",
}
for header, desc in common_headers.items():
    print(f"  {header}: {desc}")

print("\n常见的 HTTP 响应头:")
response_headers = {
    "Content-Type": "响应体的类型",
    "Content-Length": "响应体的长度",
    "Server": "服务器信息",
    "Set-Cookie": "设置 Cookie",
    "Cache-Control": "缓存控制",
}
for header, desc in response_headers.items():
    print(f"  {header}: {desc}")

# 查看实际的响应头
if get_response:
    print("\n实际响应头示例:")
    for key, value in get_response.headers.items():
        print(f"  {key}: {value}")


# ========== 10. 错误处理和超时 ==========

print("\n" + "=" * 50)
print("10. 错误处理和超时")
print("=" * 50)

def error_handling_demo():
    """演示错误处理"""
    try:
        with httpx.Client(timeout=1) as client:  # 1秒超时
            print("  >>> [触发] 发送请求到不存在的地址")
            response = client.get("https://this-domain-does-not-exist-12345.com")
            return response

    except httpx.TimeoutException:
        print("  [错误] 请求超时")
    except httpx.ConnectError:
        print("  [错误] 连接失败")
    except httpx.HTTPStatusError as e:
        print(f"  [错误] HTTP 状态错误: {e.response.status_code}")
    except Exception as e:
        print(f"  [错误] {type(e).__name__}: {e}")

error_handling_demo()


print("\n" + "=" * 50)
print("实验室演示完成！")
print("=" * 50)
print("""
重要提示:
  1. HTTP 是现代 Web 应用的基础协议
  2. httpx 是推荐的 HTTP 客户端库（支持同步和异步）
  3. 后续学习:
     - lab-12: asyncio 异步网络编程
     - lab-14: API 集成（深入使用 httpx）
     - lab-17: FastAPI 服务开发
""")
