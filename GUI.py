from PyQt6.QtWidgets import (
    QMainWindow, QTabWidget
)
from toolbar_manager import ToolbarManager
from menu_manager import MenuManager
from style_manager import StyleManager

class TextEditorGUI(QMainWindow):
    def __init__(self, format_functions, page_functions, style_manager_functions):
        super().__init__()
        self.setWindowTitle("Текстовый процессор")
        self.setGeometry(100, 100, 1280, 720)

        self.text_widget = QTabWidget(self)
        self.setCentralWidget(self.text_widget)

        self.style_manager = StyleManager(self, self.text_widget, style_manager_functions)

        self.menubar_manager = MenuManager(self, format_functions, self.text_widget)
        self.menubar_manager.create_menubar()

        self.toolbar_manager = ToolbarManager(self, page_functions)
        self.toolbar_manager.create_toolbar()

        page_functions.add_page(self.text_widget)

    def open_style_manager(self):
        self.style_manager.show()