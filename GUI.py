from PyQt6.QtWidgets import (
    QMainWindow, QTextEdit, QTabWidget, QToolBar
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from functions import TextEditorFunctions

class TextEditorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовый процессор")
        self.setGeometry(100, 100, 1280, 720)

        self.text_widget = QTabWidget(self)
        self.setCentralWidget(self.text_widget)

        self.functions = TextEditorFunctions()
    
        self.create_menubar()
        self.create_toolbar()

        self.functions.add_page(self.text_widget)

    def create_menubar(self):
        main_menu = self.menuBar()

        file_menu = main_menu.addMenu("Файл")

        new_action = QAction("Новый", self)
        file_menu.addAction(new_action)

        save_action = QAction("Сохранить", self)
        file_menu.addAction(save_action)

        open_action = QAction("Открыть", self)
        file_menu.addAction(open_action)

        insert_menu = main_menu.addMenu("Вставка")

        image_action = QAction("Изображение", self)
        insert_menu.addAction(image_action)

        hyperlink_action = QAction("Гиперссылка", self)
        insert_menu.addAction(hyperlink_action)

        format_menu = main_menu.addMenu("Формат")

        bold_action = QAction("Полужирный", self)
        bold_action.triggered.connect(lambda: self.functions.toggle_bold(self.text_widget.currentWidget()))
        format_menu.addAction(bold_action)
        
        italic_action = QAction("Курсив", self)
        italic_action.triggered.connect(lambda: self.functions.toggle_italic(self.text_widget.currentWidget()))
        format_menu.addAction(italic_action)
        
        underline_action = QAction("Подчёркнутый", self)
        underline_action.triggered.connect(lambda: self.functions.toggle_underline(self.text_widget.currentWidget()))
        format_menu.addAction(underline_action)

        font_action = QAction("Шрифт", self)
        font_action.triggered.connect(lambda: self.functions.change_font(self.text_widget.currentWidget()))
        format_menu.addAction(font_action)
        
        color_action = QAction("Цвет", self)
        color_action.triggered.connect(lambda: self.functions.change_text_color(self.text_widget.currentWidget()))
        format_menu.addAction(color_action)

        styles = QAction("Пользовательские стили", self)
        main_menu.addAction(styles)
    
    def create_toolbar(self):
           toolbar = QToolBar(self)
           toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)
           self.addToolBar(toolbar)

           toolbar.setFixedHeight(35)

           add_action = QAction("Создать страницу", self)
           add_action.triggered.connect(lambda: self.functions.add_page(self.text_widget))
           toolbar.addAction(add_action)

           delete_action = QAction("Удалить текущую страницу", self)
           delete_action.triggered.connect(lambda: self.functions.delete_page(self.text_widget))
           toolbar.addAction(delete_action)

           numbering_action = QAction("Включить/отключить нумерацию ", self)
           numbering_action.triggered.connect(lambda: self.functions.toggle_numbering(self.text_widget))
           toolbar.addAction(numbering_action)




