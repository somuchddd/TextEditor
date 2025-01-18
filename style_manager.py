from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QLabel, QComboBox
)

class StyleManager(QDialog):
    def __init__(self, style_manager_functions):
        super().__init__()
        self.style_manager_functions = style_manager_functions

        self.setWindowTitle("Пользовательские стили")
        self.setGeometry(700, 200, 300, 200)

        self.layout = QVBoxLayout(self)

        self.create_style_button = QPushButton("Создать стиль")
        #self.create_style_button.clicked.connect()
        self.layout.addWidget(self.create_style_button)

        self.apply_style_button = QPushButton("Применить стиль")
        #self.apply_style_button.clicked.connect()
        self.layout.addWidget(self.apply_style_button)

        self.label = QLabel("Выбрать стиль:")
        self.layout.addWidget(self.label)

        self.styles_list = QComboBox()
        self.layout.addWidget(self.styles_list)

class StyleManagerFunctions():
    def __init__(self):
        pass


