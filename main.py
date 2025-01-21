import sys
from PyQt6.QtWidgets import QApplication
from functions.format_functions import TextEditorFunctions
from functions.page_functions import FunctionsWithPages
from functions.search_functions import SearchManagerFunctions
from managers.style_manager import StyleManagerFunctions
from GUI import TextEditorGUI


if __name__ == '__main__':
    app = QApplication(sys.argv)

    format_functions = TextEditorFunctions()
    page_functions = FunctionsWithPages()
    style_manager_functions = StyleManagerFunctions()
    search_manager_functions = SearchManagerFunctions()

    editor = TextEditorGUI(format_functions, page_functions, style_manager_functions, search_manager_functions)
    editor.show()

    sys.exit(app.exec())
