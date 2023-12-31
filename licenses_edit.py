# -*- coding: utf-8 -*-
import pymongo
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

    def transfer_mother_form_pointer(self, mother_form_poiner):
        self.licenses_view_pointer=mother_form_poiner

    def mongo_write_license_to_db(self):  # add order entry mongo
        parameters.write_license_to_db(self)
        client = pymongo.MongoClient("localhost", 27017)  # mongo penis
        db = client.kursach_ais
        order_entry_mongo = db.license
        post ={
                "license_name":self.licenseNameLineEdit.text(),
                "date":parameters.date_format(self.dateEdit.date().getDate()),
                "expiration_date": parameters.date_format(self.expirationDateEdit.date().getDate()),
                "key": str(self.keyTextEdit.toPlainText()),
        }
        myquery = {"license_name": self.name,"date": self.date,"expiration_date": self.expiration_date,"key": self.license_key}
        newvalues = {"$set": {"license_name": self.licenseNameLineEdit.text(),"date": parameters.date_format(self.dateEdit.date().getDate()),"expiration_date": parameters.date_format(self.expirationDateEdit.date().getDate()),"key": self.keyTextEdit.toPlainText(),"pk": self.pk}}

        order_entry_mongo.update_one(myquery, newvalues)
        self.licenses_view_pointer.refresh_license_table()
        print(post, "edited")

    def transfer_data(self, pk, name, date, expiration_date, license_key):
        self.pk=pk
        self.name=name
        self.date=date
        self.date1=date
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

        self.confirmButton = QPushButton(Form, clicked = lambda: self.mongo_write_license_to_db())
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

        print(self.date)
        self.licenseNameLineEdit.setText(self.name)#vot tut hyeta
        self.dateEdit.setDate(QDate.fromString(self.date, "d.M.yyyy"))
        self.expirationDateEdit.setDate(QDate.fromString(str(self.expiration_date), "d.M.yyyy"))
        self.keyTextEdit.setText(self.license_key)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u041b\u0438\u0446\u0435\u043d\u0437\u0438\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u0441:", None))
        self.confirmButton.setText(QCoreApplication.translate("Form", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.keyTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u043f\u043e:", None))
        self.licenseNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u041b\u0438\u0446\u0435\u043d\u0437\u0438\u0438", None))
    # retranslateUi

