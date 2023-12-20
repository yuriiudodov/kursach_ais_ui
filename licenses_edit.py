# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'license_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

import parameters


class Ui_Form(object):

    def write_license_to_db(self):
        DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        VetTableQuery.prepare("""
                                 UPDATE licenses SET license_name=:license_name, date=:date, expration_date=:expiration_date, license_key=:license_key WHERE pk=:pk
                                  """)
        VetTableQuery.bindValue("::license_name", self.licenseNameLineEdit.text())
        VetTableQuery.bindValue(":date", parameters.date_format(self.dateEdit.date().getDate()))
        VetTableQuery.bindValue(":expiration_date", parameters.date_format(self.expirationDateEdit.date().getDate()))
        VetTableQuery.bindValue(":license_key", self.keyTextEdit.toPlainText())

        VetTableQuery.bindValue(":pk", self.pk)
        uspeh = VetTableQuery.exec()
        print("USPEH BLYAT&", uspeh)
        VetDbConnnection.close()
    def transfer_data(self, pk, name, date, expiration_date, license_key):
        self.pk=pk
        self.name=name
        self.date=date
        self.expiration_date = expiration_date
        self.license_key = license_key
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(814, 550)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.expirationDateEdit = QDateEdit(Form)
        self.expirationDateEdit.setObjectName(u"expirationDateEdit")

        self.gridLayout.addWidget(self.expirationDateEdit, 7, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.confirmButton = QPushButton(Form)
        self.confirmButton.setObjectName(u"confirmButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmButton.sizePolicy().hasHeightForWidth())
        self.confirmButton.setSizePolicy(sizePolicy)
        self.confirmButton.setMaximumSize(QSize(200, 120))

        self.gridLayout.addWidget(self.confirmButton, 9, 1, 1, 1)

        self.keyTextEdit = QTextEdit(Form)
        self.keyTextEdit.setObjectName(u"keyTextEdit")

        self.gridLayout.addWidget(self.keyTextEdit, 8, 1, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.licenseNameLineEdit = QLineEdit(Form)
        self.licenseNameLineEdit.setObjectName(u"licenseNameLineEdit")

        self.gridLayout.addWidget(self.licenseNameLineEdit, 3, 1, 1, 1)

        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 6, 1, 1, 1)

        self.pushButton = QPushButton(Form, clicked = lambda: Form.close())  #close button
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(230, 16777215))

        self.gridLayout.addWidget(self.pushButton, 9, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.licenseNameLineEdit.setText(self.name)
        print(self.name, self.license_key)
        self.dateEdit.setDate(QDate.fromString(self.date, "dd.MM.yyyy"))
        self.expirationDateEdit.setDate(QDate.fromString(self.expiration_date, "dd.MM.yyyy"))
        self.keyTextEdit.setText(self.license_key)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u041b\u0438\u0446\u0435\u043d\u0437\u0438\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u0441:", None))
        self.confirmButton.setText(QCoreApplication.translate("Form", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.keyTextEdit.setMarkdown("")
        self.keyTextEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.keyTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u043f\u043e:", None))
        self.licenseNameLineEdit.setText("")
        self.licenseNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u041b\u0438\u0446\u0435\u043d\u0437\u0438\u0438", None))
    # retranslateUi

