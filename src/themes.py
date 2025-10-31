"""
主题配色方案
集中管理所有主题的颜色定义
"""

# 主题配色字典
COLORS = {
    'light': {
        # 背景色
        'bg_main': '#f5f5f5',
        'bg_widget': '#ffffff',
        'bg_group': '#ffffff',
        'bg_input': '#ffffff',
        'bg_button_primary': '#0078d4',
        'bg_button_secondary': '#5c5c5c',
        'bg_scrollbar': '#f0f0f0',
        'bg_scrollbar_handle': '#c0c0c0',
        'bg_popup': 'rgba(40, 40, 40, 240)',
        
        # 文字色
        'text_normal': '#000000',
        'text_subtitle': '#666666',
        'text_status': '#0078d4',
        'text_count': '#666666',
        'text_tip': '#888888',
        'text_button': '#ffffff',
        'text_popup': '#ffffff',
        
        # 边框色
        'border': '#cccccc',
        'border_group': '#dddddd',
        
        # 悬停色
        'hover_button_primary': '#106ebe',
        'hover_button_secondary': '#6c6c6c',
        'hover_scrollbar': '#a0a0a0',
        
        # 按下色
        'pressed_button_primary': '#005a9e',
        'pressed_button_secondary': '#4c4c4c',
    },
    
    'dark': {
        # 背景色
        'bg_main': '#1e1e1e',
        'bg_widget': '#2d2d2d',
        'bg_group': '#2d2d2d',
        'bg_input': '#2d2d2d',
        'bg_button_primary': '#0078d4',
        'bg_button_secondary': '#3c3c3c',
        'bg_scrollbar': '#2d2d2d',
        'bg_scrollbar_handle': '#5c5c5c',
        'bg_popup': 'rgba(30, 30, 30, 240)',
        
        # 文字色
        'text_normal': '#e0e0e0',
        'text_subtitle': '#b0b0b0',
        'text_status': '#4a9eff',
        'text_count': '#b0b0b0',
        'text_tip': '#888888',
        'text_button': '#ffffff',
        'text_popup': '#e0e0e0',
        
        # 边框色
        'border': '#3c3c3c',
        'border_group': '#3c3c3c',
        
        # 悬停色
        'hover_button_primary': '#106ebe',
        'hover_button_secondary': '#4c4c4c',
        'hover_scrollbar': '#6c6c6c',
        
        # 按下色
        'pressed_button_primary': '#005a9e',
        'pressed_button_secondary': '#2c2c2c',
    }
}


def get_colors(theme='light'):
    """获取主题配色"""
    return COLORS.get(theme, COLORS['light'])
