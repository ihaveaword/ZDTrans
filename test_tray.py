#!/usr/bin/env python3
"""
测试托盘图标是否正常显示
"""

import sys
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QFont
from PySide6.QtCore import Qt

def test_tray():
    print("=" * 50)
    print("ZDTrans 托盘图标测试")
    print("=" * 50)
    
    app = QApplication(sys.argv)
    
    # 1. 检查系统是否支持托盘
    print("\n1️⃣ 检查系统托盘支持...")
    if QSystemTrayIcon.isSystemTrayAvailable():
        print("   ✅ 系统支持托盘图标")
    else:
        print("   ❌ 系统不支持托盘图标")
        print("   💡 macOS 用户请检查系统设置")
        return
    
    # 2. 创建托盘图标
    print("\n2️⃣ 创建托盘图标...")
    tray = QSystemTrayIcon()
    
    # 创建一个明显的蓝色图标
    pixmap = QPixmap(64, 64)
    pixmap.fill(QColor(0, 0, 0, 0))
    
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setBrush(QColor(0, 120, 215))  # 蓝色
    painter.setPen(QColor(255, 255, 255))
    painter.drawEllipse(8, 8, 48, 48)
    
    font = QFont("Arial", 32, QFont.Bold)
    painter.setFont(font)
    painter.setPen(QColor(255, 255, 255))
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "T")
    painter.end()
    
    tray.setIcon(QIcon(pixmap))
    tray.setToolTip("ZDTrans 测试图标 - 如果看到我，说明托盘正常！")
    
    # 创建菜单
    menu = QMenu()
    menu.addAction("✅ 托盘图标正常显示！")
    menu.addSeparator()
    quit_action = menu.addAction("退出测试")
    quit_action.triggered.connect(app.quit)
    
    tray.setContextMenu(menu)
    
    # 左键点击事件
    def on_activated(reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            menu.popup(app.primaryScreen().availableGeometry().center())
    
    tray.activated.connect(on_activated)
    
    # 显示托盘
    tray.show()
    
    print("   ✅ 托盘图标已创建")
    
    # 3. 检查是否可见
    print("\n3️⃣ 检查托盘图标可见性...")
    if tray.isVisible():
        print("   ✅ 托盘图标已显示")
    else:
        print("   ⚠️  托盘图标未显示")
    
    # 4. 显示使用说明
    print("\n" + "=" * 50)
    print("📍 在哪里找到托盘图标？")
    print("=" * 50)
    print("\nmacOS:")
    print("  - 查看屏幕 **右上角** 状态栏")
    print("  - 找到一个 **蓝色圆形** 图标，中间有字母 'T'")
    print("  - **左键点击** 图标可打开菜单")
    print("\n如果没看到:")
    print("  1. 点击状态栏右上角的向下箭头 ⌄ 展开隐藏图标")
    print("  2. 检查 系统偏好设置 > 控制中心")
    print("  3. 尝试移动鼠标到状态栏不同位置")
    print("\n💡 按 Ctrl+C 退出测试\n")
    print("=" * 50)
    
    # 显示一条通知确认托盘工作
    tray.showMessage(
        "ZDTrans 托盘测试",
        "如果您看到这条通知，说明托盘图标正常工作！\n请在屏幕右上角找到蓝色圆形图标。",
        QSystemTrayIcon.Information,
        5000
    )
    
    sys.exit(app.exec())

if __name__ == "__main__":
    test_tray()
