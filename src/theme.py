"""
主题管理模块
提供日间/夜间模式切换功能
"""

from PySide6.QtCore import QObject, Signal


class ThemeManager(QObject):
    """主题管理器"""
    
    theme_changed = Signal(str)  # 主题改变信号
    
    def __init__(self):
        super().__init__()
        self._current_theme = 'light'  # 默认浅色主题
        
    def set_theme(self, theme):
        """设置主题"""
        if theme in ['light', 'dark']:
            self._current_theme = theme
            self.theme_changed.emit(theme)
            
    def get_theme(self):
        """获取当前主题"""
        return self._current_theme
        
    def toggle_theme(self):
        """切换主题"""
        new_theme = 'dark' if self._current_theme == 'light' else 'light'
        self.set_theme(new_theme)
        return new_theme
        
    @staticmethod
    def get_main_window_style(theme='light'):
        """获取主窗口样式"""
        if theme == 'dark':
            return """
                QMainWindow {
                    background-color: #1e1e1e;
                }
                QGroupBox {
                    font-family: 'PingFang SC';
                    font-size: 13px;
                    font-weight: bold;
                    border: 2px solid #3c3c3c;
                    border-radius: 6px;
                    margin-top: 10px;
                    padding: 15px 10px 10px 10px;
                    background-color: #2d2d2d;
                    color: #e0e0e0;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 5px;
                    color: #e0e0e0;
                }
                QLabel {
                    color: #e0e0e0;
                }
                QTextEdit {
                    background-color: #2d2d2d;
                    border: 1px solid #3c3c3c;
                    border-radius: 4px;
                    color: #e0e0e0;
                }
                QStatusBar {
                    background-color: #2d2d2d;
                    color: #e0e0e0;
                }
            """
        else:
            return """
                QMainWindow {
                    background-color: #f5f5f5;
                }
                QGroupBox {
                    font-family: 'PingFang SC';
                    font-size: 13px;
                    font-weight: bold;
                    border: 2px solid #ddd;
                    border-radius: 6px;
                    margin-top: 10px;
                    padding: 15px 10px 10px 10px;
                    background-color: white;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 5px;
                }
            """
            
    @staticmethod
    def get_popup_style(theme='light'):
        """获取弹出窗口样式"""
        if theme == 'dark':
            return """
                QWidget {
                    background-color: rgba(30, 30, 30, 240);
                    border-radius: 10px;
                    color: #e0e0e0;
                }
                QTextEdit {
                    background-color: rgba(45, 45, 45, 200);
                    border: none;
                    border-radius: 5px;
                    padding: 10px;
                    color: #e0e0e0;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: rgba(60, 60, 60, 200);
                    border: none;
                    border-radius: 5px;
                    padding: 8px 16px;
                    color: #e0e0e0;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: rgba(80, 80, 80, 200);
                }
                QLabel {
                    color: rgba(224, 224, 224, 180);
                    font-size: 12px;
                }
            """
        else:
            return """
                QWidget {
                    background-color: rgba(40, 40, 40, 240);
                    border-radius: 10px;
                    color: white;
                }
                QTextEdit {
                    background-color: rgba(60, 60, 60, 200);
                    border: none;
                    border-radius: 5px;
                    padding: 10px;
                    color: white;
                    font-size: 14px;
                }
                QPushButton {
                    background-color: rgba(80, 80, 80, 200);
                    border: none;
                    border-radius: 5px;
                    padding: 8px 16px;
                    color: white;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: rgba(100, 100, 100, 200);
                }
                QLabel {
                    color: rgba(255, 255, 255, 180);
                    font-size: 12px;
                }
            """
            
    @staticmethod
    def get_settings_style(theme='light'):
        """获取设置对话框样式"""
        if theme == 'dark':
            return """
                QDialog {
                    background-color: #1e1e1e;
                }
                QScrollArea {
                    border: none;
                    background-color: #1e1e1e;
                }
                QScrollBar:vertical {
                    background-color: #2d2d2d;
                    width: 12px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical {
                    background-color: #5c5c5c;
                    border-radius: 6px;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background-color: #6c6c6c;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QGroupBox {
                    font-weight: bold;
                    border: 2px solid #3c3c3c;
                    border-radius: 6px;
                    margin-top: 10px;
                    padding: 15px 10px 10px 10px;
                    background-color: #2d2d2d;
                    color: #e0e0e0;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 5px;
                    color: #e0e0e0;
                }
                QLabel {
                    color: #e0e0e0;
                }
                QLineEdit, QTextEdit {
                    background-color: #2d2d2d;
                    border: 1px solid #3c3c3c;
                    border-radius: 4px;
                    padding: 5px;
                    color: #e0e0e0;
                }
                QComboBox {
                    background-color: #2d2d2d;
                    border: 1px solid #3c3c3c;
                    border-radius: 4px;
                    padding: 5px;
                    color: #e0e0e0;
                }
                QComboBox::drop-down {
                    border: none;
                }
                QComboBox QAbstractItemView {
                    background-color: #2d2d2d;
                    color: #e0e0e0;
                    selection-background-color: #0078d4;
                }
                QCheckBox {
                    color: #e0e0e0;
                }
                QPushButton {
                    background-color: #0078d4;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #106ebe;
                }
                QPushButton:pressed {
                    background-color: #005a9e;
                }
            """
        else:
            return """
                QScrollArea {
                    border: none;
                }
                QScrollBar:vertical {
                    background-color: #f0f0f0;
                    width: 12px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical {
                    background-color: #c0c0c0;
                    border-radius: 6px;
                    min-height: 20px;
                }
                QScrollBar::handle:vertical:hover {
                    background-color: #a0a0a0;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
            """
            
    @staticmethod
    def get_label_color(theme='light', color_type='normal'):
        """获取标签颜色"""
        if theme == 'dark':
            colors = {
                'normal': '#e0e0e0',
                'subtitle': '#b0b0b0',
                'status': '#4a9eff',
                'count': '#b0b0b0',
                'tip': '#888888'
            }
        else:
            colors = {
                'normal': '#000000',
                'subtitle': '#666666',
                'status': '#0078d4',
                'count': '#666666',
                'tip': '#888888'
            }
        return colors.get(color_type, colors['normal'])
        
    @staticmethod
    def get_button_style(theme='light', button_type='primary'):
        """获取按钮样式"""
        if theme == 'dark':
            if button_type == 'primary':
                return """
                    QPushButton {
                        background-color: #0078d4;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }
                    QPushButton:hover { background-color: #106ebe; }
                    QPushButton:pressed { background-color: #005a9e; }
                """
            else:  # secondary
                return """
                    QPushButton {
                        background-color: #3c3c3c;
                        color: #e0e0e0;
                        border: none;
                        border-radius: 5px;
                    }
                    QPushButton:hover { background-color: #4c4c4c; }
                    QPushButton:pressed { background-color: #2c2c2c; }
                """
        else:
            if button_type == 'primary':
                return """
                    QPushButton {
                        background-color: #0078d4;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }
                    QPushButton:hover { background-color: #106ebe; }
                    QPushButton:pressed { background-color: #005a9e; }
                """
            else:  # secondary
                return """
                    QPushButton {
                        background-color: #5c5c5c;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }
                    QPushButton:hover { background-color: #6c6c6c; }
                    QPushButton:pressed { background-color: #4c4c4c; }
                """


# 全局主题管理器实例
theme_manager = ThemeManager()
