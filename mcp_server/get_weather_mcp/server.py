# -*- coding: utf-8 -*-
# 声明文件编码为UTF-8，确保中文等字符能正常显示

# 从fastmcp库中导入FastMCP类，用于快速创建MCP工具服务
from fastmcp import FastMCP

# 创建一个MCP服务实例，服务名称为"get_weather_mcp"
# 这个名称会被AI客户端识别，用来区分不同的MCP服务
mcp = FastMCP("get_weather_mcp")

# 使用@mcp.tool装饰器，将下面的函数注册为一个可供AI调用的工具
@mcp.tool
def get_weather(city: str) -> str:
    """
    函数文档字符串（说明）：
    获取指定城市的天气信息
    :param city: 字符串类型，代表要查询天气的城市名称
    :return: 字符串类型，返回天气描述信息
    """
    # 函数核心逻辑：返回固定的模拟天气信息
    # 把传入的城市名拼接到返回字符串中
    return f"It's always sunny in {city}!"

# 判断当前脚本是否是被直接运行（而不是被其他文件导入）
if __name__ == "__main__":
    # 启动MCP服务，开始监听AI客户端的调用请求
    mcp.run()