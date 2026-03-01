import sys
import json

from PySide6.QtWidgets import (QApplication, QMainWindow,
QFileDialog, QMessageBox)

from PySide6.QtGui import QFont, QKeySequence, QShortcut
from PySide6.QtCore import Qt, QEvent

from design import Ui_MainWindow


class Notes(QMainWindow):
    def __init__(self, args=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = None
        self.data_file = "data.json"
        self.read_data()
        self.current_file_path = None

        self.setWindowTitle("Notes - Новый файл")
        self.change_text_style()

        # разрешаем drag-and-drop
        self.setAcceptDrops(True)

        #editor_page_btns
        self.ui.open_file_btn.clicked.connect(self.open_file)
        self.ui.save_file_btn.clicked.connect(self.save_file)
        self.ui.save_file_as_btn.clicked.connect(self.save_file_as)
        self.ui.new_file_btn.clicked.connect(self.create_new_file)
        self.ui.font_combo_box.currentFontChanged.connect(self.change_text_style)
        self.ui.font_size_spin_box.valueChanged.connect(self.change_text_style)

        #editor_text_edit
        self.ui.editor_text_edit.textChanged.connect(self.update_chars_count)
        # убираем вставку текста вместе со стилями
        self.ui.editor_text_edit.setAcceptRichText(False)
        # отключаем дефолтную реакцию поля на drop файла
        self.ui.editor_text_edit.setAcceptDrops(False)
        # фильтр событий на поле (для Tab)
        self.ui.editor_text_edit.installEventFilter(self)

        # создаём шорткаты
        self.save_file_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.save_file_shortcut.activated.connect(self.save_file)

        self.new_file_shortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        self.new_file_shortcut.activated.connect(self.create_new_file)

        self.open_file_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.open_file_shortcut.activated.connect(self.open_file)

        if args and len(args) > 1:
            file_to_open = args[1]
            self.load_file_from_path(file_to_open)

    def read_data(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as data_file:
                self.data = json.load(data_file)
        except (json.JSONDecodeError, FileNotFoundError):
            self.data = {}

        if "current_font" in self.data:
            self.ui.font_combo_box.setCurrentFont(QFont(self.data["current_font"]))
        if "current_font_size" in self.data:
            self.ui.font_size_spin_box.setValue(self.data["current_font_size"])

        self.save_data()

    def save_data(self):
        with open(self.data_file, "w", encoding="utf-8") as data_file:
            json.dump(self.data, data_file, ensure_ascii=False, indent=4)

    def load_file_from_path(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                self.ui.editor_text_edit.setPlainText(text)

            self.ui.editor_text_edit.document().setModified(False)
            self.current_file_path = file_path
            self.setWindowTitle(f"Notes - {file_path}")
        except Exception as error:
            QMessageBox.critical(
                self,
                "Возникла ошибка!",
                f"Ошибка при чтении файла: {error}!"
            )

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть файл",
            "",
            ""
        )

        if file_path: self.load_file_from_path(file_path)

    def create_new_file(self):
        if self.is_safe_to_proceed("Создать новый файл", "У вас есть несохраненные изменения. Вы уверены, что хотите потерять их?"):
            self.current_file_path = None
            self.ui.editor_text_edit.clear()

    def write_file(self, file_path):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.ui.editor_text_edit.toPlainText())

            self.ui.editor_text_edit.document().setModified(False)
            self.current_file_path = file_path
            self.setWindowTitle(f"Notes - {file_path}")
        except Exception as error:
            QMessageBox.critical(
                self,
                "Возникла ошибка!",
                f"Ошибка при сохранении файла: {error}!"
            )

    def save_file(self):
        if self.current_file_path:
            self.write_file(self.current_file_path)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить файл как",
            "",
            ""
        )

        if file_path:
            self.write_file(file_path)

    def change_text_style(self):
        new_font = self.ui.font_combo_box.currentFont()
        new_size = self.ui.font_size_spin_box.value()
        new_font.setPointSize(new_size)

        self.ui.editor_text_edit.setFont(new_font)

        self.data["current_font"] = new_font.family()
        self.data["current_font_size"] = new_size

        self.save_data()

    def update_chars_count(self):
        count = self.ui.editor_text_edit.document().characterCount() - 1
        if count < 0: count = 0
        self.ui.chars_count_label.setText(f"Символов: {count}")

        path = self.current_file_path if self.current_file_path else "Новый файл"
        star = "*" if self.ui.editor_text_edit.document().isModified() else ""
        self.setWindowTitle(f"Notes - {path}{star}")

    def is_safe_to_proceed(self, title, text):
        if self.ui.editor_text_edit.document().isModified():
            reply_dialog = QMessageBox.question(
                self,
                title,
                text,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

            return reply_dialog == QMessageBox.StandardButton.Yes

        return True

    def closeEvent(self, event, /):
        if self.is_safe_to_proceed("Выход", "У вас есть несохраненные изменения. Вы уверены, что хотите выйти?"):
            event.accept()
        else:
            event.ignore()

    def dragEnterEvent(self, event, /):
        if event.mimeData().hasUrls():
            event.accept()
        else: event.ignore()

    def dropEvent(self, event, /):
        all_urls = event.mimeData().urls()
        clean_paths = []
        for url in all_urls:
            file_path = url.toLocalFile()
            clean_paths.append(file_path)

        if len(clean_paths) > 0:
            first_file = clean_paths[0]
            if self.is_safe_to_proceed("Открыть файл", "У вас есть несохраненные изменения. Продолжить?"):
                self.load_file_from_path(first_file)

    def eventFilter(self, watched, event, /):
        if watched is self.ui.editor_text_edit and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Tab:
                self.ui.editor_text_edit.insertPlainText(" " * 4)
                return True
        return super().eventFilter(watched, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Notes(sys.argv)
    window.show()

    sys.exit(app.exec())
