"""
设置界面模块
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                               QLineEdit, QPushButton, QComboBox, QGroupBox,
                               QFormLayout, QMessageBox, QCheckBox, QTextEdit,
                               QScrollArea, QWidget)
from PySide6.QtCore import Qt, Signal
import json
from .theme import theme_manager


class SettingsDialog(QDialog):
    """设置对话框"""
    
    # 信号定义
    settings_saved = Signal(dict)
    
    def __init__(self, current_config, parent=None):
        super().__init__(parent)
        self.current_config = current_config
        self.init_ui()
        self.load_config()
        
        # 连接主题变化信号
        theme_manager.theme_changed.connect(self.apply_theme)
        # 应用初始主题
        self.apply_theme(theme_manager.get_theme())
        
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("ZDTrans - 设置")
        self.setModal(True)
        self.setMinimumWidth(500)
        self.setMinimumHeight(600)
        self.setMaximumHeight(800)
        
        # 主布局
        main_layout = QVBoxLayout()
        
        # 创建滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 创建内容容器
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # API设置组
        api_group = QGroupBox("API 配置")
        api_layout = QFormLayout()
        
        self.provider_combo = QComboBox()
        self.provider_combo.addItems(["OpenAI", "火山方舟(豆包)", "DeepL", "Claude"])
        self.provider_combo.currentTextChanged.connect(self._on_provider_changed)
        api_layout.addRow("API 提供商:", self.provider_combo)
        
        self.api_key_edit = QLineEdit()
        self.api_key_edit.setEchoMode(QLineEdit.Password)
        self.api_key_edit.setPlaceholderText("输入你的 API Key")
        api_layout.addRow("API Key:", self.api_key_edit)
        
        self.base_url_edit = QLineEdit()
        self.base_url_edit.setPlaceholderText("https://api.openai.com/v1")
        api_layout.addRow("Base URL:", self.base_url_edit)
        
        self.model_edit = QLineEdit()
        self.model_edit.setPlaceholderText("如: doubao-pro-32k 或 doubao-1-5-lite-32k-250115")
        api_layout.addRow("Model:", self.model_edit)
        
        api_group.setLayout(api_layout)
        layout.addWidget(api_group)
        
        # 翻译设置组
        trans_group = QGroupBox("翻译配置")
        trans_layout = QFormLayout()
        
        # 学科领域选择
        domain_layout = QHBoxLayout()
        self.domain_combo = QComboBox()
        self.domain_combo.setEditable(True)  # 允许编辑
        self.domain_combo.addItems([
            "通用", "计算机科学", "医学", "生物学", 
            "物理学", "化学", "数学", "工程学", "经济学"
        ])
        self.domain_combo.setToolTip("可直接输入自定义学科领域")
        domain_layout.addWidget(self.domain_combo)
        
        # 添加"+"按钮用于保存自定义领域
        add_domain_btn = QPushButton("+")
        add_domain_btn.setFixedSize(30, 30)
        add_domain_btn.setToolTip("将自定义领域添加到列表")
        add_domain_btn.clicked.connect(self._add_custom_domain)
        domain_layout.addWidget(add_domain_btn)
        self.add_domain_button = add_domain_btn
        
        trans_layout.addRow("学科领域:", domain_layout)
        
        self.custom_context_edit = QTextEdit()
        self.custom_context_edit.setPlaceholderText("例如：这是深度学习方向的论文，重点关注神经网络架构")
        self.custom_context_edit.setMaximumHeight(60)
        trans_layout.addRow("自定义说明:", self.custom_context_edit)
        
        # 添加关键词输入
        self.keywords_edit = QLineEdit()
        self.keywords_edit.setPlaceholderText("例如：机器学习, 神经网络, 深度学习（用逗号分隔）")
        self.keywords_edit.setToolTip("输入专业领域的关键词，帮助AI更准确地翻译术语")
        trans_layout.addRow("关键词:", self.keywords_edit)
        
        self.academic_mode_check = QCheckBox("学术模式")
        self.academic_mode_check.setToolTip("开启后将使用学术论文专用的翻译风格")
        trans_layout.addRow("", self.academic_mode_check)
        
        self.preserve_terms_check = QCheckBox("保留术语原文")
        self.preserve_terms_check.setToolTip("专业术语首次出现时会标注英文原文")
        trans_layout.addRow("", self.preserve_terms_check)
        
        trans_group.setLayout(trans_layout)
        layout.addWidget(trans_group)
        
        # 快捷键设置组
        hotkey_group = QGroupBox("快捷键配置")
        hotkey_layout = QFormLayout()
        
        self.translate_hotkey_edit = QLineEdit()
        self.translate_hotkey_edit.setPlaceholderText("例如: Ctrl+Q")
        self.translate_hotkey_edit.setReadOnly(True)
        hotkey_layout.addRow("翻译快捷键:", self.translate_hotkey_edit)
        
        self.polish_hotkey_edit = QLineEdit()
        self.polish_hotkey_edit.setPlaceholderText("例如: Ctrl+Shift+Q")
        self.polish_hotkey_edit.setReadOnly(True)
        hotkey_layout.addRow("润色快捷键:", self.polish_hotkey_edit)
        
        hotkey_note = QLabel("💡 提示: 快捷键可在 config.json 中修改")
        hotkey_note.setStyleSheet("color: #666; font-size: 10px;")
        hotkey_layout.addRow("", hotkey_note)
        
        hotkey_group.setLayout(hotkey_layout)
        layout.addWidget(hotkey_group)
        
        # UI设置组
        ui_group = QGroupBox("界面配置")
        ui_layout = QFormLayout()
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["日间模式", "夜间模式"])
        self.theme_combo.currentTextChanged.connect(self._on_theme_changed)
        ui_layout.addRow("主题:", self.theme_combo)
        
        ui_group.setLayout(ui_layout)
        layout.addWidget(ui_group)
        
        # 将内容容器设置到滚动区域
        scroll.setWidget(content_widget)
        
        # 将滚动区域添加到主布局
        main_layout.addWidget(scroll)
        
        # 按钮布局（固定在底部，不滚动）
        button_layout = QHBoxLayout()
        
        self.save_button = QPushButton("保存")
        self.save_button.clicked.connect(self.save_settings)
        button_layout.addWidget(self.save_button)
        
        self.cancel_button = QPushButton("取消")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)
        
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
        
    def load_config(self):
        """加载配置"""
        # API配置
        api_config = self.current_config.get('api', {})
        
        provider = api_config.get('provider', 'openai')
        if provider == 'openai':
            self.provider_combo.setCurrentText("OpenAI")
        elif provider == 'volcengine' or provider == 'doubao':
            self.provider_combo.setCurrentText("火山方舟(豆包)")
        elif provider == 'deepl':
            self.provider_combo.setCurrentText("DeepL")
        elif provider == 'claude':
            self.provider_combo.setCurrentText("Claude")
            
        self.api_key_edit.setText(api_config.get('api_key', ''))
        self.base_url_edit.setText(api_config.get('base_url', ''))
        self.model_edit.setText(api_config.get('model', ''))
        
        # 翻译配置
        trans_config = self.current_config.get('translation', {})
        domain = trans_config.get('domain', 'general')
        
        # 标准学科领域映射
        domain_map = {
            'general': '通用',
            'computer_science': '计算机科学',
            'medicine': '医学',
            'biology': '生物学',
            'physics': '物理学',
            'chemistry': '化学',
            'mathematics': '数学',
            'engineering': '工程学',
            'economics': '经济学'
        }
        
        # 加载自定义学科领域列表
        custom_domains = trans_config.get('custom_domains', [])
        for custom_domain in custom_domains:
            # 只添加不在默认列表中的领域
            if custom_domain not in domain_map.values():
                self.domain_combo.addItem(custom_domain)
        
        # 设置当前学科领域（支持自定义领域）
        if domain in domain_map:
            self.domain_combo.setCurrentText(domain_map[domain])
        else:
            # 直接使用域值（可能是自定义的）
            self.domain_combo.setCurrentText(domain)
        
        self.custom_context_edit.setPlainText(trans_config.get('custom_context', ''))
        self.keywords_edit.setText(trans_config.get('keywords', ''))
        self.academic_mode_check.setChecked(trans_config.get('academic_mode', False))
        self.preserve_terms_check.setChecked(trans_config.get('preserve_terms', True))
        
        # 快捷键配置
        hotkey_config = self.current_config.get('hotkey', {})
        self.translate_hotkey_edit.setText(hotkey_config.get('translate', 'Ctrl+Q'))
        self.polish_hotkey_edit.setText(hotkey_config.get('polish', 'Ctrl+Shift+Q'))
        
        # UI配置
        ui_config = self.current_config.get('ui', {})
        theme = ui_config.get('theme', 'light')
        self.theme_combo.setCurrentText("夜间模式" if theme == 'dark' else "日间模式")
        
    def _add_custom_domain(self):
        """添加自定义学科领域到下拉列表"""
        current_text = self.domain_combo.currentText().strip()
        if not current_text:
            QMessageBox.warning(self, "提示", "请输入学科领域名称")
            return
        
        # 检查是否已存在
        for i in range(self.domain_combo.count()):
            if self.domain_combo.itemText(i) == current_text:
                QMessageBox.information(self, "提示", "该领域已存在于列表中")
                return
        
        # 添加到下拉列表
        self.domain_combo.addItem(current_text)
        self.domain_combo.setCurrentText(current_text)
        QMessageBox.information(self, "成功", f"已添加自定义领域：{current_text}")
    
    def _on_theme_changed(self, theme_text):
        """主题改变时立即应用"""
        theme = 'dark' if theme_text == "夜间模式" else 'light'
        theme_manager.set_theme(theme)
    
    def apply_theme(self, theme):
        """应用主题"""
        self.setStyleSheet(theme_manager.get_settings_style(theme))
    
    def _on_provider_changed(self, provider_text):
        """当提供商改变时更新默认值"""
        if provider_text == "OpenAI":
            self.base_url_edit.setPlaceholderText("https://api.openai.com/v1")
            self.model_edit.setPlaceholderText("gpt-3.5-turbo")
        elif provider_text == "火山方舟(豆包)":
            self.base_url_edit.setPlaceholderText("https://ark.cn-beijing.volces.com/api/v3")
            self.model_edit.setPlaceholderText("doubao-pro-32k")
        elif provider_text == "Claude":
            self.base_url_edit.setPlaceholderText("https://api.anthropic.com/v1")
            self.model_edit.setPlaceholderText("claude-3-sonnet-20240229")
    
    def save_settings(self):
        """保存设置"""
        # 验证API Key
        api_key = self.api_key_edit.text().strip()
        if not api_key:
            QMessageBox.warning(self, "警告", "请输入 API Key")
            return
        
        # 转换提供商名称
        provider_text = self.provider_combo.currentText()
        if provider_text == "OpenAI":
            provider = "openai"
        elif provider_text == "火山方舟(豆包)":
            provider = "volcengine"
        elif provider_text == "DeepL":
            provider = "deepl"
        elif provider_text == "Claude":
            provider = "claude"
        else:
            provider = provider_text.lower()
        
        # 获取 base_url，如果为空则使用占位符的值
        base_url = self.base_url_edit.text().strip()
        if not base_url:
            base_url = self.base_url_edit.placeholderText()
        
        # 获取 model，如果为空则使用占位符的值
        model = self.model_edit.text().strip()
        if not model:
            model = self.model_edit.placeholderText()
        
        # 转换领域名称（支持自定义）
        domain_text = self.domain_combo.currentText().strip()
        domain_map_reverse = {
            '通用': 'general',
            '计算机科学': 'computer_science',
            '医学': 'medicine',
            '生物学': 'biology',
            '物理学': 'physics',
            '化学': 'chemistry',
            '数学': 'mathematics',
            '工程学': 'engineering',
            '经济学': 'economics'
        }
        
        # 如果是标准领域，使用映射的key；否则直接使用输入的文本
        if domain_text in domain_map_reverse:
            domain = domain_map_reverse[domain_text]
        else:
            # 自定义领域，直接使用文本
            domain = domain_text
        
        # 收集所有自定义领域（不在标准列表中的）
        custom_domains = []
        for i in range(self.domain_combo.count()):
            item_text = self.domain_combo.itemText(i)
            if item_text not in domain_map_reverse:
                custom_domains.append(item_text)
            
        # 构建新配置
        new_config = {
            'api': {
                'provider': provider,
                'api_key': api_key,
                'base_url': base_url,
                'model': model
            },
            'translation': {
                'domain': domain,
                'custom_domains': custom_domains,  # 保存自定义领域列表
                'custom_context': self.custom_context_edit.toPlainText().strip(),
                'keywords': self.keywords_edit.text().strip(),
                'preserve_terms': self.preserve_terms_check.isChecked(),
                'academic_mode': self.academic_mode_check.isChecked()
            },
            'hotkey': {
                'translate': self.translate_hotkey_edit.text() or 'Ctrl+Q',
                'polish': self.polish_hotkey_edit.text() or 'Ctrl+Shift+Q'
            },
            'ui': {
                'theme': 'dark' if self.theme_combo.currentText() == "夜间模式" else 'light'
            },
            'general': self.current_config.get('general', {})
        }
        
        # 发送信号
        self.settings_saved.emit(new_config)
        
        # 显示成功消息
        QMessageBox.information(self, "成功", "设置已保存")
        
        # 关闭对话框
        self.accept()
