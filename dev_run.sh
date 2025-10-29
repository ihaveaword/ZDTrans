#!/bin/bash
# 开发工具脚本 - 清理缓存并重启程序

echo "🧹 清理 Python 缓存..."
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -name ".DS_Store" -delete 2>/dev/null

echo "✅ 缓存已清理"
echo ""
echo "🚀 启动程序..."
source .venv/bin/activate
python main.py
