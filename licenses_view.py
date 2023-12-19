# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'licenses_view.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QTableWidget, QTableWidgetItem, QWidget, QDialog)

import licenses_add
import licenses_edit
import pandas as pd
from sqlalchemy import text, create_engine

import parameters


class Ui_Form(object):

    def delete_license(self):
        DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        vet_query_str="""DELETE FROM license WHERE pk =""" + self.licensesTableWidget.item(self.licensesTableWidget.currentRow(), 0).text()
        VetTableQuery.prepare(vet_query_str)

        uspeh = VetTableQuery.exec()
        VetDbConnnection.close()

    def open_license_add(self):
        self.window = QDialog()
        self.ui = licenses_add.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_license_edit(self):
        self.window = QDialog()
        self.ui = licenses_edit.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def refresh_license_table(self):
        DB_PATH = parameters.DB_PATH  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        data_for_table = pd.read_sql(text(f'SELECT * FROM license'), db_connection).astype(str)
        self.licensesTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(len(data_for_table)):
                self.licensesTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(918, 674)
        self.licensesTableWidget = QTableWidget(Form)
        if (self.licensesTableWidget.columnCount() < 5):
            self.licensesTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.licensesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.licensesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.licensesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.licensesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.licensesTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.licensesTableWidget.setObjectName(u"licensesTableWidget")
        self.licensesTableWidget.setGeometry(QRect(50, 130, 771, 411))
        self.licensesTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.licensesTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.licensesTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.licensesTableWidget.horizontalHeader().setStretchLastSection(True)
        self.editPushButton = QPushButton(Form, clicked = lambda: self.open_license_edit())
        self.editPushButton.setObjectName(u"editPushButton")
        self.editPushButton.setGeometry(QRect(50, 570, 181, 81))
        self.addPushButton = QPushButton(Form, clicked = lambda: self.open_license_add())
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setGeometry(QRect(250, 570, 181, 81))
        self.deletePushButton = QPushButton(Form, clicked = lambda: self.delete_license())
        self.deletePushButton.setObjectName(u"deletePushButton")
        self.deletePushButton.setGeometry(QRect(670, 570, 181, 81))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 591, 81))
        font = QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.label.setFont(font)
        self.refresh_license_table()
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.licensesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem1 = self.licensesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None));
        ___qtablewidgetitem2 = self.licensesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None));
        ___qtablewidgetitem3 = self.licensesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0438\u0441\u0442\u0435\u0447\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem4 = self.licensesTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None));
        self.editPushButton.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.addPushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deletePushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u041b\u0438\u0446\u0435\u043d\u0437\u0438\u0439(\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440)", None))
    # retranslateUi

