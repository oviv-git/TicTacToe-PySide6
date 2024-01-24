# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(700, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(700, 760))
        Widget.setBaseSize(QSize(960, 540))
        Widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.menuTab = QWidget()
        self.menuTab.setObjectName(u"menuTab")
        self.verticalLayout = QVBoxLayout(self.menuTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameLogo = QLabel(self.menuTab)
        self.gameLogo.setObjectName(u"gameLogo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gameLogo.sizePolicy().hasHeightForWidth())
        self.gameLogo.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Elephant"])
        font.setPointSize(64)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.gameLogo.setFont(font)

        self.verticalLayout.addWidget(self.gameLogo, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gameResultsLabel = QLabel(self.menuTab)
        self.gameResultsLabel.setObjectName(u"gameResultsLabel")
        font1 = QFont()
        font1.setPointSize(20)
        self.gameResultsLabel.setFont(font1)

        self.verticalLayout.addWidget(self.gameResultsLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.infoVLayout = QVBoxLayout()
        self.infoVLayout.setObjectName(u"infoVLayout")
        self.infoVLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.infoHLayout = QHBoxLayout()
        self.infoHLayout.setObjectName(u"infoHLayout")
        self.infoHLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.infoLeftHLayout = QVBoxLayout()
        self.infoLeftHLayout.setObjectName(u"infoLeftHLayout")
        self.infoTopLeftHLayout = QHBoxLayout()
        self.infoTopLeftHLayout.setObjectName(u"infoTopLeftHLayout")
        self.infoTopLeftHLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.player_1Selection = QComboBox(self.menuTab)
        self.player_1Selection.addItem("")
        self.player_1Selection.addItem("")
        self.player_1Selection.setObjectName(u"player_1Selection")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.player_1Selection.sizePolicy().hasHeightForWidth())
        self.player_1Selection.setSizePolicy(sizePolicy2)
        self.player_1Selection.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setPointSize(14)
        self.player_1Selection.setFont(font2)

        self.infoTopLeftHLayout.addWidget(self.player_1Selection, 0, Qt.AlignHCenter)

        self.player_1Score = QLabel(self.menuTab)
        self.player_1Score.setObjectName(u"player_1Score")
        font3 = QFont()
        font3.setPointSize(24)
        self.player_1Score.setFont(font3)

        self.infoTopLeftHLayout.addWidget(self.player_1Score, 0, Qt.AlignLeft)

        self.infoTopLeftHLayout.setStretch(0, 5)
        self.infoTopLeftHLayout.setStretch(1, 1)

        self.infoLeftHLayout.addLayout(self.infoTopLeftHLayout)


        self.infoHLayout.addLayout(self.infoLeftHLayout)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.infoHLayout.addItem(self.horizontalSpacer)

        self.infoRightHLayout = QVBoxLayout()
        self.infoRightHLayout.setObjectName(u"infoRightHLayout")
        self.infoTopRightHLayout = QHBoxLayout()
        self.infoTopRightHLayout.setObjectName(u"infoTopRightHLayout")
        self.infoTopRightHLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.player_2Selection = QComboBox(self.menuTab)
        self.player_2Selection.addItem("")
        self.player_2Selection.addItem("")
        self.player_2Selection.setObjectName(u"player_2Selection")
        sizePolicy2.setHeightForWidth(self.player_2Selection.sizePolicy().hasHeightForWidth())
        self.player_2Selection.setSizePolicy(sizePolicy2)
        self.player_2Selection.setMinimumSize(QSize(250, 0))
        self.player_2Selection.setFont(font2)

        self.infoTopRightHLayout.addWidget(self.player_2Selection, 0, Qt.AlignHCenter)

        self.player_2Score = QLabel(self.menuTab)
        self.player_2Score.setObjectName(u"player_2Score")
        self.player_2Score.setFont(font3)

        self.infoTopRightHLayout.addWidget(self.player_2Score, 0, Qt.AlignLeft)

        self.infoTopRightHLayout.setStretch(0, 5)
        self.infoTopRightHLayout.setStretch(1, 1)

        self.infoRightHLayout.addLayout(self.infoTopRightHLayout)


        self.infoHLayout.addLayout(self.infoRightHLayout)

        self.infoHLayout.setStretch(0, 4)
        self.infoHLayout.setStretch(1, 1)
        self.infoHLayout.setStretch(2, 4)

        self.infoVLayout.addLayout(self.infoHLayout)


        self.verticalLayout.addLayout(self.infoVLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.startGameButton = QPushButton(self.menuTab)
        self.startGameButton.setObjectName(u"startGameButton")
        sizePolicy1.setHeightForWidth(self.startGameButton.sizePolicy().hasHeightForWidth())
        self.startGameButton.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Segoe Fluent Icons"])
        font4.setPointSize(32)
        self.startGameButton.setFont(font4)

        self.verticalLayout_2.addWidget(self.startGameButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.tabWidget.addTab(self.menuTab, "")
        self.gameTab = QWidget()
        self.gameTab.setObjectName(u"gameTab")
        self.verticalLayout_5 = QVBoxLayout(self.gameTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(16, 0, 16, 48)
        self.gameInfoLayout = QHBoxLayout()
        self.gameInfoLayout.setObjectName(u"gameInfoLayout")
        self.gameLabel_1 = QLabel(self.gameTab)
        self.gameLabel_1.setObjectName(u"gameLabel_1")
        self.gameLabel_1.setFont(font1)

        self.gameInfoLayout.addWidget(self.gameLabel_1, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gameInfoLayout.addItem(self.horizontalSpacer_3)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gameInfoLayout.addItem(self.verticalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gameInfoLayout.addItem(self.horizontalSpacer_2)

        self.gameLabel_2 = QLabel(self.gameTab)
        self.gameLabel_2.setObjectName(u"gameLabel_2")
        self.gameLabel_2.setFont(font1)

        self.gameInfoLayout.addWidget(self.gameLabel_2, 0, Qt.AlignRight)

        self.gameInfoLayout.setStretch(0, 2)
        self.gameInfoLayout.setStretch(1, 1)
        self.gameInfoLayout.setStretch(3, 1)
        self.gameInfoLayout.setStretch(4, 2)

        self.verticalLayout_5.addLayout(self.gameInfoLayout)

        self.boardGrid = QGridLayout()
        self.boardGrid.setSpacing(0)
        self.boardGrid.setObjectName(u"boardGrid")
        self.rowHLayout_1 = QHBoxLayout()
        self.rowHLayout_1.setObjectName(u"rowHLayout_1")
        self.tile_1 = QPushButton(self.gameTab)
        self.tile_1.setObjectName(u"tile_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tile_1.sizePolicy().hasHeightForWidth())
        self.tile_1.setSizePolicy(sizePolicy3)
        self.tile_1.setMinimumSize(QSize(200, 200))
        self.tile_1.setMaximumSize(QSize(200, 200))
        self.tile_1.setSizeIncrement(QSize(10, 10))
        self.tile_1.setBaseSize(QSize(200, 200))
        font5 = QFont()
        font5.setFamilies([u"Gill Sans MT"])
        font5.setPointSize(84)
        font5.setBold(False)
        self.tile_1.setFont(font5)

        self.rowHLayout_1.addWidget(self.tile_1)

        self.tile_2 = QPushButton(self.gameTab)
        self.tile_2.setObjectName(u"tile_2")
        sizePolicy3.setHeightForWidth(self.tile_2.sizePolicy().hasHeightForWidth())
        self.tile_2.setSizePolicy(sizePolicy3)
        self.tile_2.setMinimumSize(QSize(200, 200))
        self.tile_2.setMaximumSize(QSize(200, 200))
        self.tile_2.setSizeIncrement(QSize(10, 10))
        self.tile_2.setBaseSize(QSize(200, 200))
        self.tile_2.setFont(font5)

        self.rowHLayout_1.addWidget(self.tile_2)

        self.tile_3 = QPushButton(self.gameTab)
        self.tile_3.setObjectName(u"tile_3")
        sizePolicy3.setHeightForWidth(self.tile_3.sizePolicy().hasHeightForWidth())
        self.tile_3.setSizePolicy(sizePolicy3)
        self.tile_3.setMinimumSize(QSize(200, 200))
        self.tile_3.setMaximumSize(QSize(200, 200))
        self.tile_3.setSizeIncrement(QSize(10, 10))
        self.tile_3.setBaseSize(QSize(200, 200))
        self.tile_3.setFont(font5)

        self.rowHLayout_1.addWidget(self.tile_3)


        self.boardGrid.addLayout(self.rowHLayout_1, 0, 0, 1, 1)

        self.rowHLayout_3 = QHBoxLayout()
        self.rowHLayout_3.setObjectName(u"rowHLayout_3")
        self.tile_7 = QPushButton(self.gameTab)
        self.tile_7.setObjectName(u"tile_7")
        sizePolicy3.setHeightForWidth(self.tile_7.sizePolicy().hasHeightForWidth())
        self.tile_7.setSizePolicy(sizePolicy3)
        self.tile_7.setMinimumSize(QSize(200, 200))
        self.tile_7.setMaximumSize(QSize(200, 200))
        self.tile_7.setSizeIncrement(QSize(10, 10))
        self.tile_7.setBaseSize(QSize(200, 200))
        self.tile_7.setFont(font5)

        self.rowHLayout_3.addWidget(self.tile_7)

        self.tile_8 = QPushButton(self.gameTab)
        self.tile_8.setObjectName(u"tile_8")
        sizePolicy3.setHeightForWidth(self.tile_8.sizePolicy().hasHeightForWidth())
        self.tile_8.setSizePolicy(sizePolicy3)
        self.tile_8.setMinimumSize(QSize(200, 200))
        self.tile_8.setMaximumSize(QSize(200, 200))
        self.tile_8.setSizeIncrement(QSize(10, 10))
        self.tile_8.setBaseSize(QSize(200, 200))
        self.tile_8.setFont(font5)

        self.rowHLayout_3.addWidget(self.tile_8)

        self.tile_9 = QPushButton(self.gameTab)
        self.tile_9.setObjectName(u"tile_9")
        sizePolicy3.setHeightForWidth(self.tile_9.sizePolicy().hasHeightForWidth())
        self.tile_9.setSizePolicy(sizePolicy3)
        self.tile_9.setMinimumSize(QSize(200, 200))
        self.tile_9.setMaximumSize(QSize(200, 200))
        self.tile_9.setSizeIncrement(QSize(10, 10))
        self.tile_9.setBaseSize(QSize(200, 200))
        self.tile_9.setFont(font5)

        self.rowHLayout_3.addWidget(self.tile_9)


        self.boardGrid.addLayout(self.rowHLayout_3, 2, 0, 1, 1)

        self.rowHLayout_2 = QHBoxLayout()
        self.rowHLayout_2.setObjectName(u"rowHLayout_2")
        self.tile_4 = QPushButton(self.gameTab)
        self.tile_4.setObjectName(u"tile_4")
        sizePolicy3.setHeightForWidth(self.tile_4.sizePolicy().hasHeightForWidth())
        self.tile_4.setSizePolicy(sizePolicy3)
        self.tile_4.setMinimumSize(QSize(200, 200))
        self.tile_4.setMaximumSize(QSize(200, 200))
        self.tile_4.setSizeIncrement(QSize(10, 10))
        self.tile_4.setBaseSize(QSize(200, 200))
        self.tile_4.setFont(font5)

        self.rowHLayout_2.addWidget(self.tile_4)

        self.tile_5 = QPushButton(self.gameTab)
        self.tile_5.setObjectName(u"tile_5")
        sizePolicy3.setHeightForWidth(self.tile_5.sizePolicy().hasHeightForWidth())
        self.tile_5.setSizePolicy(sizePolicy3)
        self.tile_5.setMinimumSize(QSize(200, 200))
        self.tile_5.setMaximumSize(QSize(200, 200))
        self.tile_5.setSizeIncrement(QSize(10, 10))
        self.tile_5.setBaseSize(QSize(200, 200))
        self.tile_5.setFont(font5)

        self.rowHLayout_2.addWidget(self.tile_5)

        self.tile_6 = QPushButton(self.gameTab)
        self.tile_6.setObjectName(u"tile_6")
        sizePolicy3.setHeightForWidth(self.tile_6.sizePolicy().hasHeightForWidth())
        self.tile_6.setSizePolicy(sizePolicy3)
        self.tile_6.setMinimumSize(QSize(200, 200))
        self.tile_6.setMaximumSize(QSize(200, 200))
        self.tile_6.setSizeIncrement(QSize(10, 10))
        self.tile_6.setBaseSize(QSize(200, 200))
        self.tile_6.setFont(font5)

        self.rowHLayout_2.addWidget(self.tile_6)


        self.boardGrid.addLayout(self.rowHLayout_2, 1, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.boardGrid)

        self.verticalLayout_5.setStretch(1, 3)
        self.tabWidget.addTab(self.gameTab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.gameLogo.setText(QCoreApplication.translate("Widget", u"TicTacToe", None))
        self.gameResultsLabel.setText("")
        self.player_1Selection.setItemText(0, QCoreApplication.translate("Widget", u"Human Player", None))
        self.player_1Selection.setItemText(1, QCoreApplication.translate("Widget", u"Computer Player", None))

        self.player_1Score.setText(QCoreApplication.translate("Widget", u"0", None))
        self.player_2Selection.setItemText(0, QCoreApplication.translate("Widget", u"Computer Player", None))
        self.player_2Selection.setItemText(1, QCoreApplication.translate("Widget", u"Human Player", None))

        self.player_2Score.setText(QCoreApplication.translate("Widget", u"0", None))
        self.startGameButton.setText(QCoreApplication.translate("Widget", u"Start Game", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.menuTab), QCoreApplication.translate("Widget", u"Tab 1", None))
        self.gameLabel_1.setText("")
        self.gameLabel_2.setText("")
        self.tile_1.setText("")
        self.tile_2.setText("")
        self.tile_3.setText("")
        self.tile_7.setText("")
        self.tile_8.setText("")
        self.tile_9.setText("")
        self.tile_4.setText("")
        self.tile_5.setText("")
        self.tile_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gameTab), QCoreApplication.translate("Widget", u"Tab 2", None))
    # retranslateUi

