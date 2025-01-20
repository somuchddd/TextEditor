from PyQt6.QtWidgets import (
    QMainWindow, QTabWidget
)
from PyQt6.QtGui import QIcon
from toolbar_manager import ToolbarManager
from menu_manager import MenuManager
from style_manager import StyleManager
from search_manager import SearchAndReplaceManager


class TextEditorGUI(QMainWindow):
    def __init__(self, format_functions, page_functions, style_manager_functions):
        super().__init__()
        self.setWindowTitle("Текстовый процессор")
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowIcon(QIcon("img-icons/text_editor.png"))

        self.text_widget = QTabWidget(self)
        self.setCentralWidget(self.text_widget)

        self.style_manager = StyleManager(self, self.text_widget, style_manager_functions)

        self.search_manager = SearchAndReplaceManager(self)

        self.menubar_manager = MenuManager(self, format_functions, page_functions, self.text_widget)
        self.menubar_manager.create_menubar()

        self.toolbar_manager = ToolbarManager(self, page_functions)
        self.toolbar_manager.create_toolbar()

        page_functions.add_page(self.text_widget)

    def open_style_manager(self):
        self.style_manager.show()

    def open_search_manager(self):
        self.search_manager.show()
    
    