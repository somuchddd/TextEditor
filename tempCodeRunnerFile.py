import sys
from PyQt6.QtWidgets import QApplication
from GUI import TextEditorGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditorGUI()
    editor.show()
    sys.exit(app.exec())

