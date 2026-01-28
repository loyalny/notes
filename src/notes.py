import sys
import time
import os
import json

from groq import Groq

from PySide6.QtWidgets import (QApplication, QMainWindow,
    QFileDialog, QMessageBox)

from PySide6.QtGui import QFont

from design import Ui_MainWindow


class Notes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = {}
        self.read_data()
        self.current_file_path = None
        self.setWindowTitle("Notes - Новый файл")
        self.ui.stackedWidget.setCurrentIndex(0)
        self.change_text_style()

        self.ui.openfile_btn.clicked.connect(self.open_file)
        self.ui.savefile_btn.clicked.connect(self.save_file)
        self.ui.savefileas_btn.clicked.connect(self.save_file_as)
        self.ui.newfile_btn.clicked.connect(self.create_new_file)
        self.ui.fontComboBox.currentFontChanged.connect(self.change_text_style)
        self.ui.spinBox.valueChanged.connect(self.change_text_style)
        self.ui.openai_btn.clicked.connect(self.open_ai_page)
        self.ui.openmainpage_btn.clicked.connect(self.open_main_page)
        self.ui.aianalyze_btn.clicked.connect(self.start_groq_work)
        self.ui.aiinfo_btn.clicked.connect(self.open_ai_info_page)

        self.ui.textEdit.textChanged.connect(self.update_chars_count)

    def read_data(self):
        try:
            with open("data.json", "r", encoding="utf-8") as data_file:
                self.data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}
            with open("data.json", "w", encoding="utf-8") as data_file:
                json.dump(self.data, data_file, ensure_ascii=False, indent=2)

        if "groq_api_key" in self.data:
            self.ui.aiapikey_lineedit.setText(self.data["groq_api_key"])

        if "current_font_size" in self.data:
            self.ui.spinBox.setValue(self.data["current_font_size"])

        if "current_font" in self.data:
            font = QFont(self.data["current_font"])
            self.ui.fontComboBox.setCurrentFont(font)

    def save_data(self, key, value):
        self.data[key] = value
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def start_groq_work(self):
        user_text = self.ui.textEdit.toPlainText().strip()
        user_api_key = self.ui.aiapikey_lineedit.text().strip()

        if not user_api_key:
            QMessageBox.warning(
                self,
                "Предупреждение!",
                "Введите Groq API key!"
            )
            return

        if not user_text:
            QMessageBox.warning(
                self,
                "Предупреждение!",
                "В вашем поле нету текста!"
            )
            return

        self.ui.aianalyze_btn.setEnabled(False)
        self.ui.aianalyze_btn.setText("Анализирую...")

        client = Groq(api_key=user_api_key)

        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Ты — анализатор текстов. Ниже будет приведён"
                    " текст пользователя. Тебе нужно проанализировать его и понять что это? Возможно,"
                    " это просто мысли пользователя, сочинение, программный код, математические формулы."
                    " Дай краткий анализ того, что ты видишь. Затем, в зависимости от того, что это,"
                    " тебе, может быть, придётся исправить ошибки (орфографические, математические, логические)."
                    " Прояви креативность и выдай ответ в формате: сначала небольшой анализ текста, а потом исправление"
                    " ошибок, но только если они есть. В самом конце упомяни, что анализ выполнен нейросетью, может"
                    " содержать ошибки, ответ сгенерирован только для справки. Удачи!"},
                    {"role": "user", "content": user_text}
                ],
                temperature=0.5,
                stream=True
            )

            self.ui.ai_textedit.clear()

            for chunk in completion:
                content = chunk.choices[0].delta.content
                if content:
                    self.ui.ai_textedit.insertPlainText(content)
                    QApplication.processEvents()
                    time.sleep(0.01)
        except Exception as error:
            QMessageBox.critical(
                self,
                "Возникла ошибка!",
                "Ошибка сервера" + str(error) + " !"
            )
        finally:
            self.ui.aianalyze_btn.setEnabled(True)
            self.ui.aianalyze_btn.setText("Анализировать")

    def open_ai_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def open_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def open_ai_info_page(self):
        QMessageBox.information(self, "ReviewAI", """
Review AI — это интеллектуальный помощник, интегрированный в ваш редактор. Он использует мощную нейросеть Llama 3.3 через платформу Groq для мгновенного анализа ваших записей.

Что умеет эта функция:
* Глубокий анализ: ИИ определит тип контента (код, эссе, список задач или математические формулы).
* Поиск ошибок: Проверка орфографии, пунктуации, а также логических и программных ошибок.
* Креативная правка: Советы по улучшению текста с сохранением вашего стиля.

Как воспользоваться:
1. Перейдите на сайт https://console.groq.com и зарегистрируйтесь.
2. Перейдите на вкладку API Keys и создайте новый ключ.
3. Скопируйте и вставьте его в соответствующее поле в приложении.

Внимание: Нейросеть пока не может анализировать слишком большие тексты. Ответы генерируются ИИ и могут содержать ошибки. Используйте их только в справочных целях.
""",
            QMessageBox.StandardButton.Ok
        )

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть файл",
            "",
            ""
        )

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    text = file.read()
                    self.ui.textEdit.setPlainText(text)

                self.ui.textEdit.document().setModified(False)
                self.current_file_path = file_path
                self.setWindowTitle(f"Notes - {file_path}")
                self.change_text_style()
            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Возникла ошибка!",
                    f"Ошибка при чтении файла: {error}!"
                )
        else:
            QMessageBox.warning(
                self,
                "Предупреждение!",
                "Вы не выбрали файл!"
            )

    def save_file(self):
        if self.current_file_path:
            try:
                with open(self.current_file_path, "w", encoding="utf-8") as file:
                    file.write(self.ui.textEdit.toPlainText())

                self.ui.textEdit.document().setModified(False)
                self.setWindowTitle(f"Notes - {self.current_file_path}")
            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Возникла ошибка!",
                    f"Ошибка при сохранении файла: {error}!"
                )
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
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.ui.textEdit.toPlainText())

                self.ui.textEdit.document().setModified(False)
                self.current_file_path = file_path
                self.setWindowTitle(f"Notes - {file_path}")
            except Exception as error:
                QMessageBox.critical(
                    self,
                    "Возникла ошибка!",
                    f"Ошибка при сохранении файла: {error}!"
                )
        else:
            QMessageBox.warning(
                self,
                "Предупреждение!",
                "Вы не сохранили файл!"
            )

    def is_safe_to_proceed(self, title, text):
        if self.ui.textEdit.document().isModified():
            reply_dialog = QMessageBox.question(
                self,
                title,
                text,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

            return reply_dialog == QMessageBox.StandardButton.Yes

        return True

    def create_new_file(self):
        if self.is_safe_to_proceed("Создать новый файл", "У вас есть несохраненные изменения. Вы уверены, что хотите потерять их?"):
            self.current_file_path = None
            self.ui.textEdit.setPlainText("")

    def change_text_style(self):
        new_font = self.ui.fontComboBox.currentFont()
        new_font.setPointSize(self.ui.spinBox.value())
        self.ui.textEdit.setFont(new_font)

        self.save_data("current_font_size", self.ui.spinBox.value())
        self.save_data("current_font", new_font.family())

    def update_chars_count(self):
        count = self.ui.textEdit.document().characterCount() - 1
        if count < 0: count = 0
        self.ui.charscount_label.setText(f"Символов: {count}")

        path = self.current_file_path if self.current_file_path else "Новый файл"
        star = "*" if self.ui.textEdit.document().isModified() else ""
        self.setWindowTitle(f"Notes - {path}{star}")

    def closeEvent(self, event, /):
        self.save_data("groq_api_key", self.ui.aiapikey_lineedit.text())
        if self.is_safe_to_proceed("Выход", "У вас есть несохраненные изменения. Вы уверены, что хотите выйти?"):
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Notes()
    window.show()

    sys.exit(app.exec())
