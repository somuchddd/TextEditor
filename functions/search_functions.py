from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QTextCursor, QTextDocument
import re


class SearchManagerFunctions():
    def __init__(self):
        super().__init__()
        self.matches = []
        self.current_match = -1

    def search(self, text_widget, search_text, use_regex):
        self.matches = []
        self.current_match = -1

        if not search_text:
            QMessageBox.warning(None, "Ошибка", "Введите текст для поиска")     

        if not self.matches:
            try:
                if not use_regex:
                        search_text = re.escape(search_text)
                for i in range(text_widget.count()):
                    text_field = text_widget.widget(i)
                    document = text_field.toPlainText()
                    regex = re.compile(search_text)
                    iter = regex.finditer(document)
                    for match in iter:
                        start, end = match.span()
                        self.matches.append((i, start, end))
                        print("Добавлено совпадение:", (i, start, end))
            except re.error as e:
                QMessageBox.warning(None, "Ошибка", "Указано некорректно регулярное выражение")
        
        if self.matches:
            self.current_match = (self.current_match + 1) % len(self.matches)
            self.highlight_match(text_widget)

    def search_next(self, text_widget):
        if self.matches:
            self.current_match = (self.current_match + 1) % len(self.matches)
            self.highlight_match(text_widget)

        else: 
            QMessageBox.warning(None, "Ошибка", "Совпадений не найдено")

    def search_prev(self, text_widget):
        if self.matches:
            self.current_match = (self.current_match - 1) % len(self.matches)
            self.highlight_match(text_widget)

        else: 
            QMessageBox.warning(None, "Ошибка", "Совпадений не найдено")

    def replace_current(self, text_widget, replace_text):
        if not replace_text:
            QMessageBox.warning(None, "Ошибка", "Введите текст для замены.")

        elif self.matches and self.current_match >= 0:
            tab_index, start, end = self.matches[self.current_match]
            text_field = text_widget.widget(tab_index)
            cursor = text_field.textCursor()
            cursor.setPosition(start)
            cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, end-start)
            cursor.insertText(replace_text)
            for i in range(self.current_match + 1, len(self.matches)):
                if self.matches[i][0] == tab_index:
                    self.matches[i] = (self.matches[i][0], self.matches[i][1] + len(replace_text) - (end - start), self.matches[i][2] + len(replace_text) - (end - start))
            self.matches.pop(self.current_match)
            if self.matches:
                self.current_match = self.current_match % len(self.matches)
                self.highlight_match(text_widget)
            else:
                self.current_match_index = -1
            
    def replace_all(self, text_widget, replace_text):
        if not replace_text:
            QMessageBox.warning(None, "Ошибка", "Введите текст для замены.")

        for i in range(len(self.matches)):
            tab_index, start, end = self.matches[i]
            text_field = text_widget.widget(tab_index)
            cursor = text_field.textCursor()
            cursor.setPosition(start)
            cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, end-start)
            cursor.insertText(replace_text)
            for j in range(i + 1, len(self.matches)):
                if self.matches[j][0] == tab_index:
                    self.matches[j] = (self.matches[j][0], self.matches[j][1] + len(replace_text) - (end - start), self.matches[j][2] + len(replace_text) - (end - start))
    
        self.matches = []
        self.current_match_index = -1

    def highlight_match(self, text_widget):
        text_index, start, end = self.matches[self.current_match]
        text_field = text_widget.widget(text_index)
        text_widget.setCurrentIndex(text_index)

        cursor = text_field.textCursor()
        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, end-start)
        text_field.setTextCursor(cursor)
        text_field.ensureCursorVisible()

    def clear_matches(self):
        self.matches = []
        self.current_match = -1