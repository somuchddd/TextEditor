from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QCheckBox
from PyQt6.QtGui import QIcon, QIntValidator, QTextCursor, QTextBlockFormat

class IntervalManager(QDialog):
    def __init__(self, main_window, text_widget, interval_manager_functions):
        super().__init__(main_window)
        self.main_window = main_window
        self.text_widget = text_widget
        self.interval_manager_functions = interval_manager_functions

        self.setWindowTitle("Интервалы и отступы")
        self.setGeometry(600, 200, 300, 150)
        self.setWindowIcon(QIcon("img-icons/intervals.png"))

        self.interval_layout = QVBoxLayout()
        self.indent_layout = QVBoxLayout()
        self.main_layout = QHBoxLayout(self)

        self.label = QLabel("Введите межстрочный интервал:")
        self.interval_layout.addWidget(self.label)

        self.interval_input = QLineEdit()
        self.interval_input.setValidator(QIntValidator(self))
        self.interval_layout.addWidget(self.interval_input)
        
        self.interval_apply_button = QPushButton("Применить межстрочные интервалы")
        self.interval_apply_button.clicked.connect(lambda: self.interval_manager_functions.apply_interval(self.text_widget, self.interval_input.text()))
        self.interval_layout.addWidget(self.interval_apply_button)

        self.interval_apply_full_doc = QPushButton("Применить интервалы ко всему документу")
        self.interval_apply_full_doc.clicked.connect(lambda: self.interval_manager_functions.apply_interval_to_full_doc(self.text_widget, self.interval_input.text()))
        self.interval_layout.addWidget(self.interval_apply_full_doc)

        self.interval_reset_button = QPushButton("Сбросить межстрочные интервалы")
        self.interval_reset_button.clicked.connect(lambda: self.interval_manager_functions.reset_interval(self.text_widget))
        self.interval_layout.addWidget(self.interval_reset_button)

        self.top_indent_label = QLabel("Введите верхний отступ:")
        self.indent_layout.addWidget(self.top_indent_label)
        self.top_indent_input = QLineEdit()
        self.top_indent_input.setValidator(QIntValidator(self))
        self.indent_layout.addWidget(self.top_indent_input)

        self.bottom_indent_label = QLabel("Введите нижний отступ:")
        self.indent_layout.addWidget(self.bottom_indent_label)
        self.bottom_indent_input = QLineEdit()
        self.bottom_indent_input.setValidator(QIntValidator(self))
        self.indent_layout.addWidget(self.bottom_indent_input)

        self.right_indent_label = QLabel("Введите правый отступ:")
        self.indent_layout.addWidget(self.right_indent_label)
        self.right_indent_input = QLineEdit()
        self.right_indent_input.setValidator(QIntValidator(self))
        self.indent_layout.addWidget(self.right_indent_input)

        self.left_indent_label = QLabel("Введите левый отступ:")
        self.indent_layout.addWidget(self.left_indent_label)
        self.left_indent_input = QLineEdit()
        self.left_indent_input.setValidator(QIntValidator(self))
        self.indent_layout.addWidget(self.left_indent_input)

        self.indent_apply_button = QPushButton("Применить отступы:")
        self.indent_apply_button.clicked.connect(lambda: self.interval_manager_functions.apply_indents(self.text_widget, self.left_indent_input.text(), self.top_indent_input.text(), self.right_indent_input.text(), self.bottom_indent_input.text()))
        self.indent_layout.addWidget(self.indent_apply_button)

        self.indent_apply_button = QPushButton("Применить отступы ко всему документу:")
        self.indent_apply_button.clicked.connect(lambda: self.interval_manager_functions.apply_indents_to_full_doc(self.text_widget, self.left_indent_input.text(), self.top_indent_input.text(), self.right_indent_input.text(), self.bottom_indent_input.text()))
        self.indent_layout.addWidget(self.indent_apply_button)

        self.indent_reset_button = QPushButton("Сбросить отступы")
        self.indent_reset_button.clicked.connect(lambda: self.interval_manager_functions.reset_indents(self.text_widget))
        self.indent_layout.addWidget(self.indent_reset_button)
        
        self.indent_layout.addStretch()

        self.main_layout.addLayout(self.interval_layout, 1)
        self.main_layout.addLayout(self.indent_layout, 1)


class IntervalManagerFunctions():
    def apply_interval(self, text_widget, interval):
        try:
            text_field = text_widget.currentWidget()

            block_format = QTextBlockFormat()
            block_format.setLineHeight(int(interval), QTextBlockFormat.LineHeightTypes.FixedHeight.value)

            cursor = text_field.textCursor()
            cursor.beginEditBlock()

        # Перебираем все блоки, начиная со второго
            block = text_field.document().begin().next()
            while block.isValid():
                cursor.setPosition(block.position())
                cursor.setBlockFormat(block_format)
                block = block.next()

            # Завершаем редактирование
            cursor.endEditBlock()
        except:
            QMessageBox.warning(None, "Ошибка", "Введите межстрочный интервал")
    
    def apply_interval_to_full_doc(self, text_widget, interval):
        current_index = text_widget.currentIndex()
        for tab_index in range(text_widget.count()):
            text_widget.setCurrentIndex(tab_index)
            self.apply_interval(text_widget, interval)
            
        text_widget.setCurrentIndex(current_index)

    def reset_interval(self, text_widget):
        self.apply_interval(text_widget, 16)


    def apply_indents(self, text_widget, left_indent, top_indent, right_indent, bottom_indent):
        try:
            text_field = text_widget.currentWidget()
            page_indents = (int(left_indent), int(top_indent), int(right_indent), int(bottom_indent)) 
            text_field.setViewportMargins(*page_indents)
        except:
            QMessageBox.warning(None, "Ошибка", "Введите отступы со всех сторон")

    def apply_indents_to_full_doc(self, text_widget, left_indent, top_indent, right_indent, bottom_indent):
        current_index = text_widget.currentIndex()
        for tab_index in range(text_widget.count()):
            text_widget.setCurrentIndex(tab_index)
            self.apply_indents(text_widget, left_indent, top_indent, right_indent, bottom_indent)
        text_widget.setCurrentIndex(current_index)

    def reset_indents(self, text_widget):
        self.apply_indents(text_widget, 0, 0, 0, 0)

        
