from PyQt6.QtGui import (
    QTextCharFormat, QFont, QColor, QTextCursor
)
from PyQt6.QtWidgets import (
    QColorDialog, QFontDialog, QTextEdit, QMessageBox, QFileDialog, QInputDialog
)
class TextEditorFunctions:
    def __init__(self):
        self.numbering = False
        self.full_document = False

    def toggle_bold(self, text_widget):
        cursor = text_widget.currentWidget().textCursor()  
        if self.full_document == False:
            if cursor.hasSelection():  
                current_format = cursor.charFormat()
                char_format = QTextCharFormat()
                char_format.setFontWeight(QFont.Weight.Bold if current_format.fontWeight() != QFont.Weight.Bold else QFont.Weight.Normal)
                cursor.mergeCharFormat(char_format)
            else: 
                current_weight = text_widget.currentWidget().fontWeight()
                text_widget.currentWidget().setFontWeight(QFont.Weight.Bold if current_weight != QFont.Weight.Bold else QFont.Weight.Normal)
        else:
            current_format = cursor.charFormat()
            for i in range(text_widget.count()):
                text_field = text_widget.widget(i)
                cursor = text_field.textCursor()
                cursor.select(QTextCursor.SelectionType.Document)
                char_format = QTextCharFormat()
                char_format.setFontWeight(QFont.Weight.Bold if current_format.fontWeight() != QFont.Weight.Bold else QFont.Weight.Normal)
                cursor.mergeCharFormat(char_format)
   
    def toggle_italic(self, text_widget):
        cursor = text_widget.currentWidget().textCursor()
        if self.full_document == False:
            if cursor.hasSelection():
                current_format = cursor.charFormat()
                char_format = QTextCharFormat()

                char_format.setFontItalic(not current_format.fontItalic())
                cursor.mergeCharFormat(char_format)
            else:
                current_italic = text_widget.currentWidget().fontItalic()
                text_widget.currentWidget().setFontItalic(not current_italic)
        else: 
            current_format = cursor.charFormat()
            for i in range(text_widget.count()):
                text_field = text_widget.widget(i)
                cursor = text_field.textCursor()
                cursor.select(QTextCursor.SelectionType.Document)
                char_format = QTextCharFormat()
                char_format.setFontItalic(not current_format.fontItalic())
                cursor.mergeCharFormat(char_format)
            
    def toggle_underline(self, text_widget):
        cursor = text_widget.currentWidget().textCursor()
        if not self.full_document:
            if cursor.hasSelection():
                current_format = cursor.charFormat()
                char_format = QTextCharFormat()

                char_format.setFontUnderline(not current_format.fontUnderline())
                cursor.mergeCharFormat(char_format)
            else:
                current_underline = text_widget.currentWidget().fontUnderline()
                text_widget.currentWidget().setFontUnderline(not current_underline)
        else: 
            current_format = cursor.charFormat()
            for i in range(text_widget.count()):
                text_field = text_widget.widget(i)
                cursor = text_field.textCursor()
                cursor.select(QTextCursor.SelectionType.Document)
                char_format = QTextCharFormat()
                char_format.setFontUnderline(not current_format.fontUnderline())
                cursor.mergeCharFormat(char_format)

    def change_font(self, text_widget):
        font, ok = QFontDialog.getFont()
        if ok and not self.full_document:
            cursor = text_widget.currentWidget().textCursor()
            if cursor.hasSelection():
                char_format = QTextCharFormat()
                char_format.setFont(font)
                cursor.mergeCharFormat(char_format)
            else:
                text_widget.currentWidget().setCurrentFont(font)
        elif ok and self.full_document: 
            for i in range(text_widget.count()):
                text_field = text_widget.widget(i)
                cursor = text_field.textCursor()
                cursor.select(QTextCursor.SelectionType.Document)
                char_format = QTextCharFormat()
                char_format.setFont(font)
                cursor.mergeCharFormat(char_format)

    def change_text_color(self, text_widget):
        color = QColorDialog.getColor()
        if color.isValid() and not self.full_document:
            cursor = text_widget.currentWidget().textCursor()
            if cursor.hasSelection():
                char_format = QTextCharFormat()
                char_format.setForeground(color)
                cursor.mergeCharFormat(char_format)
            else:
                text_widget.currentWidget().setTextColor(color)
        elif color.isValid() and self.full_document:
            for i in range(text_widget.count()):
                text_field = text_widget.widget(i)
                cursor = text_field.textCursor()
                cursor.select(QTextCursor.SelectionType.Document)
                char_format = QTextCharFormat()
                char_format.setForeground(color)
                cursor.mergeCharFormat(char_format)

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

    def toggle_full_document_format(self):
        self.full_document = not self.full_document
