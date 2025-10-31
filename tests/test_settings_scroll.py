#!/usr/bin/env python3
"""
测试设置窗口滚动功能
"""

import sys
from PySide6.QtWidgets import QApplication
from src.settings import SettingsDialog
from src.utils import load_config

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 加载配置
    config = load_config()
    
    # 创建设置对话框
    dialog = SettingsDialog(config)
    dialog.show()
    
    print("✅ 设置窗口已打开")
    print("📋 功能说明：")
    print("  - 窗口高度限制在 600-800px")
    print("  - 内容超出时会显示滚动条")
    print("  - 保存和取消按钮固定在底部")
    print("  - 滚动条样式美化（日间/夜间模式）")
    
    sys.exit(app.exec())
