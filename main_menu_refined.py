# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu_refined.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget, QDialog)

import licenses_view
import order_choose_organisations


class Ui_MainWindow(object):

    def open_order_creation(self):  # opens order_choose_organisations.py
        self.window = QDialog()
        self.ui = order_choose_organisations.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_license_manager(self):  # opens licenses manager (licenses_view.py)
        self.window = QDialog()
        self.ui = licenses_view.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1018, 600)
        MainWindow.setMaximumSize(QSize(1018, 16777215))
        icon = QIcon()
        iconThemeName = u"accessories-character-map"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(self.centralwidget, clicked = lambda: self.open_order_creation())
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.licensesPushButton = QPushButton(self.centralwidget, clicked = lambda: self.open_license_manager())
        self.licensesPushButton.setObjectName(u"licensesPushButton")
        self.licensesPushButton.setMinimumSize(QSize(0, 50))
        self.licensesPushButton.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.licensesPushButton, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(1000, 600))
        self.label.setPixmap(QPixmap(u"D:/\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0438/c652a4d3f6de2c3a232d72beeb9b8ac0.jpg"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1018, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u041c\u0435\u043d\u044e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u0443\u0441\u043a \u0437\u0430\u043a\u0430\u0437\u0430 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0443", None))
        self.licensesPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u044f\u043c\u0438", None))
        self.label.setText("")
    # retranslateUi

