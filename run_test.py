#!/usr/bin/env python3
"""简单测试主窗口"""
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

# 在 macOS 上启用高 DPI 支持
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

from src.main_window import MainWindow

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

print("创建主窗口...")
window = MainWindow()

print(f"窗口创建完成")
print(f"窗口标题: {window.windowTitle()}")
print(f"窗口大小: {window.size().width()}x{window.size().height()}")

print("显示主窗口...")
window.show()
window.raise_()
window.activateWindow()

print(f"窗口是否可见: {window.isVisible()}")
print(f"窗口是否激活: {window.isActiveWindow()}")
print("")
print("=" * 60)
print("主窗口应该已经显示在屏幕上了！")
print("如果看不到，请检查:")
print("1. 是否被其他窗口遮挡")
print("2. 是否在其他桌面/空间")
print("3. 按 Cmd+Tab 查看是否在应用列表中")
print("=" * 60)
print("")
print("按 Ctrl+C 退出")

sys.exit(app.exec())
