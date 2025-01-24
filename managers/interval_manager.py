from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
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

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Введите межстрочный интервал:")
        self.layout.addWidget(self.label)

        self.interval_input = QLineEdit()
        self.interval_input.setValidator(QIntValidator(self))
        self.layout.addWidget(self.interval_input)
        
        self.interval_apply_button = QPushButton("Применить межстрочные интервалы")
        self.interval_apply_button.clicked.connect(lambda: self.interval_manager_functions.apply_interval(self.text_widget, self.interval_input.text()))
        self.layout.addWidget(self.interval_apply_button)

        self.interval_reset_button = QPushButton("Сбросить межстрочные интервалы")
        self.interval_reset_button.clicked.connect(lambda: self.interval_manager_functions.reset_interval(self.text_widget))
        self.layout.addWidget(self.interval_reset_button)

        self.layout.addStretch()

class IntervalManagerFunctions():
    def apply_interval(self, text_widget, interval):
        text_field = text_widget.currentWidget()

        block_format = QTextBlockFormat()
        block_format.setLineHeight(int(interval), QTextBlockFormat.LineHeightTypes.ProportionalHeight.value)

        cursor = text_field.textCursor()
        cursor.clearSelection()
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.mergeBlockFormat(block_format)

    def reset_interval(self, text_widget):
        self.apply_interval(text_widget, 100)
