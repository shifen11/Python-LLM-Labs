# lab-13-http-protocol - HTTP 协议入门

## 简介

本实验室介绍 HTTP（Hypertext Transfer Protocol）协议的基础概念，包括请求/响应结构、状态码、REST API 基础、以及如何使用 httpx 发送 HTTP 请求和处理 JSON 数据。这些知识是理解 API 集成（lab-14）和 FastAPI 服务开发（lab-17）的重要基础。

## 学习目标

- 理解 HTTP 请求和响应的基本结构
- 掌握常见的 HTTP 状态码及其含义
- 理解 REST API 的基本概念和设计原则
- 能够使用 httpx 发送各种 HTTP 请求
- 掌握 JSON 数据的序列化和反序列化

## 运行方法

### 交互式演示

```bash
python main.py
```

### 练习题

```bash
python exercises.py
```

## 核心概念

### HTTP 请求结构

```
GET /api/users HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Content-Type: application/json
Authorization: Bearer token123

{"name": "张三", "age": 25}
```

### HTTP 响应结构

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 42

{"id": 1, "name": "张三", "age": 25}
```

### 常见 HTTP 状态码

| 状态码 | 类别 | 说明 | 示例 |
|-------|------|------|------|
| 200 | 成功 | 请求成功 | OK |
| 201 | 成功 | 资源创建成功 | Created |
| 301 | 重定向 | 永久重定向 | Moved Permanently |
| 302 | 重定向 | 临时重定向 | Found |
| 400 | 客户端错误 | 请求参数错误 | Bad Request |
| 401 | 客户端错误 | 未认证 | Unauthorized |
| 403 | 客户端错误 | 无权限 | Forbidden |
| 404 | 客户端错误 | 资源不存在 | Not Found |
| 500 | 服务器错误 | 服务器内部错误 | Internal Server Error |

### REST API 基础

REST（Representational State Transfer）是一种软件架构风格，主要原则：

- **无状态**：每个请求包含所有必要信息
- **统一接口**：使用标准的 HTTP 方法
- **资源导向**：通过 URI 访问资源

常用 HTTP 方法与 CRUD 操作对应：

| HTTP 方法 | CRUD 操作 | 说明 |
|-----------|----------|------|
| GET | Read | 获取资源 |
| POST | Create | 创建资源 |
| PUT / PATCH | Update | 更新资源 |
| DELETE | Delete | 删除资源 |

## 内容概览

### main.py 演示内容

1. **HTTP 请求/响应结构**
   - 请求行、请求头、请求体
   - 状态行、响应头、响应体

2. **HTTP 状态码**
   - 2xx 成功状态
   - 3xx 重定向状态
   - 4xx 客户端错误
   - 5xx 服务器错误

3. **REST API 基础**
   - REST 设计原则
   - HTTP 方法与 CRUD 对应

4. **使用 httpx 发送请求**
   - GET 请求
   - POST 请求
   - 处理响应

5. **JSON 数据处理**
   - `json.loads()` 反序列化
   - `json.dumps()` 序列化

### exercises.py 练习题

1. 发送 HTTP GET 请求
2. 发送 HTTP POST 请求
3. 解析 JSON 响应
4. 处理不同的 HTTP 状态码
5. 构造 REST API 请求

## 前置知识

- Python 基础语法
- 网络编程基础（lab-11）
- JSON 数据格式

## 后续关联

- **lab-12-asyncio-concurrency**：异步 HTTP 请求
- **lab-14-api-integration**：调用外部 API
- **lab-17-fastapi-service**：开发 HTTP 服务

## 注意事项

- 演示需要网络连接
- 使用公开 API（httpbin.org）避免密钥
- httpx 是现代 Python HTTP 客户端，支持同步和异步
