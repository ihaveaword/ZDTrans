#!/bin/bash
# 创建 macOS DMG 安装程序

VERSION="1.2.3"
APP_NAME="ZDTrans"
DMG_NAME="${APP_NAME}-v${VERSION}-macOS"

echo "📦 创建 DMG 安装程序..."
echo ""

# 检查应用是否存在
if [ ! -d "dist/${APP_NAME}.app" ]; then
    echo "❌ 找不到 dist/${APP_NAME}.app"
    echo "请先运行: pyinstaller zdtrans.spec"
    exit 1
fi

# 创建临时目录
TMP_DIR="tmp_dmg"
rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR"

# 复制应用到临时目录
echo "📁 准备文件..."
cp -r "dist/${APP_NAME}.app" "$TMP_DIR/"

# 创建应用程序文件夹的符号链接
ln -s /Applications "$TMP_DIR/Applications"

# 可选：添加背景图片和自定义样式
# mkdir -p "$TMP_DIR/.background"
# cp resources/dmg-background.png "$TMP_DIR/.background/"

# 创建 DMG
echo "🔨 创建 DMG..."
hdiutil create -volname "$APP_NAME" \
    -srcfolder "$TMP_DIR" \
    -ov -format UDZO \
    "release/${DMG_NAME}.dmg"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ DMG 创建成功！"
    echo ""
    echo "📁 位置: release/${DMG_NAME}.dmg"
    echo "📊 大小: $(du -h "release/${DMG_NAME}.dmg" | cut -f1)"
    echo ""
    echo "📝 使用说明:"
    echo "1. 双击 DMG 文件"
    echo "2. 将 ${APP_NAME}.app 拖到 Applications 文件夹"
    echo "3. 完成安装！"
else
    echo ""
    echo "❌ DMG 创建失败"
    exit 1
fi

# 清理临时文件
rm -rf "$TMP_DIR"

echo ""
echo "🎉 完成！"
