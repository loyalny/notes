import sys

from notes import Notes

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Notes(sys.argv)
    window.show()

    sys.exit(app.exec())