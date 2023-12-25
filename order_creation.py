# -*- coding: utf-8 -*-
import pandas as pd
################################################################################
## Form generated from reading UI file 'order_creation.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QTableWidget, QTableWidgetItem, QWidget, QDialog)
from sqlalchemy import create_engine, text

import docs_browser
import order_add_position
import parameters


class Ui_Form(object):
    def refresh_order_entries_table(self):
        parameters.refresh_order_entries_table(self)
    def __init__(self):
        self.refresh_order_entries_table=parameters.refresh_order_entries_table()

    def change_order(self, order_num):
        self.order_num = order_num
        self.label_5.setText(str(self.order_num))
        self.refresh_order_entries_table()

    def __init__(self):
        self.order_num = parameters.just_give_doc_number()#pk+1 dayot nomer dokumenta dalya interfeisa, iz nego mozhno poluchit pk documenta otnyav 1

    def create_new_order(self):
        parameters.create_new_order()
        #new_order_pk = new_order_number-1
        self.order_num=parameters.just_give_doc_number()
        self.label_5.setText(str(self.order_num))
        self.refresh_order_entries_table()

    def open_docs_browser(self):#add order entry window
        self.window = QDialog()
        self.ui = docs_browser.Ui_widget()
        self.ui.transfer_form_pointer(self)
        self.ui.setupUi(self.window)
        self.window.show()

    def open_order_add_position(self):#add order entry window
        self.window = QDialog()
        self.ui = order_add_position.Ui_Form()
        self.ui.transfer_data(self.order_num, self)#vozmozhno oshibka i nado otnyat 1, ya v ujase pochemy ono rabotaet
        self.ui.setupUi(self.window)
        self.window.show()
    def transfer_data(self, customer, supplier, date):
        self.customer=customer
        self.supplier=supplier
        self.date=date



    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1017, 695)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 741, 61))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 91, 61))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 91, 61))
        self.label_3.setFont(font1)
        self.label_5 = QLabel(Form) #order number
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 10, 81, 61))
        self.label_5.setFont(font)
        self.label_5.setText(self.order_num)

        self.label_6 = QLabel(Form)#order date
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(420, 10, 201, 61))
        self.label_6.setFont(font)
        self.label_6.setText(self.date)


        self.label_4 = QLabel(Form)#supplier
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 90, 691, 21))
        self.label_4.setFont(font1)
        self.label_4.setText(self.supplier)

        self.label_7 = QLabel(Form)#customer
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 130, 781, 21))
        self.label_7.setFont(font1)
        self.label_7.setText(self.customer)

        self.positionsTableWidget = QTableWidget(Form)
        if (self.positionsTableWidget.columnCount() < 5):
            self.positionsTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.positionsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.positionsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.positionsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.positionsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.positionsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.positionsTableWidget.setObjectName(u"positionsTableWidget")
        self.positionsTableWidget.setGeometry(QRect(20, 190, 721, 371))
        self.addPushButton = QPushButton(Form, clicked = lambda: self.open_order_add_position())
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setGeometry(QRect(20, 580, 141, 81))
        self.deletePushButton = QPushButton(Form)
        self.deletePushButton.setObjectName(u"deletePushButton")
        self.deletePushButton.setGeometry(QRect(170, 580, 141, 81))
        self.createOrderPushButton = QPushButton(Form)
        self.createOrderPushButton.setObjectName(u"createOrderPushButton")
        self.createOrderPushButton.setGeometry(QRect(600, 580, 141, 81))
        self.newOrderPushButton = QPushButton(Form, clicked = lambda:self.create_new_order())#new order idk
        self.newOrderPushButton.setObjectName(u"createOrderPushButton_2")
        self.newOrderPushButton.setGeometry(QRect(870, 20, 141, 81))

        self.openDocsBrowserPushButton = QPushButton(Form, clicked=lambda: self.open_docs_browser())  # new order idk
        self.openDocsBrowserPushButton.setObjectName(u"createOrderPushButton_2")
        self.openDocsBrowserPushButton.setGeometry(QRect(800, 160, 141, 81))

        self.refresh_order_entries_table()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0430\u0437 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0443 \u2116             \u043e\u0442 ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c:", None))
        # self.label_5.setText(QCoreApplication.translate("Form", u"N", None))
        # self.label_6.setText(QCoreApplication.translate("Form", u"DATE", None))
        # self.label_4.setText(QCoreApplication.translate("Form", u"supplier", None))
        # self.label_7.setText(QCoreApplication.translate("Form", u"customer", None))
        ___qtablewidgetitem = self.positionsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u043d\u043e\u043c", None));
        ___qtablewidgetitem1 = self.positionsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem2 = self.positionsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0446\u0435\u043d\u0430", None));
        ___qtablewidgetitem3 = self.positionsTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u043a\u043e\u043b-\u0432\u043e", None));
        ___qtablewidgetitem4 = self.positionsTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0441\u0443\u043c\u043c\u0430", None));
        self.addPushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.deletePushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.createOrderPushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.newOrderPushButton.setText("новый")
        self.openDocsBrowserPushButton.setText("МЕНЕДЖЕР")
    # retranslateUi

