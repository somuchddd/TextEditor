from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSize

class MenuManager():
    def __init__(self, main_window, format_functions, text_widget, style_manager):
        self.main_window = main_window
        self.format_functions = format_functions
        self.text_widget = text_widget
        self.style_manager = style_manager
    
    def create_menubar(self):
        main_menu = self.main_window.menuBar()

        file_menu = main_menu.addMenu("Файл")

        new_file_action = QAction("Новый", self.main_window)
        file_menu.addAction(new_file_action)

        save_file_action = QAction("Сохранить", self.main_window)
        file_menu.addAction(save_file_action)

        open_file_action = QAction("Открыть", self.main_window)
        file_menu.addAction(open_file_action)

        insert_menu = main_menu.addMenu("Вставка")

        image_insert_action = QAction("Изображение", self.main_window)
        image_insert_action.triggered.connect(lambda: self.format_functions.insert_image(self.main_window.text_widget.currentWidget(), QSize(400, 250)))
        insert_menu.addAction(image_insert_action)

        hyperlink_insert_action = QAction("Гиперссылка", self.main_window)
        hyperlink_insert_action.triggered.connect(lambda: self.format_functions.insert_hyperlink(self.main_window.text_widget.currentWidget()))
        insert_menu.addAction(hyperlink_insert_action)

        format_menu = main_menu.addMenu("Формат")

        bold_action = QAction("Полужирный", self.main_window)
        bold_action.triggered.connect(lambda: self.format_functions.toggle_bold(self.text_widget))
        format_menu.addAction(bold_action)
        
        italic_action = QAction("Курсив", self.main_window)
        italic_action.triggered.connect(lambda: self.format_functions.toggle_italic(self.text_widget))
        format_menu.addAction(italic_action)
        
        underline_action = QAction("Подчёркнутый", self.main_window)
        underline_action.triggered.connect(lambda: self.format_functions.toggle_underline(self.text_widget))
        format_menu.addAction(underline_action)

        font_action = QAction("Шрифт", self.main_window)
        font_action.triggered.connect(lambda: self.format_functions.change_font(self.text_widget))
        format_menu.addAction(font_action)
        
        color_action = QAction("Цвет", self.main_window)
        color_action.triggered.connect(lambda: self.format_functions.change_text_color(self.text_widget))
        format_menu.addAction(color_action)

        full_document_action = QAction("Применять стили форматирования ко всему документу", self.main_window, checkable=True)
        full_document_action.setChecked(False)
        full_document_action.triggered.connect(lambda: self.format_functions.toggle_full_document_format())
        format_menu.addAction(full_document_action)

        styles = QAction("Пользовательские стили", self.main_window)
        styles.triggered.connect(self.open_style_manager)
        main_menu.addAction(styles)

    def open_style_manager(self):
        self.style_manager.show()