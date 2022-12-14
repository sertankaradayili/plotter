# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import numpy as np
import matplotlib.pyplot as plt



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.actionplot = QtWidgets.QPushButton(self.centralwidget)
        self.actionplot.setGeometry(QtCore.QRect(410, 350, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.actionplot.setFont(font)
        self.actionplot.setObjectName("actionplot")
        self.titleofgraph = QtWidgets.QLabel(self.centralwidget)
        self.titleofgraph.setGeometry(QtCore.QRect(370, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.titleofgraph.setFont(font)
        self.titleofgraph.setAcceptDrops(False)
        self.titleofgraph.setObjectName("titleofgraph")
        self.titleofxaxis = QtWidgets.QLabel(self.centralwidget)
        self.titleofxaxis.setGeometry(QtCore.QRect(370, 160, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.titleofxaxis.setFont(font)
        self.titleofxaxis.setAcceptDrops(False)
        self.titleofxaxis.setObjectName("titleofxaxis")
        self.titleofyaxis = QtWidgets.QLabel(self.centralwidget)
        self.titleofyaxis.setGeometry(QtCore.QRect(370, 210, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.titleofyaxis.setFont(font)
        self.titleofyaxis.setAcceptDrops(False)
        self.titleofyaxis.setObjectName("titleofyaxis")
        self.actiontitle = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.actiontitle.setGeometry(QtCore.QRect(520, 120, 191, 31))
        self.actiontitle.setObjectName("actiontitle")
        self.actionxtitle = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.actionxtitle.setGeometry(QtCore.QRect(520, 170, 191, 31))
        self.actionxtitle.setObjectName("actionxtitle")
        self.actionytitle = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.actionytitle.setGeometry(QtCore.QRect(520, 220, 191, 31))
        self.actionytitle.setObjectName("actionytitle")
        self.actionpic = QtWidgets.QLabel(self.centralwidget)
        self.actionpic.setGeometry(QtCore.QRect(20, 90, 331, 201))
        self.actionpic.setText("")
        self.actionpic.setPixmap(QtGui.QPixmap("imgs/graph.png"))
        self.actionpic.setScaledContents(True)
        self.actionpic.setObjectName("actionpic")
        self.actionimport = QtWidgets.QPushButton(self.centralwidget)
        self.actionimport.setGeometry(QtCore.QRect(110, 350, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.actionimport.setFont(font)
        self.actionimport.setObjectName("actionimport")
        self.maintitle = QtWidgets.QLabel(self.centralwidget)
        self.maintitle.setGeometry(QtCore.QRect(240, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.maintitle.setFont(font)
        self.maintitle.setObjectName("maintitle")
        self.developedbysertan = QtWidgets.QLabel(self.centralwidget)
        self.developedbysertan.setGeometry(QtCore.QRect(600, 450, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(8)
        self.developedbysertan.setFont(font)
        self.developedbysertan.setAcceptDrops(False)
        self.developedbysertan.setObjectName("developedbysertan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 26))
        self.menubar.setObjectName("menubar")
        self.menuPlotter = QtWidgets.QMenu(self.menubar)
        self.menuPlotter.setObjectName("menuPlotter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuPlotter.addAction(self.actionHelp)
        self.menuPlotter.addAction(self.actionExit)
        self.menubar.addAction(self.menuPlotter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.actionplot.clicked.connect(self.show_graph)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionplot.setText(_translate("MainWindow", "Plot!"))
        self.titleofgraph.setText(_translate("MainWindow", "Title of Graph"))
        self.titleofxaxis.setText(_translate("MainWindow", "Title of X-axis"))
        self.titleofyaxis.setText(_translate("MainWindow", "Title of Y-axis"))
        self.actionimport.setText(_translate("MainWindow", "Import Data File"))
        self.maintitle.setText(_translate("MainWindow", "PLOTTER"))
        self.developedbysertan.setText(_translate("MainWindow", "Developed by Sertan"))
        self.menuPlotter.setTitle(_translate("MainWindow", "Plotter!"))
        self.actionHelp.setText(_translate("MainWindow", "Help!"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "See the prerequests!"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
    

    
    def show_graph(self):
        os.chdir(r'C:\Users\serta\OneDrive\Masa??st??\G3\G3')
        a=np.loadtxt('25mA.txt')
        x=a[:,0]
        y=a[:,1]
        plt.plot(x,y,linewidth=2, color='b')
        plt.title('Current vs Power for 25mA')
        plt.xlabel('Current in mA')
        plt.ylabel('Power in mW')
        plt.show()
        
        

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
