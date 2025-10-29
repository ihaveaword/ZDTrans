#!/bin/bash
# 快速打包脚本 - macOS

echo "📦 开始打包 ZDTrans..."
echo ""

# 检查虚拟环境
if [ ! -d ".venv" ]; then
    echo "❌ 虚拟环境不存在，请先创建"
    exit 1
fi

# 激活虚拟环境
source .venv/bin/activate

# 检查 PyInstaller
if ! command -v pyinstaller &> /dev/null; then
    echo "📥 安装 PyInstaller..."
    pip install pyinstaller
fi

# 清理旧的打包文件
echo "🧹 清理旧文件..."
rm -rf build dist *.spec 2>/dev/null

# 打包
echo "🔨 开始打包..."
pyinstaller --name="ZDTrans" \
    --windowed \
    --onefile \
    --add-data="config.json.example:." \
    --add-data="README.md:." \
    --add-data="docs:docs" \
    --hidden-import="pynput.keyboard._darwin" \
    --hidden-import="pynput.mouse._darwin" \
    --exclude-module="matplotlib" \
    --exclude-module="numpy" \
    --exclude-module="pandas" \
    main.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 打包成功！"
    echo ""
    echo "📁 可执行文件位置: dist/ZDTrans"
    echo ""
    echo "📝 下一步："
    echo "1. 测试运行: ./dist/ZDTrans"
    echo "2. 创建 DMG: 见文档"
    echo "3. 发布到 GitHub"
else
    echo ""
    echo "❌ 打包失败，请检查错误信息"
    exit 1
fi
