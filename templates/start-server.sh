#!/usr/bin/env bash
# start-server.sh — 课程 HTTP 服务器一键启动
# 用法: bash start-server.sh
# 使用 Python 内置 HTTP 服务器，自动打开浏览器到第一课

PORT=${1:-8000}
DEFAULT=""

if [ -f "index.html" ]; then
  DEFAULT="http://localhost:$PORT/index.html"
else
  FIRST=$(ls lessons/*.html 2>/dev/null | sort | head -1)
  if [ -n "$FIRST" ]; then
    DEFAULT="http://localhost:$PORT/$(basename "$FIRST")"
  else
    DEFAULT="http://localhost:$PORT/"
  fi
fi

echo "=== teach_more_pic 课程服务器 ==="
echo "端口: $PORT"
echo "打开: $DEFAULT"
echo "按 Ctrl+C 停止服务器"
echo ""

# macOS
if command -v open &>/dev/null; then
  open "$DEFAULT"
# Linux
elif command -v xdg-open &>/dev/null; then
  xdg-open "$DEFAULT"
fi

python3 -m http.server "$PORT" --bind 127.0.0.1
