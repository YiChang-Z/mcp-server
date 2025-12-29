FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# 暴露 fastmcp 預設的 8000 埠 (或你指定的埠)
EXPOSE 10000
# 啟動指令，對應你之前的 fastmcp run 指令
CMD ["fastmcp", "run", "app.py", "--transport", "http", "--host", "0.0.0.0", "--port", "10000"]