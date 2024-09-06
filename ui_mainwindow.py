# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(639, 336)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 291, 221))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 101, 21))
        self.ytSearchInput = QLineEdit(self.groupBox)
        self.ytSearchInput.setObjectName(u"ytSearchInput")
        self.ytSearchInput.setGeometry(QRect(110, 30, 171, 22))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 121, 21))
        self.maxSearchSpinBox = QSpinBox(self.groupBox)
        self.maxSearchSpinBox.setObjectName(u"maxSearchSpinBox")
        self.maxSearchSpinBox.setGeometry(QRect(130, 90, 51, 22))
        self.maxSearchSpinBox.setMinimum(1)
        self.maxSearchSpinBox.setMaximum(1000)
        self.searchTermInput = QLineEdit(self.groupBox)
        self.searchTermInput.setObjectName(u"searchTermInput")
        self.searchTermInput.setGeometry(QRect(100, 60, 191, 22))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 60, 81, 21))
        self.searchButton = QPushButton(self.groupBox)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(10, 180, 93, 28))
        self.searchButton.setAutoExclusive(False)
        self.searchButton.setAutoDefault(True)
        self.searchButton.setFlat(False)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 270, 611, 23))
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 250, 51, 20))
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(60, 250, 561, 20))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(320, 20, 311, 211))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 639, 26))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.ytSearchInput, self.searchTermInput)
        QWidget.setTabOrder(self.searchTermInput, self.maxSearchSpinBox)
        QWidget.setTabOrder(self.maxSearchSpinBox, self.searchButton)

        self.retranslateUi(MainWindow)

        self.searchButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoOnePiece", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search Parameters", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"The tearm used to search YouTube", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"YT Search Term", None))
#if QT_CONFIG(tooltip)
        self.ytSearchInput.setToolTip(QCoreApplication.translate("MainWindow", u"The tearm used to search YouTube", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"The maximum ammount of videos to be searched", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max. search Videos", None))
#if QT_CONFIG(tooltip)
        self.maxSearchSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"The maximum ammount of videos to be searched", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.searchTermInput.setToolTip(QCoreApplication.translate("MainWindow", u"The term to be searched in the Video", None))
#endif // QT_CONFIG(tooltip)
        self.searchTermInput.setText(QCoreApplication.translate("MainWindow", u"One piece", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"The term to be searched in the Video", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Search Term", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statusLabel.setText("")
    # retranslateUi

