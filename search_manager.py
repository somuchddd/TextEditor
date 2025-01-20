from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
)
from PyQt6.QtGui import QIcon


class SearchAndReplaceManager(QDialog):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window

        self.setWindowTitle("Поиск и замена текста")
        self.setGeometry(1050, 200, 300, 200)
        self.setWindowIcon(QIcon("img-icons/search.png"))

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel("Текст для поиска:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите текст для поиска")
        self.layout.addWidget(self.search_input)

        self.layout.addWidget(QLabel("Текст для замены:"))
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Введите текст для замены")
        self.layout.addWidget(self.replace_input)

        self.search_next_button = QPushButton("Следующее совпадение")
        #self.search_next_button.clicked.connect()
        self.layout.addWidget(self.search_next_button)

        self.search_prev_button = QPushButton("Предыдущее совпадение")
        #self.search_prev_button.clicked.connect()
        self.layout.addWidget(self.search_prev_button)

        self.replace_current_button = QPushButton("Заменить текущее совпадение")
        #self.replace_current_button.clicked.connect()
        self.layout.addWidget(self.replace_current_button)

        self.replace_all_button = QPushButton("Заменить все совпадение")
        #self.replace_all_button.clicked.connect()
        self.layout.addWidget(self.replace_all_button)


class SearchManagerFunctions():
    def __init__():
        super().__init__()

        

        




