from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QLabel, QComboBox, QInputDialog, QColorDialog, QFontDialog, QMessageBox
)
from PyQt6.QtGui import (
    QFont, QColor, QTextCharFormat, QIcon
)


class StyleManager(QDialog):
    def __init__(self, main_window, text_widget, style_manager_functions):
        super().__init__(main_window)
        self.main_window = main_window
        self.text_widget = text_widget
        self.style_manager_functions = style_manager_functions

        self.setWindowTitle("Пользовательские стили")
        self.setGeometry(600, 200, 300, 150)
        self.setWindowIcon(QIcon("img-icons/style_manager.png"))

        self.layout = QVBoxLayout(self)

        self.create_style_button = QPushButton("Создать стиль")
        self.create_style_button.clicked.connect(lambda: self.style_manager_functions.create_style(self, self.styles_list))
        self.layout.addWidget(self.create_style_button)

        self.apply_style_button = QPushButton("Применить стиль")
        self.apply_style_button.clicked.connect(lambda: self.style_manager_functions.apply_style_to_text(self.text_widget, self.styles_list))
        self.layout.addWidget(self.apply_style_button)

        self.label = QLabel("Выбрать стиль:")
        self.layout.addWidget(self.label)

        self.styles_list = QComboBox()
        self.layout.addWidget(self.styles_list)


class StyleManagerFunctions():
    def __init__(self):
        self.styles = []

    def create_style(self, dialog, styles_list):
        name, ok = QInputDialog.getText(dialog, "Название стиля", "Введите название стиля")
        if ok and name:
            font, ok = QFontDialog.getFont()
            if ok:
                color = QColorDialog.getColor()
                if color.isValid():
                    style = [name, font.family(), font.pointSize(), color.name()]
                    self.styles.append(style)
                    styles_list.addItem(self.styles[-1][0])

    def apply_style_to_text(self, text_widget, styles_list):
        current_index = styles_list.currentIndex()
        if current_index >= 0:
            style = self.styles[current_index]
            font = QFont(style[1], style[2])
            color = QColor(style[3])
            cursor = text_widget.currentWidget().textCursor()
            format = QTextCharFormat()
            format.setFont(font)
            format.setForeground(color)
            cursor.mergeCharFormat(format)
            text_widget.currentWidget().setTextCursor(cursor)
        else: 
            QMessageBox.warning(None, "Ошибка", "Стиль не выбран")

    


