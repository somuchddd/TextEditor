from PyQt6.QtWidgets import (
    QTextEdit, QMessageBox
)

class FunctionsWithPages():
    def __init__(self):
        self.numbering = False
        
    def add_page(self, text_widget):
        if self.numbering == True:
            page_title = f"Страница {text_widget.count() + 1}"
        else:
            page_title = "Страница"
        text_widget.addTab(QTextEdit(), page_title)
    
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