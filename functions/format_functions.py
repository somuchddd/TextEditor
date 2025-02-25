from PyQt6.QtGui import (
    QTextCharFormat, QFont, QColor, QTextCursor, QImage, QTextBlockFormat
)
from PyQt6.QtWidgets import (
    QColorDialog, QFontDialog, QFileDialog, QInputDialog
)
from PyQt6.QtCore import Qt


class TextEditorFunctions():
    def __init__(self):
        self.full_document = False

    def toggle_bold(self, text_widget):
        if text_widget.count() != 0:
            cursor = text_widget.currentWidget().textCursor()  
            if self.full_document == False:
                current_format = cursor.charFormat()
                char_format = QTextCharFormat()
                char_format.setFontWeight(QFont.Weight.Bold if current_format.fontWeight() != QFont.Weight.Bold else QFont.Weight.Normal)
                cursor.mergeCharFormat(char_format)
                text_widget.currentWidget().setTextCursor(cursor)
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
        if text_widget.count() != 0:
            cursor = text_widget.currentWidget().textCursor()
            if self.full_document == False:
                    current_format = cursor.charFormat()
                    char_format = QTextCharFormat()
                    char_format.setFontItalic(not current_format.fontItalic())
                    cursor.mergeCharFormat(char_format)
                    text_widget.currentWidget().setTextCursor(cursor)
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
        if text_widget.count() != 0:
            cursor = text_widget.currentWidget().textCursor()
            if not self.full_document:
                current_format = cursor.charFormat()
                char_format = QTextCharFormat()
                char_format.setFontUnderline(not current_format.fontUnderline())
                cursor.mergeCharFormat(char_format)
                text_widget.currentWidget().setTextCursor(cursor)
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
        if text_widget.count() != 0:
            if ok and not self.full_document:
                cursor = text_widget.currentWidget().textCursor()
                char_format = QTextCharFormat()
                char_format.setFont(font)
                cursor.mergeCharFormat(char_format)
                text_widget.currentWidget().setTextCursor(cursor)
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
        if text_widget.count() != 0:
            if color.isValid() and not self.full_document:
                cursor = text_widget.currentWidget().textCursor()
                char_format = QTextCharFormat()
                char_format.setForeground(color)
                cursor.mergeCharFormat(char_format)
                text_widget.currentWidget().setTextCursor(cursor)
            elif color.isValid() and self.full_document:
                for i in range(text_widget.count()):
                    text_field = text_widget.widget(i)
                    cursor = text_field.textCursor()
                    cursor.select(QTextCursor.SelectionType.Document)
                    char_format = QTextCharFormat()
                    char_format.setForeground(color)
                    cursor.mergeCharFormat(char_format)

    def insert_image(self, text_field, size):
        file_name, _ = QFileDialog.getOpenFileName(None, "Выбрать изображение", "", "Изображение (*.png *.jpg *.jpeg)")
        if file_name:
            image = QImage(file_name)
            image = image.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio)
            cursor = text_field.textCursor()

            cursor.insertBlock()
            block_format = QTextBlockFormat()
            block_format.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cursor.mergeBlockFormat(block_format)

            cursor.insertImage(image)

    def insert_hyperlink(self, text_field):
        url, ok = QInputDialog.getText(None, "Введите ссылку", "Ссылка")
        hyperlink_style = QTextCharFormat()
        hyperlink_style.setForeground(QColor(0, 128, 255))
        hyperlink_style.setFontUnderline(True)
        hyperlink_style.setAnchor(True)
        hyperlink_style.setAnchorHref(url)
        if url and ok:
            cursor = text_field.textCursor()
            cursor.insertText(url, hyperlink_style)
            cursor.insertText(" ", QTextCharFormat())

    def toggle_full_document_format(self):
        self.full_document = not self.full_document

    def clear_format(self, text_widget):
        text_widget.currentWidget().setCurrentCharFormat(QTextCharFormat())