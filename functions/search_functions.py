from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QTextCursor, QTextDocument


class SearchManagerFunctions():
    def __init__(self):
        super().__init__()
        self.matches = []
        self.current_match = -1

    def search_next(self, text_widget, search_text):
        if not search_text:
            QMessageBox.warning(None, "Ошибка", "Введите текст для поиска")     

        elif not self.matches:
            self.matches = []
            for i in range(text_widget.count()):
                text_field = text_widget.widget(i)
                document = text_field.document()
                cursor = text_field.textCursor()
                cursor.setPosition(0)
                while not cursor.isNull() and not cursor.atEnd():
                    cursor = document.find(search_text, cursor)
                    if not cursor.isNull():
                        self.matches.append((i, cursor.position()))

        else: 
            self.current_match = (self.current_match + 1) % len(self.matches)
            self.highlight_match(text_widget, search_text)

    def search_prev(self, text_widget, search_text):
        if not search_text:
            QMessageBox.warning(None, "Ошибка", "Введите текст для поиска")     

        elif not self.matches:
            self.matches = []
            for i in range(text_widget.count()):
                text_field = text_widget.widget(i)
                document = text_field.document()
                cursor = text_field.textCursor()
                cursor.setPosition(0)
                while not cursor.isNull() and not cursor.atEnd():
                    cursor = document.find(search_text, cursor)
                    if not cursor.isNull():
                        self.matches.append((i, cursor.position()))

        else:
            self.current_match = (self.current_match - 1) % len(self.matches)
            self.highlight_match(text_widget, search_text)

    def replace_current(self, text_widget, search_text, replace_text):
        if not replace_text:
            QMessageBox.warning(None, "Ошибка", "Введите текст для замены.")

        elif self.matches and self.current_match >= 0:
            tab_index, position = self.matches[self.current_match]
            text_edit = text_widget.widget(tab_index)
            cursor = text_edit.textCursor()
            cursor.setPosition(position)
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveMode.KeepAnchor, len(search_text))
            cursor.insertText(replace_text)
            for i in range(self.current_match + 1, len(self.matches)):
                if self.matches[i][0] == tab_index:
                    self.matches[i] = (self.matches[i][0], self.matches[i][1] + len(replace_text) - len(search_text))
            self.matches.pop(self.current_match)
            if self.matches:
                self.current_match = self.current_match % len(self.matches)
                self.highlight_match(text_widget, search_text)
            else:
                self.current_match_index = -1
            
    def replace_all(self, text_widget, search_text, replace_text):
        if not replace_text:
            QMessageBox.warning(None, "Ошибка", "Введите текст для замены.")

        for i in range(text_widget.count()):
            text_field = text_widget.widget(i)
            document = text_field.document()
            cursor = text_field.textCursor()
            cursor.setPosition(0)
            while not cursor.isNull() and not cursor.atEnd():
                cursor = document.find(search_text, cursor)
                if not cursor.isNull():
                    cursor.insertText(replace_text)
    
        self.matches = []
        self.current_match_index = -1

    def highlight_match(self, text_widget, search_text):
        text_index, position = self.matches[self.current_match]
        text_field = text_widget.widget(text_index)
        text_widget.setCurrentIndex(text_index)

        cursor = text_field.textCursor()
        cursor.setPosition(position)
        cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveMode.KeepAnchor, len(search_text))
        text_field.setTextCursor(cursor)
        text_field.ensureCursorVisible()

    def clear_matches(self):
        self.matches = []
        self.current_match = -1