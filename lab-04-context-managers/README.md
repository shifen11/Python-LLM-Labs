# lab-04-context-managers

**`with` 语句与上下文管理器**

## 知识点

- `with EXPR as x:` 确保进入时 `__enter__`、退出时 `__exit__` 被调用
- 对比 Java `try-with-resources`，用于资源获取与释放
- 实现方式：`__enter__` / `__exit__` 协议，或 `@contextmanager` + `yield`

## 运行

```bash
python main.py
```
