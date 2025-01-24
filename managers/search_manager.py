from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QCheckBox, QHBoxLayout
)
from PyQt6.QtGui import QIcon


class SearchAndReplaceManager(QDialog):
    def __init__(self, main_window, text_widget, search_manager_functions):
        super().__init__(main_window)
        self.main_window = main_window
        self.text_widget = text_widget
        self.search_manager_functions = search_manager_functions

        self.setWindowTitle("Поиск и замена текста")
        self.setGeometry(950, 200, 600, 200)
        self.setWindowIcon(QIcon("img-icons/search.png"))

        self.search_layout = QVBoxLayout()
        self.replace_layout = QVBoxLayout()
        self.main_layout = QHBoxLayout(self)

        self.search_layout.addWidget(QLabel("Текст для поиска:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите текст для поиска")
        self.search_layout.addWidget(self.search_input)

        self.replace_layout.addWidget(QLabel("Текст для замены:"))
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Введите текст для замены")
        self.replace_layout.addWidget(self.replace_input)

        self.search_button = QPushButton("Поиск")
        self.search_button.clicked.connect(lambda: self.search_manager_functions.search(self.text_widget, self.search_input.text(), self.regex_checkbox.isChecked()))
        self.search_layout.addWidget(self.search_button)
        
        self.search_next_button = QPushButton("Следующее совпадение")
        self.search_next_button.clicked.connect(lambda: self.search_manager_functions.search_next(self.text_widget))
        self.search_layout.addWidget(self.search_next_button)

        self.search_prev_button = QPushButton("Предыдущее совпадение")
        self.search_prev_button.clicked.connect(lambda: self.search_manager_functions.search_prev(self.text_widget))
        self.search_layout.addWidget(self.search_prev_button)
        
        self.replace_current_button = QPushButton("Заменить текущее совпадение")
        self.replace_current_button.clicked.connect(lambda: self.search_manager_functions.replace_current(self.text_widget, self.replace_input.text()))
        self.replace_layout.addWidget(self.replace_current_button)

        self.replace_all_button = QPushButton("Заменить все совпадения")
        self.replace_all_button.clicked.connect(lambda: self.search_manager_functions.replace_all(self.text_widget, self.replace_input.text()))
        self.replace_layout.addWidget(self.replace_all_button)

        self.regex_checkbox = QCheckBox("Регулярные выражения")
        self.replace_layout.addWidget(self.regex_checkbox)

        self.replace_layout.addStretch()
        self.search_layout.addStretch()

        self.main_layout.addLayout(self.search_layout, 1)
        self.main_layout.addLayout(self.replace_layout, 1)




    

        

        




