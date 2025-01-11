from PyQt6.QtWidgets import QMainWindow, QTextEdit
from PyQt6.QtGui import QAction
from functions import TextEditorFunctions

class TextEditorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовый процессор")
        self.setGeometry(100, 100, 1280, 720)

        self.text_field=QTextEdit(self)
        self.setCentralWidget(self.text_field)

        self.functions = TextEditorFunctions()
    
        self.create_toolbar()

    def create_toolbar(self):
        main_menu = self.menuBar()

        #ФАЙЛ
        file_menu = main_menu.addMenu("Файл")

        new_action = QAction("Новый", self)
        new_action.triggered.connect(self.new_action)
        file_menu.addAction(new_action)

        save_action = QAction("Сохранить", self)
        file_menu.addAction(save_action)

        open_action = QAction("Открыть", self)
        file_menu.addAction(open_action)

        #ВСТАВКА
        insert_menu = main_menu.addMenu("Вставка")

        image_action = QAction("Изображение", self)
        insert_menu.addAction(image_action)

        hyperlink_action = QAction("Гиперссылка", self)
        insert_menu.addAction(hyperlink_action)

        #ФОРМАТ
        format_menu = main_menu.addMenu("Формат")

        bold_action = QAction("Полужирный", self)
        bold_action.triggered.connect(self.toggle_bold)
        format_menu.addAction(bold_action)
        
        italic_action = QAction("Курсив", self)
        italic_action.triggered.connect(self.toggle_italic)
        format_menu.addAction(italic_action)
        
        underline_action = QAction("Подчёркнутый", self)
        underline_action.triggered.connect(self.toggle_underline)
        format_menu.addAction(underline_action)

        font_action = QAction("Шрифт", self)
        font_action.triggered.connect(self.change_font)
        format_menu.addAction(font_action)
        
        color_action = QAction("Цвет", self)
        color_action.triggered.connect(self.change_text_color)
        format_menu.addAction(color_action)

        #ПОЛЬЗОВАТЕЛЬСКИЕ СТИЛИ
        styles = QAction("Пользовательские стили", self)
        main_menu.addAction(styles)

    def new_action(self):
            self.functions.new_action(self.text_field)
            
    def toggle_bold(self):
            self.functions.toggle_bold(self.text_field)

    def toggle_italic(self):
            self.functions.toggle_italic(self.text_field)

    def toggle_underline(self):
            self.functions.toggle_underline(self.text_field)

    def change_font(self):
            self.functions.change_font(self.text_field)

    def change_text_color(self):
            self.functions.change_text_color(self.text_field)

