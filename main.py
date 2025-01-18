import sys
from PyQt6.QtWidgets import QApplication
from format_functions import TextEditorFunctions
from page_functions import FunctionsWithPages
from style_manager import StyleManager, StyleManagerFunctions
from GUI import TextEditorGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)

    format_functions = TextEditorFunctions()
    page_functions = FunctionsWithPages()
    style_manager_functions = StyleManagerFunctions()
    style_manager = StyleManager(style_manager_functions)

    editor = TextEditorGUI(format_functions, page_functions, style_manager)
    editor.show()

    sys.exit(app.exec())
