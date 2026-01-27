# lab-11-api-integration

**使用 httpx / requests 调用外部 API**

## 知识点

- `requests.get` / `post`、`response.json()`
- `httpx` 支持同步与异步，与 FastAPI 生态一致
- 本 demo 使用公开 API（如 httpbin）避免密钥

## 运行

```bash
pip install httpx requests
python main.py
```

注意：会发起真实 HTTP 请求，需网络。
