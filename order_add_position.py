# -*- coding: utf-8 -*-
import pandas as pd
import pymongo
################################################################################
## Form generated from reading UI file 'order_add_position.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget)
from sqlalchemy import create_engine, text

import parameters


class Ui_Form(object):

    def refresh_suppliers_table(self):
        parameters.refresh_suppliers_table(self)

    def transfer_data(self, order_pk, mother_form):
        self.order_pk=order_pk
        self.mother_form=mother_form


    def mongo_add_position_to_order(self):  # add order entry mongo
        parameters.add_position_to_order(self)
        client = pymongo.MongoClient("localhost", 27017)  # mongo penis
        db = client.kursach_ais
        order_entry_mongo = db.order_entry
        post ={ "pk":"0",#pk_autoincrement.autoincrement_max("order_entry"),
                "name":self.goodsTableWidget.item(self.goodsTableWidget.currentRow(), 1 ).text(),
                "count":str(self.countSpinBox.value()),
                "price": self.priceLineEdit.text(),
                "related_to_order":self.order_pk,
                "sum": self.label.text(),
        }
        order_entry_mongo.insert_one(post)
        print(post)
        self.mother_form.refresh_order_entries_table()


    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(834, 519)
        self.confirmPushButton = QPushButton(Form, clicked = lambda:self.mongo_add_position_to_order())
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(670, 460, 121, 51))
        self.cancelPushButton = QPushButton(Form)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(370, 470, 121, 20))
        # self.countSpinBox = QSpinBox(Form, valueChanged = lambda:self.label.setText((self.countSpinBox.value()*int(self.priceLineEdit.text()))))
        # self.countSpinBox.setObjectName(u"countSpinBox")
        # self.countSpinBox.setGeometry(QRect(522, 120, 71, 22))
        # self.countSpinBox.setMinimum(1)
        # self.countSpinBox.setMaximum(100000)
        self.priceLineEdit = QLineEdit(Form)
        self.priceLineEdit.setObjectName(u"priceLineEdit")
        self.priceLineEdit.setGeometry(QRect(392, 120, 113, 21))
        self.priceLineEdit.setMaxLength(7)
        self.priceLineEdit.setText("1")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 120, 121, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(600, 90, 121, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(522, 90, 71, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(402, 90, 101, 16))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 361, 61))
        self.goodsTableWidget = QTableWidget(Form)

        self.countSpinBox = QSpinBox(Form, valueChanged=lambda: self.label.setText(str((
            (int(self.countSpinBox.value()) * int(self.priceLineEdit.text()))))))
        self.countSpinBox.setObjectName(u"countSpinBox")
        self.countSpinBox.setGeometry(QRect(522, 120, 71, 22))
        self.countSpinBox.setMinimum(1)
        self.countSpinBox.setMaximum(100000)

        if (self.goodsTableWidget.columnCount() < 3):
            self.goodsTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.goodsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.goodsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.goodsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.goodsTableWidget.setObjectName(u"goodsTableWidget")
        self.goodsTableWidget.setGeometry(QRect(20, 80, 331, 411))

        self.refresh_suppliers_table()


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0437\u0438\u0446\u0438\u0438", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c ", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
        self.priceLineEdit.setInputMask("[D999999999]")
        self.priceLineEdit.setText("1")
        self.label.setText(QCoreApplication.translate("Form", u"SumPH", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u043a\u043e\u043b-\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0446\u0435\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0437\u0438\u0446\u0438\u0438</span></p></body></html>", None))
        ___qtablewidgetitem = self.goodsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem1 = self.goodsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.goodsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0415\u0434.\u0438\u0437\u043c.", None));
    # retranslateUi

