# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(343, 509)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.todoView = QListView(self.centralwidget)
        self.todoView.setObjectName(u"todoView")

        self.verticalLayout.addWidget(self.todoView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.completeButton = QPushButton(self.centralwidget)
        self.completeButton.setObjectName(u"completeButton")

        self.horizontalLayout.addWidget(self.completeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.todoEdit = QLineEdit(self.centralwidget)
        self.todoEdit.setObjectName(u"todoEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todoEdit.sizePolicy().hasHeightForWidth())
        self.todoEdit.setSizePolicy(sizePolicy)
        self.todoEdit.setMinimumSize(QSize(0, 38))

        self.verticalLayout.addWidget(self.todoEdit)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 343, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.completeButton.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add todo", None))
    # retranslateUi

