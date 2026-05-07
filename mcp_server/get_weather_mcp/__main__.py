# -*- coding: utf-8 -*-
# 设置文件编码为UTF-8，确保中文等字符正常显示

# 导入异步IO库，用于运行异步服务
import asyncio
# 导入操作系统相关功能，用于读取环境变量
import os

# 从当前包目录下导入 server 模块（就是你之前写的 FastMCP 服务）
from . import server

# 从环境变量读取 HOST，不存在则默认使用 127.0.0.1（本地）
host = os.getenv('HOST', '127.0.0.1')
# 从环境变量读取 PORT，不存在则默认使用 8000 端口
port = int(os.getenv('PORT', 8000))


def stdio():
    """
    标准输入输出模式启动入口（用于 AI 客户端直接调用）
    这是 MCP 标准通信方式，适合 Cursor、Claude、豆包 等 AI 工具
    """
    # 异步运行 MCP 服务，使用 stdio 传输协议
    asyncio.run(server.mcp.run(transport="stdio"))


def http():
    """
    HTTP 服务启动入口（用于网页/API 形式提供 MCP 服务）
    可以通过浏览器、HTTP 请求调用这个天气工具
    """
    # 异步运行 MCP 服务，使用 http 传输协议
    asyncio.run(server.mcp.run(
        transport="http",  # 传输方式：HTTP
        host=host,         # 绑定地址
        port=port,         # 绑定端口
        path="/mcp"        # 请求路径：http://localhost:8000/mcp
    ))


# 如果直接运行此文件，默认启动 HTTP 服务
if __name__ == "__main__":
    http()