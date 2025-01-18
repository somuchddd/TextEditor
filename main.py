import sys
from PyQt6.QtWidgets import QApplication
from format_functions import TextEditorFunctions
from page_functions import FunctionsWithPages
from GUI import TextEditorGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)

    format_functions = TextEditorFunctions()
    page_functions = FunctionsWithPages()

    editor = TextEditorGUI(format_functions, page_functions)
    editor.show()

    sys.exit(app.exec())
