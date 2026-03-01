# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(749, 583)
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
        self.editor_page = QWidget()
        self.editor_page.setObjectName(u"editor_page")
        self.verticalLayout_2 = QVBoxLayout(self.editor_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btns_layout = QWidget(self.editor_page)
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
        self.open_file_btn = QPushButton(self.btns_layout)
        self.open_file_btn.setObjectName(u"open_file_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.open_file_btn.sizePolicy().hasHeightForWidth())
        self.open_file_btn.setSizePolicy(sizePolicy2)
        self.open_file_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.open_file_btn)

        self.new_file_btn = QPushButton(self.btns_layout)
        self.new_file_btn.setObjectName(u"new_file_btn")
        sizePolicy2.setHeightForWidth(self.new_file_btn.sizePolicy().hasHeightForWidth())
        self.new_file_btn.setSizePolicy(sizePolicy2)
        self.new_file_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.new_file_btn)

        self.save_file_btn = QPushButton(self.btns_layout)
        self.save_file_btn.setObjectName(u"save_file_btn")
        sizePolicy2.setHeightForWidth(self.save_file_btn.sizePolicy().hasHeightForWidth())
        self.save_file_btn.setSizePolicy(sizePolicy2)
        self.save_file_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.save_file_btn)

        self.save_file_as_btn = QPushButton(self.btns_layout)
        self.save_file_as_btn.setObjectName(u"save_file_as_btn")
        sizePolicy2.setHeightForWidth(self.save_file_as_btn.sizePolicy().hasHeightForWidth())
        self.save_file_as_btn.setSizePolicy(sizePolicy2)
        self.save_file_as_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.save_file_as_btn)

        self.font_combo_box = QFontComboBox(self.btns_layout)
        self.font_combo_box.setObjectName(u"font_combo_box")

        self.horizontalLayout_6.addWidget(self.font_combo_box)

        self.font_size_spin_box = QSpinBox(self.btns_layout)
        self.font_size_spin_box.setObjectName(u"font_size_spin_box")
        self.font_size_spin_box.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.font_size_spin_box.setMinimum(8)
        self.font_size_spin_box.setValue(18)

        self.horizontalLayout_6.addWidget(self.font_size_spin_box)


        self.verticalLayout_2.addWidget(self.btns_layout)

        self.editor_text_edit = QTextEdit(self.editor_page)
        self.editor_text_edit.setObjectName(u"editor_text_edit")
        self.editor_text_edit.setTabletTracking(False)
        self.editor_text_edit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.editor_text_edit.setFrameShape(QFrame.Shape.StyledPanel)
        self.editor_text_edit.setLineWidth(1)
        self.editor_text_edit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.verticalLayout_2.addWidget(self.editor_text_edit)

        self.text_info_layout = QWidget(self.editor_page)
        self.text_info_layout.setObjectName(u"text_info_layout")
        self.horizontalLayout_7 = QHBoxLayout(self.text_info_layout)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.app_version_label = QLabel(self.text_info_layout)
        self.app_version_label.setObjectName(u"app_version_label")
        sizePolicy.setHeightForWidth(self.app_version_label.sizePolicy().hasHeightForWidth())
        self.app_version_label.setSizePolicy(sizePolicy)
        self.app_version_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.app_version_label)

        self.chars_count_label = QLabel(self.text_info_layout)
        self.chars_count_label.setObjectName(u"chars_count_label")
        sizePolicy.setHeightForWidth(self.chars_count_label.sizePolicy().hasHeightForWidth())
        self.chars_count_label.setSizePolicy(sizePolicy)
        self.chars_count_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.chars_count_label)


        self.verticalLayout_2.addWidget(self.text_info_layout)

        self.stackedWidget.addWidget(self.editor_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.open_file_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.new_file_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.save_file_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.save_file_as_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.app_version_label.setText(QCoreApplication.translate("MainWindow", u"Notes 1.0", None))
        self.chars_count_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b\u043e\u0432: 0", None))
    # retranslateUi

