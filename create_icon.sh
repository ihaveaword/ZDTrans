#!/bin/bash
# 创建 macOS .icns 图标文件

echo "🎨 创建 macOS 应用图标..."

# 检查是否有源图片
if [ ! -f "resources/icons/icon.png" ]; then
    echo "❌ 找不到 resources/icons/icon.png"
    exit 1
fi

# 创建临时目录
ICONSET="resources/icons/AppIcon.iconset"
mkdir -p "$ICONSET"

# 生成各种尺寸的图标
echo "📐 生成多种尺寸..."
sips -z 16 16     resources/icons/icon.png --out "$ICONSET/icon_16x16.png" 2>/dev/null
sips -z 32 32     resources/icons/icon.png --out "$ICONSET/icon_16x16@2x.png" 2>/dev/null
sips -z 32 32     resources/icons/icon.png --out "$ICONSET/icon_32x32.png" 2>/dev/null
sips -z 64 64     resources/icons/icon.png --out "$ICONSET/icon_32x32@2x.png" 2>/dev/null
sips -z 128 128   resources/icons/icon.png --out "$ICONSET/icon_128x128.png" 2>/dev/null
sips -z 256 256   resources/icons/icon.png --out "$ICONSET/icon_128x128@2x.png" 2>/dev/null
sips -z 256 256   resources/icons/icon.png --out "$ICONSET/icon_256x256.png" 2>/dev/null
sips -z 512 512   resources/icons/icon.png --out "$ICONSET/icon_256x256@2x.png" 2>/dev/null
sips -z 512 512   resources/icons/icon.png --out "$ICONSET/icon_512x512.png" 2>/dev/null
sips -z 1024 1024 resources/icons/icon.png --out "$ICONSET/icon_512x512@2x.png" 2>/dev/null

# 转换为 icns
echo "🔄 转换为 .icns 格式..."
iconutil -c icns "$ICONSET" -o resources/icons/icon.icns

if [ $? -eq 0 ]; then
    echo "✅ 图标创建成功: resources/icons/icon.icns"
    # 清理临时文件
    rm -rf "$ICONSET"
else
    echo "❌ 图标转换失败"
    exit 1
fi
