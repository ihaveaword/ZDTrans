"""
主题管理模块
提供日间/夜间模式切换功能
"""

from PySide6.QtCore import QObject, Signal
from .themes import get_colors


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
        c = get_colors(theme)
        return f"""
            QMainWindow {{
                background-color: {c['bg_main']};
            }}
            QGroupBox {{
                font-family: 'PingFang SC';
                font-size: 13px;
                font-weight: bold;
                border: 2px solid {c['border_group']};
                border-radius: 6px;
                margin-top: 10px;
                padding: 15px 10px 10px 10px;
                background-color: {c['bg_group']};
                color: {c['text_normal']};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: {c['text_normal']};
            }}
            QLabel {{
                color: {c['text_normal']};
            }}
            QTextEdit {{
                background-color: {c['bg_widget']};
                border: 1px solid {c['border']};
                border-radius: 4px;
                color: {c['text_normal']};
            }}
            QStatusBar {{
                background-color: {c['bg_widget']};
                color: {c['text_normal']};
            }}
        """
            
    @staticmethod
    def get_popup_style(theme='light'):
        """获取弹出窗口样式"""
        c = get_colors(theme)
        return f"""
            QWidget {{
                background-color: {c['bg_popup']};
                border-radius: 10px;
                color: {c['text_popup']};
            }}
            QTextEdit {{
                background-color: rgba(60, 60, 60, 200);
                border: none;
                border-radius: 5px;
                padding: 10px;
                color: {c['text_popup']};
                font-size: 14px;
            }}
            QPushButton {{
                background-color: rgba(80, 80, 80, 200);
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                color: {c['text_popup']};
                font-size: 12px;
            }}
            QPushButton:hover {{
                background-color: rgba(100, 100, 100, 200);
            }}
            QLabel {{
                color: rgba(255, 255, 255, 180);
                font-size: 12px;
            }}
        """
            
    @staticmethod
    def get_settings_style(theme='light'):
        """获取设置对话框样式"""
        c = get_colors(theme)
        return f"""
            QDialog {{
                background-color: {c['bg_main']};
            }}
            QScrollArea {{
                border: none;
                background-color: {c['bg_main']};
            }}
            QScrollBar:vertical {{
                background-color: {c['bg_scrollbar']};
                width: 12px;
                border-radius: 6px;
            }}
            QScrollBar::handle:vertical {{
                background-color: {c['bg_scrollbar_handle']};
                border-radius: 6px;
                min-height: 20px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: {c['hover_scrollbar']};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
            QGroupBox {{
                font-weight: bold;
                border: 2px solid {c['border_group']};
                border-radius: 6px;
                margin-top: 10px;
                padding: 15px 10px 10px 10px;
                background-color: {c['bg_group']};
                color: {c['text_normal']};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: {c['text_normal']};
            }}
            QLabel {{
                color: {c['text_normal']};
            }}
            QLineEdit, QTextEdit {{
                background-color: {c['bg_input']};
                border: 1px solid {c['border']};
                border-radius: 4px;
                padding: 5px;
                color: {c['text_normal']};
            }}
            QComboBox {{
                background-color: {c['bg_input']};
                border: 1px solid {c['border']};
                border-radius: 4px;
                padding: 5px;
                color: {c['text_normal']};
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                background-color: {c['bg_input']};
                color: {c['text_normal']};
                selection-background-color: {c['bg_button_primary']};
                selection-color: {c['text_button']};
            }}
            QCheckBox {{
                color: {c['text_normal']};
            }}
            QPushButton {{
                background-color: {c['bg_button_primary']};
                color: {c['text_button']};
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {c['hover_button_primary']};
            }}
            QPushButton:pressed {{
                background-color: {c['pressed_button_primary']};
            }}
        """
            
    @staticmethod
    def get_label_color(theme='light', color_type='normal'):
        """获取标签颜色"""
        c = get_colors(theme)
        color_map = {
            'normal': c['text_normal'],
            'subtitle': c['text_subtitle'],
            'status': c['text_status'],
            'count': c['text_count'],
            'tip': c['text_tip']
        }
        return color_map.get(color_type, c['text_normal'])
        
    @staticmethod
    def get_button_style(theme='light', button_type='primary'):
        """获取按钮样式"""
        c = get_colors(theme)
        
        if button_type == 'primary':
            return f"""
                QPushButton {{
                    background-color: {c['bg_button_primary']};
                    color: {c['text_button']};
                    border: none;
                    border-radius: 5px;
                }}
                QPushButton:hover {{ background-color: {c['hover_button_primary']}; }}
                QPushButton:pressed {{ background-color: {c['pressed_button_primary']}; }}
            """
        else:  # secondary
            return f"""
                QPushButton {{
                    background-color: {c['bg_button_secondary']};
                    color: {c['text_button']};
                    border: none;
                    border-radius: 5px;
                }}
                QPushButton:hover {{ background-color: {c['hover_button_secondary']}; }}
                QPushButton:pressed {{ background-color: {c['pressed_button_secondary']}; }}
            """


# 全局主题管理器实例
theme_manager = ThemeManager()
