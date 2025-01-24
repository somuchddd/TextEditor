from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QSize


class MenuManager():
    def __init__(self, main_window, format_functions, page_functions, text_widget):
        self.main_window = main_window
        self.format_functions = format_functions
        self.page_functions = page_functions
        self.text_widget = text_widget
    
    def create_menubar(self):
        main_menu = self.main_window.menuBar()

        file_menu = main_menu.addMenu("Файл")
        new_file_action = QAction(QIcon("img-icons/new_file.png"), "Новый", self.main_window)
        new_file_action.triggered.connect(lambda: self.page_functions.create_new_file(self.main_window.text_widget))
        file_menu.addAction(new_file_action)

        save_file_action = QAction(QIcon("img-icons/save_file.png"), "Сохранить", self.main_window)
        file_menu.addAction(save_file_action)

        open_file_action = QAction(QIcon("img-icons/open_file.png"), "Открыть", self.main_window)
        file_menu.addAction(open_file_action)

        insert_menu = main_menu.addMenu("Вставка")

        image_insert_action = QAction(QIcon("img-icons/image.png"), "Изображение", self.main_window)
        image_insert_action.triggered.connect(lambda: self.format_functions.insert_image(self.main_window.text_widget.currentWidget(), QSize(400, 250)))
        insert_menu.addAction(image_insert_action)

        hyperlink_insert_action = QAction(QIcon("img-icons/hyperlink.png"), "Гиперссылка", self.main_window)
        hyperlink_insert_action.triggered.connect(lambda: self.format_functions.insert_hyperlink(self.main_window.text_widget.currentWidget()))
        insert_menu.addAction(hyperlink_insert_action)

        format_menu = main_menu.addMenu("Формат")

        bold_action = QAction(QIcon("img-icons/bold.png"), "Полужирный", self.main_window)
        bold_action.triggered.connect(lambda: self.format_functions.toggle_bold(self.text_widget))
        format_menu.addAction(bold_action)
        
        italic_action = QAction(QIcon("img-icons/italic.png") ,"Курсив", self.main_window)
        italic_action.triggered.connect(lambda: self.format_functions.toggle_italic(self.text_widget))
        format_menu.addAction(italic_action)
        
        underline_action = QAction(QIcon("img-icons/underline.png"), "Подчёркнутый", self.main_window)
        underline_action.triggered.connect(lambda: self.format_functions.toggle_underline(self.text_widget))
        format_menu.addAction(underline_action)

        format_menu.addSeparator()

        font_action = QAction(QIcon("img-icons/font.png"), "Шрифт", self.main_window)
        font_action.triggered.connect(lambda: self.format_functions.change_font(self.text_widget))
        format_menu.addAction(font_action)
        
        color_action = QAction(QIcon("img-icons/text_color.png"), "Цвет", self.main_window)
        color_action.triggered.connect(lambda: self.format_functions.change_text_color(self.text_widget))
        format_menu.addAction(color_action)

        format_menu.addSeparator()

        full_document_action = QAction("Применять стили форматирования ко всему документу", self.main_window, checkable=True)
        full_document_action.setChecked(False)
        full_document_action.triggered.connect(lambda: self.format_functions.toggle_full_document_format())
        format_menu.addAction(full_document_action)

        clear_format_action = QAction("Сбросить форматирование", self.main_window)
        clear_format_action.triggered.connect(lambda: self.format_functions.clear_format(self.text_widget))
        format_menu.addAction(clear_format_action)

        styles_action = QAction("Пользовательские стили", self.main_window)
        styles_action.triggered.connect(self.main_window.open_style_manager)
        main_menu.addAction(styles_action)

        search_action = QAction("Поиск и замена", self.main_window)
        search_action.triggered.connect(self.main_window.open_search_manager)
        main_menu.addAction(search_action)

        interval_action = QAction("Интервалы и отступы", self.main_window)
        interval_action.triggered.connect(self.main_window.open_interval_manager)
        main_menu.addAction(interval_action)
