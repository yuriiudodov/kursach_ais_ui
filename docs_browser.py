# -*- coding: utf-8 -*-
import pandas as pd
################################################################################
## Form generated from reading UI file 'docs_browser.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
from sqlalchemy import create_engine, text

import parameters


class Ui_widget(object):

    def refresh_orders_table(self):
        DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        data_for_table = pd.read_sql(text(
            f'SELECT pk, pk+1 AS number, date  FROM orderj'),
                                     db_connection).astype(str)
        self.docsTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(len(data_for_table)):
                self.docsTableWidget.setItem(row_num, col_num,
                                                  QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def transfer_form_pointer(self, mother_form_pointer):
        self.mother_form_pointer=mother_form_pointer

    def choose_document_and_close(self, widget):
        self.mother_form_pointer.change_order(self.docsTableWidget.item(self.docsTableWidget.currentRow(), 1).text())
        widget.close()
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(598, 680)
        self.docsTableWidget = QTableWidget(widget)
        if (self.docsTableWidget.columnCount() < 3):
            self.docsTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.docsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.docsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.docsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.docsTableWidget.setObjectName(u"docsTableWidget")
        self.docsTableWidget.setGeometry(QRect(60, 100, 331, 461))
        self.confirmPushButton = QPushButton(widget, clicked= lambda: self.choose_document_and_close(widget))
        self.confirmPushButton.setObjectName(u"choosePushButton")
        self.confirmPushButton.setGeometry(QRect(420, 610, 121, 41))
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 251, 51))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.cancelPushButton = QPushButton(widget, clicked =  lambda:widget.close())
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(40, 610, 121, 41))
        self.refresh_orders_table()
        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u0412\u044b\u0431\u043e\u0440 \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        ___qtablewidgetitem = self.docsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widget", u"\u041f\u041a", None));
        ___qtablewidgetitem1 = self.docsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widget", u"\u043d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem2 = self.docsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u0442\u0430", None));
        self.confirmPushButton.setText(QCoreApplication.translate("widget", u"\u0412\u044b\u0431\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u0412\u044b\u0431\u043e\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.cancelPushButton.setText(QCoreApplication.translate("widget", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

