# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_SchedulerManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(907, 610)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(400, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ClearOutputBoxButton = QtWidgets.QPushButton(self.frame)
        self.ClearOutputBoxButton.setGeometry(QtCore.QRect(480, 0, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearOutputBoxButton.sizePolicy().hasHeightForWidth())
        self.ClearOutputBoxButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ClearOutputBoxButton.setFont(font)
        self.ClearOutputBoxButton.setObjectName("ClearOutputBoxButton")
        self.gridLayout_2.addWidget(self.frame, 4, 1, 1, 1)
        self.currentTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.currentTime.setFont(font)
        self.currentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime.setObjectName("currentTime")
        self.gridLayout_2.addWidget(self.currentTime, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 20, 10, 20)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pauseSchedulerButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pauseSchedulerButton.sizePolicy().hasHeightForWidth())
        self.pauseSchedulerButton.setSizePolicy(sizePolicy)
        self.pauseSchedulerButton.setMinimumSize(QtCore.QSize(20, 40))
        self.pauseSchedulerButton.setMaximumSize(QtCore.QSize(200, 80))
        self.pauseSchedulerButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pauseSchedulerButton.setFont(font)
        self.pauseSchedulerButton.setObjectName("pauseSchedulerButton")
        self.horizontalLayout.addWidget(self.pauseSchedulerButton)
        self.resumeSchedulerButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.resumeSchedulerButton.sizePolicy().hasHeightForWidth())
        self.resumeSchedulerButton.setSizePolicy(sizePolicy)
        self.resumeSchedulerButton.setMinimumSize(QtCore.QSize(20, 40))
        self.resumeSchedulerButton.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.resumeSchedulerButton.setFont(font)
        self.resumeSchedulerButton.setObjectName("resumeSchedulerButton")
        self.horizontalLayout.addWidget(self.resumeSchedulerButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.outputBox = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputBox.sizePolicy().hasHeightForWidth())
        self.outputBox.setSizePolicy(sizePolicy)
        self.outputBox.setMinimumSize(QtCore.QSize(400, 50))
        self.outputBox.setMaximumSize(QtCore.QSize(2000, 100))
        self.outputBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outputBox.setFont(font)
        self.outputBox.setObjectName("outputBox")
        self.gridLayout_2.addWidget(self.outputBox, 3, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 300))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setBaseSize(QtCore.QSize(550, 400))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.leftPanelLayout = QtWidgets.QVBoxLayout()
        self.leftPanelLayout.setContentsMargins(0, 0, -1, 0)
        self.leftPanelLayout.setSpacing(0)
        self.leftPanelLayout.setObjectName("leftPanelLayout")
        self.functionFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.functionFrame.sizePolicy().hasHeightForWidth())
        self.functionFrame.setSizePolicy(sizePolicy)
        self.functionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.functionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.functionFrame.setObjectName("functionFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.functionFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.functionLayout = QtWidgets.QVBoxLayout()
        self.functionLayout.setContentsMargins(5, 0, 5, 0)
        self.functionLayout.setSpacing(10)
        self.functionLayout.setObjectName("functionLayout")
        self.addJobButton = QtWidgets.QPushButton(self.functionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addJobButton.sizePolicy().hasHeightForWidth())
        self.addJobButton.setSizePolicy(sizePolicy)
        self.addJobButton.setMinimumSize(QtCore.QSize(40, 20))
        self.addJobButton.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addJobButton.setFont(font)
        self.addJobButton.setObjectName("addJobButton")
        self.functionLayout.addWidget(self.addJobButton)
        self.editJobButton = QtWidgets.QPushButton(self.functionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editJobButton.sizePolicy().hasHeightForWidth())
        self.editJobButton.setSizePolicy(sizePolicy)
        self.editJobButton.setMinimumSize(QtCore.QSize(40, 20))
        self.editJobButton.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editJobButton.setFont(font)
        self.editJobButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editJobButton.setObjectName("editJobButton")
        self.functionLayout.addWidget(self.editJobButton)
        self.removeJobButton = QtWidgets.QPushButton(self.functionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeJobButton.sizePolicy().hasHeightForWidth())
        self.removeJobButton.setSizePolicy(sizePolicy)
        self.removeJobButton.setMinimumSize(QtCore.QSize(40, 20))
        self.removeJobButton.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.removeJobButton.setFont(font)
        self.removeJobButton.setObjectName("removeJobButton")
        self.functionLayout.addWidget(self.removeJobButton)
        self.clearJobButton = QtWidgets.QPushButton(self.functionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearJobButton.sizePolicy().hasHeightForWidth())
        self.clearJobButton.setSizePolicy(sizePolicy)
        self.clearJobButton.setMinimumSize(QtCore.QSize(40, 20))
        self.clearJobButton.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.clearJobButton.setFont(font)
        self.clearJobButton.setObjectName("clearJobButton")
        self.functionLayout.addWidget(self.clearJobButton)
        self.gridLayout.addLayout(self.functionLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.SchedStateFrame = QtWidgets.QFrame(self.functionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SchedStateFrame.sizePolicy().hasHeightForWidth())
        self.SchedStateFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.SchedStateFrame.setFont(font)
        self.SchedStateFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SchedStateFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SchedStateFrame.setObjectName("SchedStateFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SchedStateFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SchedStateLayout = QtWidgets.QHBoxLayout()
        self.SchedStateLayout.setObjectName("SchedStateLayout")
        self.schedLabel = QtWidgets.QLabel(self.SchedStateFrame)
        self.schedLabel.setObjectName("schedLabel")
        self.SchedStateLayout.addWidget(self.schedLabel)
        self.schedState = QtWidgets.QLabel(self.SchedStateFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedState.sizePolicy().hasHeightForWidth())
        self.schedState.setSizePolicy(sizePolicy)
        self.schedState.setMinimumSize(QtCore.QSize(100, 0))
        self.schedState.setObjectName("schedState")
        self.SchedStateLayout.addWidget(self.schedState)
        self.horizontalLayout_2.addLayout(self.SchedStateLayout)
        self.gridLayout.addWidget(self.SchedStateFrame, 2, 0, 1, 1)
        self.leftPanelLayout.addWidget(self.functionFrame)
        self.gridLayout_2.addLayout(self.leftPanelLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 907, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuTestOptions = QtWidgets.QMenu(self.menubar)
        self.menuTestOptions.setEnabled(True)
        self.menuTestOptions.setObjectName("menuTestOptions")
        self.menuRunSpider = QtWidgets.QMenu(self.menubar)
        self.menuRunSpider.setObjectName("menuRunSpider")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_File = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionNew_File.setFont(font)
        self.actionNew_File.setShortcut("Ctrl+A")
        self.actionNew_File.setObjectName("actionNew_File")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCurrent_Version = QtWidgets.QAction(MainWindow)
        self.actionCurrent_Version.setObjectName("actionCurrent_Version")
        self.actionConfig = QtWidgets.QAction(MainWindow)
        self.actionConfig.setObjectName("actionConfig")
        self.action_RefreshSchedulerState = QtWidgets.QAction(MainWindow)
        self.action_RefreshSchedulerState.setEnabled(True)
        self.action_RefreshSchedulerState.setObjectName("action_RefreshSchedulerState")
        self.action_AddTestData2Table = QtWidgets.QAction(MainWindow)
        self.action_AddTestData2Table.setObjectName("action_AddTestData2Table")
        self.action_RemoveTestData = QtWidgets.QAction(MainWindow)
        self.action_RemoveTestData.setObjectName("action_RemoveTestData")
        self.action_Func1 = QtWidgets.QAction(MainWindow)
        self.action_Func1.setObjectName("action_Func1")
        self.action_Func2 = QtWidgets.QAction(MainWindow)
        self.action_Func2.setObjectName("action_Func2")
        self.action_ClearSchedStateText = QtWidgets.QAction(MainWindow)
        self.action_ClearSchedStateText.setObjectName("action_ClearSchedStateText")
        self.action_Func3 = QtWidgets.QAction(MainWindow)
        self.action_Func3.setObjectName("action_Func3")
        self.actionImport_Json = QtWidgets.QAction(MainWindow)
        self.actionImport_Json.setObjectName("actionImport_Json")
        self.actionrunVerintSpider = QtWidgets.QAction(MainWindow)
        self.actionrunVerintSpider.setObjectName("actionrunVerintSpider")
        self.actionConfig_Spider = QtWidgets.QAction(MainWindow)
        self.actionConfig_Spider.setObjectName("actionConfig_Spider")
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionConfig)
        self.menuImport.addAction(self.actionImport_Json)
        self.menuImport.addAction(self.actionCopy)
        self.menuImport.addAction(self.actionPaste)
        self.menuAbout.addAction(self.actionCurrent_Version)
        self.menuTestOptions.addAction(self.action_RefreshSchedulerState)
        self.menuTestOptions.addAction(self.action_AddTestData2Table)
        self.menuTestOptions.addAction(self.action_RemoveTestData)
        self.menuTestOptions.addAction(self.action_Func1)
        self.menuTestOptions.addAction(self.action_Func2)
        self.menuTestOptions.addAction(self.action_Func3)
        self.menuRunSpider.addAction(self.actionrunVerintSpider)
        self.menuRunSpider.addAction(self.actionConfig_Spider)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuRunSpider.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuTestOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.ClearOutputBoxButton.clicked.connect(self.outputBox.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheduler Manager"))
        self.ClearOutputBoxButton.setText(_translate("MainWindow", "Clear Output"))
        self.currentTime.setText(_translate("MainWindow", "Loading..."))
        self.pauseSchedulerButton.setText(_translate("MainWindow", "Pause"))
        self.resumeSchedulerButton.setText(_translate("MainWindow", "Resume"))
        self.outputBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Run Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "State"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ID"))
        self.addJobButton.setText(_translate("MainWindow", "Add Job"))
        self.editJobButton.setText(_translate("MainWindow", "Edit Job"))
        self.removeJobButton.setText(_translate("MainWindow", "Remove Job"))
        self.clearJobButton.setText(_translate("MainWindow", "Clear Job"))
        self.schedLabel.setText(_translate("MainWindow", "Scheduler: "))
        self.schedState.setText(_translate("MainWindow", "Initiating"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuTestOptions.setTitle(_translate("MainWindow", "TestOptions"))
        self.menuRunSpider.setTitle(_translate("MainWindow", "Run Spider"))
        self.actionNew_File.setText(_translate("MainWindow", "New File"))
        self.actionNew_File.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionSave_File.setStatusTip(_translate("MainWindow", "Save current file"))
        self.actionSave_File.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy selection"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste selection"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCurrent_Version.setText(_translate("MainWindow", "About"))
        self.actionConfig.setText(_translate("MainWindow", "Config"))
        self.action_RefreshSchedulerState.setText(_translate("MainWindow", "RefreshSchedulerState"))
        self.action_AddTestData2Table.setText(_translate("MainWindow", "AddTestData2Table"))
        self.action_RemoveTestData.setText(_translate("MainWindow", "RemoveTestData"))
        self.action_Func1.setText(_translate("MainWindow", "Func1"))
        self.action_Func2.setText(_translate("MainWindow", "Func2"))
        self.action_ClearSchedStateText.setText(_translate("MainWindow", "clearSchedStateText"))
        self.action_Func3.setText(_translate("MainWindow", "Func3"))
        self.actionImport_Json.setText(_translate("MainWindow", "Import Json"))
        self.actionrunVerintSpider.setText(_translate("MainWindow", "Run Verint Spider"))
        self.actionConfig_Spider.setText(_translate("MainWindow", "Config Spider"))
