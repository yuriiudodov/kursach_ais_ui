# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget, QDialog)

import licenses_view
import order_choose_organisations


class Ui_Widget(object):

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
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(900, 900))
        self.licensesPushButton = QPushButton(Widget, clicked = lambda: self.open_license_manager())
        self.licensesPushButton.setObjectName(u"licensesPushButton")
        self.licensesPushButton.setGeometry(QRect(90, 570, 221, 41))
        self.orderPushButton = QPushButton(Widget, clicked = lambda: self.open_order_creation())
        self.orderPushButton.setObjectName(u"orderPushButton")
        self.orderPushButton.setGeometry(QRect(480, 570, 191, 31))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u041c\u0435\u043d\u044e", None))
        self.licensesPushButton.setText(QCoreApplication.translate("Widget", u"\u043f\u043e\u0434\u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u044f\u043c\u0438", None))
        self.orderPushButton.setText(QCoreApplication.translate("Widget", u"\u0432\u044b\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0443", None))
    # retranslateUi

