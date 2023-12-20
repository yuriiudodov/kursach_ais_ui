# -*- coding: utf-8 -*-
import pandas as pd
################################################################################
## Form generated from reading UI file 'order_choose_organisations.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHeaderView,
                               QLabel, QPushButton, QSizePolicy, QTableWidget,
                               QTableWidgetItem, QWidget, QDialog)
from sqlalchemy import create_engine, text

import order_creation
import parameters


class Ui_Form(object):

    def open_order_creation(self):
        self.window = QDialog()
        self.ui = order_creation.Ui_Form()
        self.ui.transfer_data("PMC Wagner","PMC Redan", "04.12.2012")
        self.ui.setupUi(self.window)
        self.window.show()

    def refresh_customers_table(self):
        DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        data_for_table = pd.read_sql(text(f'SELECT * FROM customer'), db_connection).astype(str)
        self.customerTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(len(data_for_table)):
                self.customerTableWidget.setItem(row_num, col_num,
                                                 QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def refresh_suppliers_table(self):
        DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        data_for_table = pd.read_sql(text(f'SELECT * FROM supplier'), db_connection).astype(str)
        self.supplierTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(len(data_for_table)):
                self.supplierTableWidget.setItem(row_num, col_num,
                                                 QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1109, 593)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.customerTableWidget = QTableWidget(Form)
        if (self.customerTableWidget.columnCount() < 4):
            self.customerTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.customerTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.customerTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.customerTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.customerTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.customerTableWidget.setObjectName(u"customerTableWidget")
        self.customerTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.customerTableWidget.horizontalHeader().setStretchLastSection(True)
        self.customerTableWidget.verticalHeader().setHighlightSections(False)

        self.gridLayout.addWidget(self.customerTableWidget, 1, 0, 1, 2)

        self.supplierTableWidget = QTableWidget(Form)
        if (self.supplierTableWidget.columnCount() < 4):
            self.supplierTableWidget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.supplierTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.supplierTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.supplierTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.supplierTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.supplierTableWidget.setObjectName(u"supplierTableWidget")
        self.supplierTableWidget.horizontalHeader().setStretchLastSection(True)
        self.supplierTableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout.addWidget(self.supplierTableWidget, 1, 2, 1, 2)

        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 3, 1, 1)

        self.confirmPushButton = QPushButton(Form, clicked = lambda: self.open_order_creation())
        self.confirmPushButton.setObjectName(u"confirmPushButton")

        self.gridLayout.addWidget(self.confirmPushButton, 3, 3, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)

        self.cancelPushButton = QPushButton(Form, clicked = lambda:Form.close())
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setMinimumSize(QSize(0, 60))

        self.gridLayout.addWidget(self.cancelPushButton, 2, 0, 2, 1)
        self.refresh_customers_table()
        self.refresh_suppliers_table()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        ___qtablewidgetitem = self.customerTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem1 = self.customerTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem2 = self.customerTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0418\u041d\u041d", None));
        ___qtablewidgetitem3 = self.customerTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041a\u041f\u041f", None));
        ___qtablewidgetitem4 = self.supplierTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem5 = self.supplierTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem6 = self.supplierTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u0418\u041d\u041d", None));
        ___qtablewidgetitem7 = self.supplierTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u041a\u041f\u041f", None));
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

