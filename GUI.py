from PyQt6.QtWidgets import QMainWindow, QTextEdit
from PyQt6.QtGui import QAction

class TextEditorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовый процессор")
        self.setGeometry(100, 100, 1280, 720)

        self.text_field=QTextEdit(self)
        self.setCentralWidget(self.text_field)

        self.create_toolbar()

    def create_toolbar(self):
        main_menu = self.menuBar()

        #ФАЙЛ
        file_menu = main_menu.addMenu("Файл")

        new_action = QAction("Новый", self)
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
        format_menu.addAction(bold_action)

        italic_action = QAction("Курсив", self)
        format_menu.addAction(italic_action)

        underline_action = QAction("Подчёркнутый", self)
        format_menu.addAction(underline_action)

        font_action = QAction("Шрифт", self)
        format_menu.addAction(font_action)

        color_action = QAction("Цвет", self)
        format_menu.addAction(color_action)

        styles = QAction("Пользовательские стили", self)
        main_menu.addAction(styles)



