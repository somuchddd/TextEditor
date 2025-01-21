from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
)
from PyQt6.QtGui import QIcon


class SearchAndReplaceManager(QDialog):
    def __init__(self, main_window, text_widget, search_manager_functions):
        super().__init__(main_window)
        self.main_window = main_window
        self.text_widget = text_widget
        self.search_manager_functions = search_manager_functions

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
        self.search_next_button.clicked.connect(lambda: self.search_manager_functions.search_next(self.text_widget, self.search_input.text()))
        self.layout.addWidget(self.search_next_button)

        self.search_prev_button = QPushButton("Предыдущее совпадение")
        self.search_prev_button.clicked.connect(lambda: self.search_manager_functions.search_prev(self.text_widget, self.search_input.text()))
        self.layout.addWidget(self.search_prev_button)

        self.layout.addWidget(QLabel("После смены текста в поле поиска нажимаем сюда:"))
        self.clear_matches_button = QPushButton("Очистить список совпадений")
        self.clear_matches_button.clicked.connect(lambda: self.search_manager_functions.clear_matches())
        self.layout.addWidget(self.clear_matches_button)
        
        self.replace_current_button = QPushButton("Заменить текущее совпадение")
        self.replace_current_button.clicked.connect(lambda: self.search_manager_functions.replace_current(self.text_widget, self.search_input.text(), self.replace_input.text()))
        self.layout.addWidget(self.replace_current_button)

        self.replace_all_button = QPushButton("Заменить все совпадения")
        self.replace_all_button.clicked.connect(lambda: self.search_manager_functions.replace_all(self.text_widget, self.search_input.text(), self.replace_input.text()))
        self.layout.addWidget(self.replace_all_button)




    

        

        




