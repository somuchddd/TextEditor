from PyQt6.QtGui import QTextCharFormat, QFont, QColor
from PyQt6.QtWidgets import (
    QColorDialog, QFontDialog, QTextEdit, QMessageBox, QFileDialog, QInputDialog
)

class TextEditorFunctions:
    def __init__(self):
        self.numbering = False

    def toggle_bold(self, text_field):
        cursor = text_field.textCursor()  
        if cursor.hasSelection():  
            current_format = cursor.charFormat()
            char_format = QTextCharFormat()

            char_format.setFontWeight(QFont.Weight.Bold if current_format.fontWeight() != QFont.Weight.Bold else QFont.Weight.Normal)
            cursor.mergeCharFormat(char_format)
        else: 
            current_weight = text_field.fontWeight()
            text_field.setFontWeight(QFont.Weight.Bold if current_weight != QFont.Weight.Bold else QFont.Weight.Normal)
            
    def toggle_italic(self, text_field):
        cursor = text_field.textCursor()
        if cursor.hasSelection():
            current_format = cursor.charFormat()
            char_format = QTextCharFormat()

            char_format.setFontItalic(not current_format.fontItalic())
            cursor.mergeCharFormat(char_format)
        else:
            current_italic = text_field.fontItalic()
            text_field.setFontItalic(not current_italic)

    def toggle_underline(self, text_field):
        cursor = text_field.textCursor()
        if cursor.hasSelection():
            current_format = cursor.charFormat()
            char_format = QTextCharFormat()

            char_format.setFontUnderline(not current_format.fontUnderline())
            cursor.mergeCharFormat(char_format)
        else:
            current_underline = text_field.fontUnderline()
            text_field.setFontUnderline(not current_underline)

    def change_font(self, text_field):
        font, ok = QFontDialog.getFont()
        if ok:
            cursor = text_field.textCursor()
            if cursor.hasSelection():
                char_format = QTextCharFormat()
                char_format.setFont(font)
                cursor.mergeCharFormat(char_format)
            else:
                text_field.setCurrentFont(font)

    def change_text_color(self, text_field):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = text_field.textCursor()
            if cursor.hasSelection():
                char_format = QTextCharFormat()
                char_format.setForeground(color)
                cursor.mergeCharFormat(char_format)
            else:
                text_field.setTextColor(color)
    
    def insert_image(self, text_field):
        file_name, _ = QFileDialog.getOpenFileName(None, "Выбрать изображение", "", "Изображение (*.png *.jpg *.jpeg)")
        if file_name:
            cursor = text_field.textCursor()
            cursor.insertImage(file_name)
    
    def insert_hyperlink(self, text_field):
        url, ok = QInputDialog.getText(None, "Введите ссылку", "Ссылка")
        hyperlink_style = QTextCharFormat()
        hyperlink_style.setForeground(QColor(0, 128, 255))
        hyperlink_style.setFontUnderline(True)
        if url and ok:
            cursor = text_field.textCursor()
            cursor.insertText(url, hyperlink_style)
            cursor.insertText(" ", QTextCharFormat())
        
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
