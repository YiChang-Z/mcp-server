from typing import Optional
from fastmcp import FastMCP

# 1. 建立 FastMCP 實例
app = FastMCP("My MCP Server")

# 2. 提供一個私有的服務或資料給 ChatGPT/Claude
@app.tool()
def get_private_core_value(task_progress: Optional[any] = None) -> str:
    """Provide private setting value of user okey"""
    return "ey_JjawQi0iI0Y2M3MzM1NC02MDU0LTRkNmItODJlMVMzI0MDQ1ZmEilCjJc"

# 3. 兩數相加的工具
@app.tool()
def add_numbers(a: int, b: int, task_progress: Optional[any] = None) -> int:
    """Add Two Numbers"""
    return a + b

if __name__ == "__main__":
    app.run()