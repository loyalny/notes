# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFontComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 591)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 400))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu_book_24dp_000000.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout_2 = QVBoxLayout(self.main_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btns_layout = QWidget(self.main_page)
        self.btns_layout.setObjectName(u"btns_layout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btns_layout.sizePolicy().hasHeightForWidth())
        self.btns_layout.setSizePolicy(sizePolicy1)
        self.btns_layout.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.btns_layout)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.openfile_btn = QPushButton(self.btns_layout)
        self.openfile_btn.setObjectName(u"openfile_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.openfile_btn.sizePolicy().hasHeightForWidth())
        self.openfile_btn.setSizePolicy(sizePolicy2)
        self.openfile_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.openfile_btn)

        self.newfile_btn = QPushButton(self.btns_layout)
        self.newfile_btn.setObjectName(u"newfile_btn")
        sizePolicy2.setHeightForWidth(self.newfile_btn.sizePolicy().hasHeightForWidth())
        self.newfile_btn.setSizePolicy(sizePolicy2)
        self.newfile_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.newfile_btn)

        self.savefile_btn = QPushButton(self.btns_layout)
        self.savefile_btn.setObjectName(u"savefile_btn")
        sizePolicy2.setHeightForWidth(self.savefile_btn.sizePolicy().hasHeightForWidth())
        self.savefile_btn.setSizePolicy(sizePolicy2)
        self.savefile_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.savefile_btn)

        self.savefileas_btn = QPushButton(self.btns_layout)
        self.savefileas_btn.setObjectName(u"savefileas_btn")
        sizePolicy2.setHeightForWidth(self.savefileas_btn.sizePolicy().hasHeightForWidth())
        self.savefileas_btn.setSizePolicy(sizePolicy2)
        self.savefileas_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.savefileas_btn)

        self.fontComboBox = QFontComboBox(self.btns_layout)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout_6.addWidget(self.fontComboBox)

        self.spinBox = QSpinBox(self.btns_layout)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.spinBox.setMinimum(8)
        self.spinBox.setValue(18)

        self.horizontalLayout_6.addWidget(self.spinBox)

        self.openai_btn = QPushButton(self.btns_layout)
        self.openai_btn.setObjectName(u"openai_btn")
        sizePolicy2.setHeightForWidth(self.openai_btn.sizePolicy().hasHeightForWidth())
        self.openai_btn.setSizePolicy(sizePolicy2)
        self.openai_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.openai_btn)


        self.verticalLayout_2.addWidget(self.btns_layout)

        self.textEdit = QTextEdit(self.main_page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setTabletTracking(False)
        self.textEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.textEdit.setFrameShape(QFrame.Shape.StyledPanel)
        self.textEdit.setLineWidth(1)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit.setReadOnly(False)
        self.textEdit.setCursorWidth(1)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.textinfo_layout = QWidget(self.main_page)
        self.textinfo_layout.setObjectName(u"textinfo_layout")
        self.horizontalLayout_7 = QHBoxLayout(self.textinfo_layout)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.appversion_label = QLabel(self.textinfo_layout)
        self.appversion_label.setObjectName(u"appversion_label")
        sizePolicy.setHeightForWidth(self.appversion_label.sizePolicy().hasHeightForWidth())
        self.appversion_label.setSizePolicy(sizePolicy)
        self.appversion_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.appversion_label)

        self.charscount_label = QLabel(self.textinfo_layout)
        self.charscount_label.setObjectName(u"charscount_label")
        sizePolicy.setHeightForWidth(self.charscount_label.sizePolicy().hasHeightForWidth())
        self.charscount_label.setSizePolicy(sizePolicy)
        self.charscount_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.charscount_label)


        self.verticalLayout_2.addWidget(self.textinfo_layout)

        self.stackedWidget.addWidget(self.main_page)
        self.ai_page = QWidget()
        self.ai_page.setObjectName(u"ai_page")
        self.verticalLayout_3 = QVBoxLayout(self.ai_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.aiinfo_layout = QWidget(self.ai_page)
        self.aiinfo_layout.setObjectName(u"aiinfo_layout")
        self.horizontalLayout = QHBoxLayout(self.aiinfo_layout)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 0, 3, -1)
        self.openmainpage_btn = QPushButton(self.aiinfo_layout)
        self.openmainpage_btn.setObjectName(u"openmainpage_btn")
        sizePolicy2.setHeightForWidth(self.openmainpage_btn.sizePolicy().hasHeightForWidth())
        self.openmainpage_btn.setSizePolicy(sizePolicy2)
        self.openmainpage_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.openmainpage_btn)

        self.reviewai_label = QLabel(self.aiinfo_layout)
        self.reviewai_label.setObjectName(u"reviewai_label")
        sizePolicy.setHeightForWidth(self.reviewai_label.sizePolicy().hasHeightForWidth())
        self.reviewai_label.setSizePolicy(sizePolicy)
        self.reviewai_label.setStyleSheet(u"font-size: 25px;")
        self.reviewai_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.reviewai_label)

        self.aiinfo_btn = QPushButton(self.aiinfo_layout)
        self.aiinfo_btn.setObjectName(u"aiinfo_btn")
        self.aiinfo_btn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.aiinfo_btn.sizePolicy().hasHeightForWidth())
        self.aiinfo_btn.setSizePolicy(sizePolicy2)
        self.aiinfo_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/info_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aiinfo_btn.setIcon(icon1)
        self.aiinfo_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.aiinfo_btn)


        self.verticalLayout_3.addWidget(self.aiinfo_layout)

        self.aiapikey_lineedit = QLineEdit(self.ai_page)
        self.aiapikey_lineedit.setObjectName(u"aiapikey_lineedit")
        self.aiapikey_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.aiapikey_lineedit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.aiapikey_lineedit)

        self.ai_textedit = QTextEdit(self.ai_page)
        self.ai_textedit.setObjectName(u"ai_textedit")
        self.ai_textedit.setEnabled(True)
        font = QFont()
        font.setPointSize(14)
        self.ai_textedit.setFont(font)
        self.ai_textedit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.ai_textedit)

        self.aianalyze_btn = QPushButton(self.ai_page)
        self.aianalyze_btn.setObjectName(u"aianalyze_btn")
        self.aianalyze_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.aianalyze_btn)

        self.stackedWidget.addWidget(self.ai_page)
        self.ai_info_page = QWidget()
        self.ai_info_page.setObjectName(u"ai_info_page")
        self.verticalLayout_5 = QVBoxLayout(self.ai_info_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.openai_btn_1 = QPushButton(self.ai_info_page)
        self.openai_btn_1.setObjectName(u"openai_btn_1")
        self.openai_btn_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.openai_btn_1)

        self.aiinfo_textedit = QTextEdit(self.ai_info_page)
        self.aiinfo_textedit.setObjectName(u"aiinfo_textedit")
        self.aiinfo_textedit.setFont(font)
        self.aiinfo_textedit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.aiinfo_textedit)

        self.stackedWidget.addWidget(self.ai_info_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.openfile_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.newfile_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.savefile_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.savefileas_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.openai_btn.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.appversion_label.setText(QCoreApplication.translate("MainWindow", u"Notes 1.0", None))
        self.charscount_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b\u043e\u0432: 0", None))
        self.openmainpage_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.reviewai_label.setText(QCoreApplication.translate("MainWindow", u"Review AI", None))
        self.aiinfo_btn.setText("")
        self.aiapikey_lineedit.setInputMask("")
        self.aiapikey_lineedit.setText("")
        self.aiapikey_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0432\u043e\u0439 Groq API key", None))
        self.aianalyze_btn.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.openai_btn_1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.aiinfo_textedit.setMarkdown("")
        self.aiinfo_textedit.setPlaceholderText("")
    # retranslateUi

