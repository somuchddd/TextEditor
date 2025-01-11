from PyQt6.QtGui import QTextCharFormat, QFont
from PyQt6.QtWidgets import (
    QColorDialog, QFontDialog
)

class TextEditorFunctions:
    def new_action(self, text_field):
        text_field.clear()

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

