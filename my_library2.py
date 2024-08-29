# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_library3DudUBn.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import m_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1158, 839)
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(Form)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: #646fff;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_menu = QToolButton(self.frame)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/img/rasmlar/menu_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(50, 50))
        self.btn_menu.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_menu)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size:20px;")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 30))
        self.label_3.setMaximumSize(QSize(50, 50))
        self.label_3.setPixmap(QPixmap(u":/img/rasmlar/account_circle_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size:20px;")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_menu_ochirish = QToolButton(self.frame)
        self.btn_menu_ochirish.setObjectName(u"btn_menu_ochirish")
        self.btn_menu_ochirish.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/img/rasmlar/close_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_ochirish.setIcon(icon1)
        self.btn_menu_ochirish.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_menu_ochirish)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 3)

        self.chap_menu = QFrame(self.page)
        self.chap_menu.setObjectName(u"chap_menu")
        self.chap_menu.setMaximumSize(QSize(16777215, 16777215))
        self.chap_menu.setStyleSheet(u"QFrame{\n"
"background-color: rgb(52, 51, 52);\n"
"}\n"
"\n"
"QPushButton {\n"
"color:grey;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"color:white;\n"
"}")
        self.chap_menu.setFrameShape(QFrame.StyledPanel)
        self.chap_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.chap_menu)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.btn_asosiy_sahifa = QPushButton(self.chap_menu)
        self.btn_asosiy_sahifa.setObjectName(u"btn_asosiy_sahifa")
        self.btn_asosiy_sahifa.setLayoutDirection(Qt.LeftToRight)
        self.btn_asosiy_sahifa.setStyleSheet(u"\n"
"#btn_home {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/img/rasmlar/home_50dp_7E7E7D_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/img/rasmlar/home_50dp_FFFFFF_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_asosiy_sahifa.setIcon(icon2)
        self.btn_asosiy_sahifa.setIconSize(QSize(40, 30))
        self.btn_asosiy_sahifa.setCheckable(True)
        self.btn_asosiy_sahifa.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_asosiy_sahifa)

        self.btn_menu_kitoblar = QPushButton(self.chap_menu)
        self.btn_menu_kitoblar.setObjectName(u"btn_menu_kitoblar")
        self.btn_menu_kitoblar.setStyleSheet(u"\n"
"#btn_home_2 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_2:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/img/rasmlar/library_books_24dp_666666_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/img/rasmlar/library_books_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_kitoblar.setIcon(icon3)
        self.btn_menu_kitoblar.setIconSize(QSize(40, 30))
        self.btn_menu_kitoblar.setCheckable(True)
        self.btn_menu_kitoblar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_kitoblar)

        self.btn_menu_talabalar = QPushButton(self.chap_menu)
        self.btn_menu_talabalar.setObjectName(u"btn_menu_talabalar")
        self.btn_menu_talabalar.setStyleSheet(u"\n"
"#btn_home_3 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_3:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/img/rasmlar/groups_24dp_666666_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/img/rasmlar/groups_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24 (2).png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_talabalar.setIcon(icon4)
        self.btn_menu_talabalar.setIconSize(QSize(40, 30))
        self.btn_menu_talabalar.setCheckable(True)
        self.btn_menu_talabalar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_talabalar)

        self.btn_menu_olingan_kitoblar = QPushButton(self.chap_menu)
        self.btn_menu_olingan_kitoblar.setObjectName(u"btn_menu_olingan_kitoblar")
        self.btn_menu_olingan_kitoblar.setStyleSheet(u"\n"
"#btn_home_4 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_4:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/img/rasmlar/menu_book_24dp_666666_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/img/rasmlar/menu_book_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_olingan_kitoblar.setIcon(icon5)
        self.btn_menu_olingan_kitoblar.setIconSize(QSize(40, 30))
        self.btn_menu_olingan_kitoblar.setCheckable(True)
        self.btn_menu_olingan_kitoblar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_olingan_kitoblar)

        self.btn_menu_muddati_otgan_kitoblar = QPushButton(self.chap_menu)
        self.btn_menu_muddati_otgan_kitoblar.setObjectName(u"btn_menu_muddati_otgan_kitoblar")
        self.btn_menu_muddati_otgan_kitoblar.setStyleSheet(u"\n"
"#btn_home_5 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_5:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/img/rasmlar/import_contacts_24dp_666666_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/img/rasmlar/import_contacts_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_muddati_otgan_kitoblar.setIcon(icon6)
        self.btn_menu_muddati_otgan_kitoblar.setIconSize(QSize(40, 30))
        self.btn_menu_muddati_otgan_kitoblar.setCheckable(True)
        self.btn_menu_muddati_otgan_kitoblar.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_menu_muddati_otgan_kitoblar)

        self.verticalSpacer = QSpacerItem(20, 375, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_menu_chiqish = QPushButton(self.chap_menu)
        self.btn_menu_chiqish.setObjectName(u"btn_menu_chiqish")
        self.btn_menu_chiqish.setStyleSheet(u"#btn_home_6 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_6:checked {\n"
"  color: white;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/img/rasmlar/close_24dp_666666_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/img/rasmlar/close_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_menu_chiqish.setIcon(icon7)
        self.btn_menu_chiqish.setCheckable(True)

        self.verticalLayout.addWidget(self.btn_menu_chiqish)


        self.gridLayout_3.addWidget(self.chap_menu, 1, 0, 1, 1)

        self.chap_kichik_menu = QFrame(self.page)
        self.chap_kichik_menu.setObjectName(u"chap_kichik_menu")
        self.chap_kichik_menu.setMinimumSize(QSize(50, 0))
        self.chap_kichik_menu.setMaximumSize(QSize(100, 16777215))
        self.chap_kichik_menu.setStyleSheet(u"QFrame{\n"
"background-color: rgb(52, 51, 52);\n"
"}\n"
"\n"
"QPushButton {\n"
"color:grey;\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border:none;\n"
"}")
        self.chap_kichik_menu.setFrameShape(QFrame.StyledPanel)
        self.chap_kichik_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.chap_kichik_menu)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.btn_asosiy_sahifa2 = QPushButton(self.chap_kichik_menu)
        self.btn_asosiy_sahifa2.setObjectName(u"btn_asosiy_sahifa2")
        self.btn_asosiy_sahifa2.setLayoutDirection(Qt.LeftToRight)
        self.btn_asosiy_sahifa2.setStyleSheet(u"\n"
"#btn_home {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        self.btn_asosiy_sahifa2.setIcon(icon2)
        self.btn_asosiy_sahifa2.setIconSize(QSize(40, 30))
        self.btn_asosiy_sahifa2.setCheckable(True)
        self.btn_asosiy_sahifa2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_asosiy_sahifa2)

        self.btn_menu_kitoblar2 = QPushButton(self.chap_kichik_menu)
        self.btn_menu_kitoblar2.setObjectName(u"btn_menu_kitoblar2")
        self.btn_menu_kitoblar2.setStyleSheet(u"\n"
"#btn_home_2 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_2:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        self.btn_menu_kitoblar2.setIcon(icon3)
        self.btn_menu_kitoblar2.setIconSize(QSize(40, 30))
        self.btn_menu_kitoblar2.setCheckable(True)
        self.btn_menu_kitoblar2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_kitoblar2)

        self.btn_menu_talabalar2 = QPushButton(self.chap_kichik_menu)
        self.btn_menu_talabalar2.setObjectName(u"btn_menu_talabalar2")
        self.btn_menu_talabalar2.setStyleSheet(u"\n"
"#btn_home_3 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_3:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        self.btn_menu_talabalar2.setIcon(icon4)
        self.btn_menu_talabalar2.setIconSize(QSize(40, 30))
        self.btn_menu_talabalar2.setCheckable(True)
        self.btn_menu_talabalar2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_talabalar2)

        self.btn_menu_olingan_kitoblar2 = QPushButton(self.chap_kichik_menu)
        self.btn_menu_olingan_kitoblar2.setObjectName(u"btn_menu_olingan_kitoblar2")
        self.btn_menu_olingan_kitoblar2.setStyleSheet(u"\n"
"#btn_home_4 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_4:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        self.btn_menu_olingan_kitoblar2.setIcon(icon5)
        self.btn_menu_olingan_kitoblar2.setIconSize(QSize(40, 30))
        self.btn_menu_olingan_kitoblar2.setCheckable(True)
        self.btn_menu_olingan_kitoblar2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_olingan_kitoblar2)

        self.btn_menu_muddati_otgan_kitoblar2 = QPushButton(self.chap_kichik_menu)
        self.btn_menu_muddati_otgan_kitoblar2.setObjectName(u"btn_menu_muddati_otgan_kitoblar2")
        self.btn_menu_muddati_otgan_kitoblar2.setStyleSheet(u"\n"
"#btn_home_5 {\n"
"  color: #7e7e7d;\n"
"  border: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"#btn_home_5:checked {\n"
"  color: white;\n"
"}\n"
"\n"
"")
        self.btn_menu_muddati_otgan_kitoblar2.setIcon(icon6)
        self.btn_menu_muddati_otgan_kitoblar2.setIconSize(QSize(40, 30))
        self.btn_menu_muddati_otgan_kitoblar2.setCheckable(True)
        self.btn_menu_muddati_otgan_kitoblar2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_menu_muddati_otgan_kitoblar2)

        self.verticalSpacer_2 = QSpacerItem(20, 326, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addWidget(self.chap_kichik_menu, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(701, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 0))
        self.widget.setMaximumSize(QSize(400, 16777215))
        self.widget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(100, 111, 255);\n"
"color:white;\n"
"font-size:14px;\n"
"}\n"
"QPushButton {\n"
"background-color: #ff4736;\n"
"\n"
"}\n"
"QLineEdit {\n"
"border:none;\n"
"border-bottom-style:solid;\n"
"border-bottom-color:white;\n"
"border-bottom-width:2px;\n"
"	color: black;\n"
"}\n"
"#kitob_ozgartirish,#kitob_kiritish,#kitob_ochirish{\n"
"border-radius:7px;\n"
"padding:5px 0;\n"
"width:60px;\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.kitob_orqaga = QPushButton(self.widget)
        self.kitob_orqaga.setObjectName(u"kitob_orqaga")

        self.gridLayout_5.addWidget(self.kitob_orqaga, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(20, 100, 20, 50)
        self.kirit_kitob_muallifi = QLineEdit(self.widget)
        self.kirit_kitob_muallifi.setObjectName(u"kirit_kitob_muallifi")

        self.gridLayout_4.addWidget(self.kirit_kitob_muallifi, 3, 1, 1, 1)

        self.kirit_kitob_nomi = QLineEdit(self.widget)
        self.kirit_kitob_nomi.setObjectName(u"kirit_kitob_nomi")

        self.gridLayout_4.addWidget(self.kirit_kitob_nomi, 1, 1, 1, 1)

        self.kirit_kitob_soni = QLineEdit(self.widget)
        self.kirit_kitob_soni.setObjectName(u"kirit_kitob_soni")

        self.gridLayout_4.addWidget(self.kirit_kitob_soni, 5, 1, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 4, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(25, 25))
        self.label_5.setMaximumSize(QSize(25, 25))
        self.label_5.setPixmap(QPixmap(u":/img/rasmlar/library_books_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(25, 25))
        self.label_6.setMaximumSize(QSize(25, 25))
        self.label_6.setPixmap(QPixmap(u":/img/rasmlar/menu_book_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24 (1).png"))
        self.label_6.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(25, 25))
        self.label_8.setMaximumSize(QSize(25, 25))
        self.label_8.setPixmap(QPixmap(u":/img/rasmlar/import_contacts_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24 (1).png"))
        self.label_8.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_8, 5, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, 8)
        self.kitob_ozgartirish = QPushButton(self.widget)
        self.kitob_ozgartirish.setObjectName(u"kitob_ozgartirish")

        self.horizontalLayout_3.addWidget(self.kitob_ozgartirish)

        self.kitob_kiritish = QPushButton(self.widget)
        self.kitob_kiritish.setObjectName(u"kitob_kiritish")

        self.horizontalLayout_3.addWidget(self.kitob_kiritish)

        self.kitob_ochirish = QPushButton(self.widget)
        self.kitob_ochirish.setObjectName(u"kitob_ochirish")

        self.horizontalLayout_3.addWidget(self.kitob_ochirish)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(100, 111, 255);\n"
"width:70px;\n"
"height:20px;\n"
"}\n"
"#lbl_sarlavha{\n"
"color:red;\n"
"font-size:20px;\n"
"font-weight:600;\n"
"}\n"
"#lbl_chiziq{\n"
"border:none;\n"
"border-bottom-color:red;\n"
"border-bottom-style:solid;\n"
"border-bottom-width:10px;\n"
"}\n"
"QTableWidget {\n"
"margin: 20px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal{\n"
"	background-color: rgb(100, 111, 255);\n"
"	color:white;\n"
"	font-weight:700;\n"
"}\n"
"QHeaderView::section:vertical{\n"
"	background-color: rgb(100, 111, 255);\n"
"	color:white;\n"
"	font-weight:700;\n"
"}\n"
"QTableWidget::item:selected {\n"
"	background-color: rgb(100, 111, 255);\n"
"	color:white;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.kitob_chiqish = QPushButton(self.widget_2)
        self.kitob_chiqish.setObjectName(u"kitob_chiqish")
        icon8 = QIcon()
        icon8.addFile(u":/img/rasmlar/backspace_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.kitob_chiqish.setIcon(icon8)
        self.kitob_chiqish.setIconSize(QSize(50, 40))

        self.horizontalLayout_4.addWidget(self.kitob_chiqish)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, 40)
        self.horizontalSpacer_5 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setVerticalSpacing(10)
        self.lbl_chiziq = QLabel(self.widget_2)
        self.lbl_chiziq.setObjectName(u"lbl_chiziq")
        self.lbl_chiziq.setMaximumSize(QSize(16777215, 4))

        self.gridLayout_6.addWidget(self.lbl_chiziq, 1, 0, 1, 4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 30))
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setPixmap(QPixmap(u":/img/rasmlar/book_5_24dp_EA3323_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_10.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_10, 0, 1, 1, 1)

        self.lbl_sarlavha = QLabel(self.widget_2)
        self.lbl_sarlavha.setObjectName(u"lbl_sarlavha")

        self.gridLayout_6.addWidget(self.lbl_sarlavha, 0, 2, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_6)

        self.horizontalSpacer_6 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_10 = QHBoxLayout(self.page_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(400, 0))
        self.widget_3.setMaximumSize(QSize(400, 16777215))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"background-color: rgb(100, 111, 255);\n"
"color:white;\n"
"font-size:14px;\n"
"}\n"
"QPushButton {\n"
"background-color: #ff4736;\n"
"\n"
"}\n"
"QLineEdit {\n"
"border:none;\n"
"border-bottom-style:solid;\n"
"border-bottom-color:white;\n"
"border-bottom-width:2px;\n"
"	color: black;\n"
"}\n"
"#talaba_ozgartirish,#talaba_kiritish,#talaba_ochirish{\n"
"border-radius:7px;\n"
"padding:5px 0;\n"
"width:60px;\n"
"}\n"
"QComboBox{\n"
"	border:none;\n"
"	border-bottom:2px solid white;\n"
"	padding:5px 0;\n"
"}\n"
"QComboBox::drop-down{\n"
"	width:20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	border:2px solid white;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: #646fff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.talaba_orqaga = QPushButton(self.widget_3)
        self.talaba_orqaga.setObjectName(u"talaba_orqaga")
        icon9 = QIcon()
        icon9.addFile(u":/img/rasmlar/keyboard_double_arrow_left_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.talaba_orqaga.setIcon(icon9)
        self.talaba_orqaga.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.talaba_orqaga, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(15)
        self.gridLayout_8.setContentsMargins(20, 100, 20, 50)
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 2, 1, 1, 1)

        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(25, 25))
        self.label_14.setMaximumSize(QSize(25, 25))
        self.label_14.setPixmap(QPixmap(u":/img/rasmlar/account_circle_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_14.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(25, 25))
        self.label_15.setMaximumSize(QSize(25, 25))
        self.label_15.setPixmap(QPixmap(u":/img/rasmlar/demography_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_15.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_15, 3, 0, 1, 1)

        self.kirit_talaba_ismi = QLineEdit(self.widget_3)
        self.kirit_talaba_ismi.setObjectName(u"kirit_talaba_ismi")

        self.gridLayout_8.addWidget(self.kirit_talaba_ismi, 1, 1, 1, 1)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 0, 1, 1, 1)

        self.talaba_kursi = QComboBox(self.widget_3)
        self.talaba_kursi.addItem("")
        self.talaba_kursi.addItem("")
        self.talaba_kursi.addItem("")
        self.talaba_kursi.setObjectName(u"talaba_kursi")

        self.gridLayout_8.addWidget(self.talaba_kursi, 3, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 0, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, 8)
        self.talaba_ozgartirish = QPushButton(self.widget_3)
        self.talaba_ozgartirish.setObjectName(u"talaba_ozgartirish")

        self.horizontalLayout_6.addWidget(self.talaba_ozgartirish)

        self.talaba_kiritish = QPushButton(self.widget_3)
        self.talaba_kiritish.setObjectName(u"talaba_kiritish")

        self.horizontalLayout_6.addWidget(self.talaba_kiritish)

        self.talaba_ochirish = QPushButton(self.widget_3)
        self.talaba_ochirish.setObjectName(u"talaba_ochirish")

        self.horizontalLayout_6.addWidget(self.talaba_ochirish)


        self.gridLayout_7.addLayout(self.horizontalLayout_6, 2, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(100, 111, 255);\n"
"width:70px;\n"
"height:20px;\n"
"}\n"
"#lbl_talaba_sarlavha{\n"
"color:red;\n"
"font-size:20px;\n"
"font-weight:600;\n"
"}\n"
"#lbl_talaba_chiziq{\n"
"border:none;\n"
"border-bottom-color:red;\n"
"border-bottom-style:solid;\n"
"border-bottom-width:10px;\n"
"}\n"
"QTableWidget {\n"
"margin: 20px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal{\n"
"	background-color: rgb(100, 111, 255);\n"
"	color:white;\n"
"	font-weight:700;\n"
"}\n"
"QHeaderView::section:vertical{\n"
"	background-color: rgb(100, 111, 255);\n"
"	color:white;\n"
"	font-weight:700;\n"
"}\n"
"QTableWidget::item:selected {\n"
"	background-color: rgb(100, 111, 255);\n"
"	color:white;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_10 = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.talaba_chiqish = QPushButton(self.widget_4)
        self.talaba_chiqish.setObjectName(u"talaba_chiqish")
        self.talaba_chiqish.setIcon(icon8)
        self.talaba_chiqish.setIconSize(QSize(50, 40))

        self.horizontalLayout_7.addWidget(self.talaba_chiqish)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 20, -1, 40)
        self.horizontalSpacer_11 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(10)
        self.lbl_chiziq_2 = QLabel(self.widget_4)
        self.lbl_chiziq_2.setObjectName(u"lbl_chiziq_2")
        self.lbl_chiziq_2.setMaximumSize(QSize(16777215, 4))

        self.gridLayout_9.addWidget(self.lbl_chiziq_2, 1, 0, 1, 4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.label_17 = QLabel(self.widget_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(30, 30))
        self.label_17.setMaximumSize(QSize(30, 30))
        self.label_17.setPixmap(QPixmap(u":/img/rasmlar/school_24dp_EA3323_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_17.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_17, 0, 1, 1, 1)

        self.lbl_talaba_sarlavha = QLabel(self.widget_4)
        self.lbl_talaba_sarlavha.setObjectName(u"lbl_talaba_sarlavha")

        self.gridLayout_9.addWidget(self.lbl_talaba_sarlavha, 0, 2, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_9)

        self.horizontalSpacer_14 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.tbl_talabalar = QTableWidget(self.widget_4)
        self.tbl_talabalar.setObjectName(u"tbl_talabalar")

        self.verticalLayout_4.addWidget(self.tbl_talabalar)


        self.horizontalLayout_10.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_11 = QHBoxLayout(self.page_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_talabani_qidirish = QWidget(self.page_4)
        self.widget_talabani_qidirish.setObjectName(u"widget_talabani_qidirish")
        self.widget_talabani_qidirish.setStyleSheet(u"QWidget{\n"
"	color:white;\n"
"	font-size:15px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"#lbl_chiziq_8{\n"
"border:none;\n"
"border-bottom-color:white;\n"
"border-bottom-style:solid;\n"
"border-bottom-width:10px;\n"
"}\n"
"#edt_talaba_qidirish{\n"
"	border-color:white;\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	padding:5px;\n"
"}\n"
"#lbl_talaba_sarlavha_4{\n"
"font-size:16px;\n"
"font-weight:700;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_talabani_qidirish)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_orqaga_kitob_berish = QPushButton(self.widget_talabani_qidirish)
        self.btn_orqaga_kitob_berish.setObjectName(u"btn_orqaga_kitob_berish")
        self.btn_orqaga_kitob_berish.setStyleSheet(u"width:70px;\n"
"height:30px;\n"
"border-radius:0;\n"
"background-color: rgb(100, 111, 255);")
        self.btn_orqaga_kitob_berish.setIcon(icon9)
        self.btn_orqaga_kitob_berish.setIconSize(QSize(20, 20))

        self.horizontalLayout_21.addWidget(self.btn_orqaga_kitob_berish)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_33)


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(40)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(70, 20, 70, 40)
        self.horizontalSpacer_41 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_41)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(20)
        self.gridLayout_21.setVerticalSpacing(10)
        self.lbl_chiziq_8 = QLabel(self.widget_talabani_qidirish)
        self.lbl_chiziq_8.setObjectName(u"lbl_chiziq_8")
        self.lbl_chiziq_8.setMaximumSize(QSize(16777215, 4))

        self.gridLayout_21.addWidget(self.lbl_chiziq_8, 1, 0, 1, 4)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_42, 0, 3, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_43, 0, 0, 1, 1)

        self.label_34 = QLabel(self.widget_talabani_qidirish)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(30, 30))
        self.label_34.setMaximumSize(QSize(30, 30))
        self.label_34.setPixmap(QPixmap(u":/img/rasmlar/school_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_34.setScaledContents(True)

        self.gridLayout_21.addWidget(self.label_34, 0, 1, 1, 1)

        self.lbl_talaba_sarlavha_4 = QLabel(self.widget_talabani_qidirish)
        self.lbl_talaba_sarlavha_4.setObjectName(u"lbl_talaba_sarlavha_4")

        self.gridLayout_21.addWidget(self.lbl_talaba_sarlavha_4, 0, 2, 1, 1)


        self.horizontalLayout_23.addLayout(self.gridLayout_21)

        self.horizontalSpacer_44 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_44)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.edt_talaba_qidirish = QLineEdit(self.widget_talabani_qidirish)
        self.edt_talaba_qidirish.setObjectName(u"edt_talaba_qidirish")

        self.verticalLayout_9.addWidget(self.edt_talaba_qidirish)

        self.tbl_talaba_qidirish = QTableWidget(self.widget_talabani_qidirish)
        self.tbl_talaba_qidirish.setObjectName(u"tbl_talaba_qidirish")

        self.verticalLayout_9.addWidget(self.tbl_talaba_qidirish)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)


        self.horizontalLayout_11.addWidget(self.widget_talabani_qidirish)

        self.widget_kitobni_qidirish = QWidget(self.page_4)
        self.widget_kitobni_qidirish.setObjectName(u"widget_kitobni_qidirish")
        self.widget_kitobni_qidirish.setStyleSheet(u"QWidget{\n"
"	color:white;\n"
"	font-size:15px;\n"
"	background-color: #646fff;\n"
"}\n"
"#lbl_chiziq_9{\n"
"border:none;\n"
"border-bottom-color:white;\n"
"border-bottom-style:solid;\n"
"border-bottom-width:10px;\n"
"}\n"
"#edt_kitob_qidirish{\n"
"	border-color:white;\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	padding:5px;\n"
"}\n"
"#lbl_talaba_sarlavha_5{\n"
"font-size:16px;\n"
"font-weight:700;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.widget_kitobni_qidirish)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(40)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 40, 20, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(70, 20, 70, 40)
        self.horizontalSpacer_45 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_45)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(20)
        self.gridLayout_22.setVerticalSpacing(10)
        self.lbl_chiziq_9 = QLabel(self.widget_kitobni_qidirish)
        self.lbl_chiziq_9.setObjectName(u"lbl_chiziq_9")
        self.lbl_chiziq_9.setMaximumSize(QSize(16777215, 4))

        self.gridLayout_22.addWidget(self.lbl_chiziq_9, 1, 0, 1, 4)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_46, 0, 3, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_47, 0, 0, 1, 1)

        self.label_35 = QLabel(self.widget_kitobni_qidirish)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(30, 30))
        self.label_35.setMaximumSize(QSize(30, 30))
        self.label_35.setPixmap(QPixmap(u":/img/rasmlar/book_2_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_35.setScaledContents(True)

        self.gridLayout_22.addWidget(self.label_35, 0, 1, 1, 1)

        self.lbl_talaba_sarlavha_6 = QLabel(self.widget_kitobni_qidirish)
        self.lbl_talaba_sarlavha_6.setObjectName(u"lbl_talaba_sarlavha_6")

        self.gridLayout_22.addWidget(self.lbl_talaba_sarlavha_6, 0, 2, 1, 1)


        self.horizontalLayout_25.addLayout(self.gridLayout_22)

        self.horizontalSpacer_48 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_48)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.edt_kitob_qidirish = QLineEdit(self.widget_kitobni_qidirish)
        self.edt_kitob_qidirish.setObjectName(u"edt_kitob_qidirish")

        self.verticalLayout_12.addWidget(self.edt_kitob_qidirish)

        self.tbl_kitob_qidirish = QTableWidget(self.widget_kitobni_qidirish)
        self.tbl_kitob_qidirish.setObjectName(u"tbl_kitob_qidirish")

        self.verticalLayout_12.addWidget(self.tbl_kitob_qidirish)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.horizontalLayout_11.addWidget(self.widget_kitobni_qidirish)

        self.widget_kitobn_berish = QWidget(self.page_4)
        self.widget_kitobn_berish.setObjectName(u"widget_kitobn_berish")
        self.widget_kitobn_berish.setStyleSheet(u"QWidget{\n"
"	color:red;\n"
"	font-size:15px;\n"
"	background-color: white;\n"
"}\n"
"#lbl_chiziq_10{\n"
"border:none;\n"
"border-bottom-color:red;\n"
"border-bottom-style:solid;\n"
"border-bottom-width:10px;\n"
"}\n"
"#edt_talaba_qidirish{\n"
"	border-color:white;\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	padding:5px;\n"
"}\n"
"#lbl_talaba_sarlavha_4{\n"
"font-size:16px;\n"
"font-weight:700;\n"
"}\n"
"\n"
"QLineEdit,QDateEdit{\n"
"padding:5px;\n"
"}\n"
"#btn_kitob_berish{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	padding:10px;\n"
"	border-radius:5px;\n"
"	font-size:16px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_kitobn_berish)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_34)

        self.talaba_orqaga_4 = QPushButton(self.widget_kitobn_berish)
        self.talaba_orqaga_4.setObjectName(u"talaba_orqaga_4")
        self.talaba_orqaga_4.setStyleSheet(u"width:70px;\n"
"height:30px;\n"
"border-radius:0;\n"
"background-color: rgb(100, 111, 255);")
        self.talaba_orqaga_4.setIcon(icon1)
        self.talaba_orqaga_4.setIconSize(QSize(50, 40))

        self.horizontalLayout_24.addWidget(self.talaba_orqaga_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_24)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(70, 20, 70, 40)
        self.horizontalSpacer_49 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_49)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setHorizontalSpacing(20)
        self.gridLayout_23.setVerticalSpacing(10)
        self.lbl_chiziq_10 = QLabel(self.widget_kitobn_berish)
        self.lbl_chiziq_10.setObjectName(u"lbl_chiziq_10")
        self.lbl_chiziq_10.setMaximumSize(QSize(16777215, 4))

        self.gridLayout_23.addWidget(self.lbl_chiziq_10, 1, 0, 1, 4)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_50, 0, 3, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_51, 0, 0, 1, 1)

        self.label_36 = QLabel(self.widget_kitobn_berish)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(30, 30))
        self.label_36.setMaximumSize(QSize(30, 30))
        self.label_36.setPixmap(QPixmap(u":/img/rasmlar/collections_bookmark_24dp_EA3323_FILL0_wght400_GRAD0_opsz24.png"))
        self.label_36.setScaledContents(True)

        self.gridLayout_23.addWidget(self.label_36, 0, 1, 1, 1)

        self.lbl_talaba_sarlavha_7 = QLabel(self.widget_kitobn_berish)
        self.lbl_talaba_sarlavha_7.setObjectName(u"lbl_talaba_sarlavha_7")

        self.gridLayout_23.addWidget(self.lbl_talaba_sarlavha_7, 0, 2, 1, 1)


        self.horizontalLayout_26.addLayout(self.gridLayout_23)

        self.horizontalSpacer_52 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_52)


        self.verticalLayout_5.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_5 = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_38 = QLabel(self.widget_kitobn_berish)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout.addWidget(self.label_38, 2, 0, 1, 2)

        self.dt_olinadigan = QDateEdit(self.widget_kitobn_berish)
        self.dt_olinadigan.setObjectName(u"dt_olinadigan")
        self.dt_olinadigan.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dt_olinadigan, 2, 2, 1, 1)

        self.label_39 = QLabel(self.widget_kitobn_berish)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 3, 0, 1, 2)

        self.dt_beriladigan = QDateEdit(self.widget_kitobn_berish)
        self.dt_beriladigan.setObjectName(u"dt_beriladigan")
        self.dt_beriladigan.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dt_beriladigan, 3, 2, 1, 1)

        self.edt_kitob_oluvchi = QLineEdit(self.widget_kitobn_berish)
        self.edt_kitob_oluvchi.setObjectName(u"edt_kitob_oluvchi")

        self.gridLayout.addWidget(self.edt_kitob_oluvchi, 0, 2, 1, 1)

        self.label_32 = QLabel(self.widget_kitobn_berish)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 0, 0, 1, 2)

        self.edt_olinadigan_kitob = QLineEdit(self.widget_kitobn_berish)
        self.edt_olinadigan_kitob.setObjectName(u"edt_olinadigan_kitob")

        self.gridLayout.addWidget(self.edt_olinadigan_kitob, 1, 2, 1, 1)

        self.label_37 = QLabel(self.widget_kitobn_berish)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout.addWidget(self.label_37, 1, 0, 1, 2)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 148, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.btn_kitob_berish = QPushButton(self.widget_kitobn_berish)
        self.btn_kitob_berish.setObjectName(u"btn_kitob_berish")

        self.verticalLayout_5.addWidget(self.btn_kitob_berish)

        self.verticalSpacer_7 = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_11.addWidget(self.widget_kitobn_berish)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_9.addWidget(self.stackedWidget)


        self.retranslateUi(Form)
        self.btn_menu.toggled.connect(self.chap_menu.setHidden)
        self.btn_menu.toggled.connect(self.chap_kichik_menu.setVisible)
        self.btn_asosiy_sahifa.clicked.connect(self.btn_asosiy_sahifa2.click)
        self.btn_menu_kitoblar.clicked.connect(self.btn_menu_kitoblar2.click)
        self.btn_menu_talabalar.clicked.connect(self.btn_menu_talabalar2.click)
        self.btn_menu_olingan_kitoblar.clicked.connect(self.btn_menu_olingan_kitoblar2.click)
        self.btn_menu_muddati_otgan_kitoblar.clicked.connect(self.btn_menu_muddati_otgan_kitoblar2.click)
        self.btn_menu_chiqish.clicked.connect(self.chap_menu.close)
        self.btn_menu_ochirish.clicked.connect(self.stackedWidget.close)
        self.kitob_chiqish.clicked.connect(Form.close)
        self.btn_menu_ochirish.clicked.connect(Form.close)
        self.btn_menu_chiqish.clicked.connect(Form.close)
        self.talaba_chiqish.clicked.connect(Form.close)
        self.talaba_orqaga_4.clicked.connect(Form.close)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_menu.setText(QCoreApplication.translate("Form", u"...", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kutubxona boshqaruv tizimi", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Otabek, xush kelibsiz", None))
        self.btn_menu_ochirish.setText(QCoreApplication.translate("Form", u"...", None))
        self.btn_asosiy_sahifa.setText(QCoreApplication.translate("Form", u"Asosiy sahifa", None))
        self.btn_menu_kitoblar.setText(QCoreApplication.translate("Form", u"Kitoblar   ", None))
        self.btn_menu_talabalar.setText(QCoreApplication.translate("Form", u"Talabalar      ", None))
        self.btn_menu_olingan_kitoblar.setText(QCoreApplication.translate("Form", u"Olingan kitoblar", None))
        self.btn_menu_muddati_otgan_kitoblar.setText(QCoreApplication.translate("Form", u"Muddati o'tgan kitoblar", None))
        self.btn_menu_chiqish.setText(QCoreApplication.translate("Form", u"Chiqish", None))
        self.btn_asosiy_sahifa2.setText("")
        self.btn_menu_kitoblar2.setText("")
        self.btn_menu_talabalar2.setText("")
        self.btn_menu_olingan_kitoblar2.setText("")
        self.btn_menu_muddati_otgan_kitoblar2.setText("")
        self.kitob_orqaga.setText(QCoreApplication.translate("Form", u"Orqaga", None))
        self.kirit_kitob_muallifi.setPlaceholderText(QCoreApplication.translate("Form", u"Muallifi", None))
        self.kirit_kitob_nomi.setPlaceholderText(QCoreApplication.translate("Form", u"Kitob nomi", None))
        self.kirit_kitob_soni.setPlaceholderText(QCoreApplication.translate("Form", u"Soni", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Kitob soni", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Kitob muallifi", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Kitob nomi", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        self.kitob_ozgartirish.setText(QCoreApplication.translate("Form", u"O'zgartirish", None))
        self.kitob_kiritish.setText(QCoreApplication.translate("Form", u"Kiritish", None))
        self.kitob_ochirish.setText(QCoreApplication.translate("Form", u"O'chirish", None))
        self.kitob_chiqish.setText("")
        self.lbl_chiziq.setText("")
        self.label_10.setText("")
        self.lbl_sarlavha.setText(QCoreApplication.translate("Form", u"Kitoblar bo'limi", None))
        self.talaba_orqaga.setText(QCoreApplication.translate("Form", u"Orqaga", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Kursi nomi", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.kirit_talaba_ismi.setPlaceholderText(QCoreApplication.translate("Form", u"Talaba ismi", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Talaba ismi", None))
        self.talaba_kursi.setItemText(0, QCoreApplication.translate("Form", u"Python", None))
        self.talaba_kursi.setItemText(1, QCoreApplication.translate("Form", u"Flutter", None))
        self.talaba_kursi.setItemText(2, QCoreApplication.translate("Form", u"C++", None))

        self.talaba_ozgartirish.setText(QCoreApplication.translate("Form", u"O'zgartirish", None))
        self.talaba_kiritish.setText(QCoreApplication.translate("Form", u"Kiritish", None))
        self.talaba_ochirish.setText(QCoreApplication.translate("Form", u"O'chirish", None))
        self.talaba_chiqish.setText("")
        self.lbl_chiziq_2.setText("")
        self.label_17.setText("")
        self.lbl_talaba_sarlavha.setText(QCoreApplication.translate("Form", u"Talabalar bo'limi", None))
        self.btn_orqaga_kitob_berish.setText(QCoreApplication.translate("Form", u"Orqaga", None))
        self.lbl_chiziq_8.setText("")
        self.label_34.setText("")
        self.lbl_talaba_sarlavha_4.setText(QCoreApplication.translate("Form", u"Talabalar", None))
        self.edt_talaba_qidirish.setPlaceholderText(QCoreApplication.translate("Form", u"Talabani qidirish", None))
        self.lbl_chiziq_9.setText("")
        self.label_35.setText("")
        self.lbl_talaba_sarlavha_6.setText(QCoreApplication.translate("Form", u"Kitoblar", None))
        self.edt_kitob_qidirish.setPlaceholderText(QCoreApplication.translate("Form", u"Kitobni qidirish", None))
        self.talaba_orqaga_4.setText("")
        self.lbl_chiziq_10.setText("")
        self.label_36.setText("")
        self.lbl_talaba_sarlavha_7.setText(QCoreApplication.translate("Form", u"Kitobni berish", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Olingan", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Qaytariladi", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Talaba", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Kitob", None))
        self.btn_kitob_berish.setText(QCoreApplication.translate("Form", u"Kitob berish", None))
    # retranslateUi

