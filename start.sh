#!/bin/bash

# ZDTrans 启动脚本

echo "🚀 启动 ZDTrans..."
echo ""

# 检查虚拟环境
if [ ! -d "venv" ] && [ ! -d ".venv" ]; then
    echo "❌ 未找到虚拟环境"
    echo "请先运行: python3 -m venv venv"
    exit 1
fi

# 激活虚拟环境
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# 检查配置文件
if [ ! -f "config.json" ]; then
    echo "⚠️  未找到配置文件"
    if [ -f "config.json.example" ]; then
        echo "正在创建配置文件..."
        cp config.json.example config.json
        echo "✅ 配置文件已创建: config.json"
        echo "请编辑 config.json 并填入你的 API Key"
        exit 0
    fi
fi

# 运行程序
python main.py
