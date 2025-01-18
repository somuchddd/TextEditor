from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

class ToolbarManager():
    def __init__(self, main_window, page_functions):
        self.main_window = main_window
        self.page_functions = page_functions
    
    def create_toolbar(self):
        toolbar = QToolBar(self.main_window)
        toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)
        self.main_window.addToolBar(toolbar)

        toolbar.setFixedHeight(35)

        add_action = QAction("Создать страницу", self.main_window)
        add_action.triggered.connect(lambda: self.page_functions.add_page(self.main_window.text_widget))
        toolbar.addAction(add_action)

        delete_action = QAction("Удалить текущую страницу", self.main_window)
        delete_action.triggered.connect(lambda: self.page_functions.delete_page(self.main_window.text_widget))
        toolbar.addAction(delete_action)

        numbering_action = QAction("Включить/отключить нумерацию ", self.main_window)
        numbering_action.triggered.connect(lambda: self.page_functions.toggle_numbering(self.main_window.text_widget))
        toolbar.addAction(numbering_action)