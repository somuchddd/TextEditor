from PyQt6.QtWidgets import (
    QTextEdit, QMessageBox
)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QTextCursor, QDesktopServices


class FunctionsWithPages():
    def __init__(self):
        self.numbering = False

    def create_new_file(self, text_widget):
        text_widget.clear()
        self.add_page(text_widget)
        
    def add_page(self, text_widget):
        text_field = QTextEdit()
        text_field.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction | Qt.TextInteractionFlag.TextEditable)
        original_mouse_press_event = text_field.mousePressEvent
        text_field.mousePressEvent = lambda event: self.text_field_mouse_press_event(event, text_field, original_mouse_press_event)
        if self.numbering == True:
            page_title = f"Страница {text_widget.count() + 1}"
        else:
            page_title = "Страница"
        text_widget.addTab(text_field, page_title)
    
    def update_titles(self, text_widget):
        for i in range(text_widget.count()):
            if self.numbering == True:
                title = f"Страница {i + 1}"
            else: 
                title = f"Страница"
            text_widget.setTabText(i, title)
            
    def toggle_numbering(self, text_widget):
        self.numbering = not self.numbering
        self.update_titles(text_widget)

    def delete_page(self, text_widget):
        current_index = text_widget.currentIndex()
        if current_index != -1:
            text_widget.removeTab(current_index)
        else:
            QMessageBox.warning(None, "Ошибка", "Нет открытых страниц для удаления.")
        self.update_titles(text_widget)

    def text_field_mouse_press_event(self, event, text_field, original_mouse_press_event):
        cursor = text_field.cursorForPosition(event.pos())
        cursor.select(QTextCursor.SelectionType.WordUnderCursor)
        char_format = cursor.charFormat()
        if char_format.isAnchor():  
            url = char_format.anchorHref()
            if url:
                QDesktopServices.openUrl(QUrl(url))
                return
        original_mouse_press_event(event)