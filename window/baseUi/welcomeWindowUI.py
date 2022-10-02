from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcomeWindow(object):
    """
    欢迎窗口Ui_welcomeWindow类，Ui_welcomeWindow类中实现了欢迎窗口的各种控件
    """
    def setupUi(self, welcomeWindow):
        """
        初始化窗口
        :param welcomeWindow:
        :return:
        """
        welcomeWindow.setObjectName("welcomeWindow")
        welcomeWindow.resize(450, 380)
        welcomeWindow.setMinimumSize(QtCore.QSize(450, 380))
        welcomeWindow.setMaximumSize(QtCore.QSize(450, 380))
        self.centralwidget = QtWidgets.QWidget(welcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 451, 211))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 290, 288, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)

        # 创建进入系统和退出系统按钮
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        welcomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcomeWindow)

        # 绑定事件函数
        self.pushButton.clicked.connect(welcomeWindow.toSystem)
        self.pushButton_2.clicked.connect(welcomeWindow.exitSystem)
        QtCore.QMetaObject.connectSlotsByName(welcomeWindow)

    def retranslateUi(self, welcomeWindow):
        """
        窗口属性修改
        :param welcomeWindow:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        welcomeWindow.setWindowTitle(_translate("welcomeWindow", "学生信息管理系统"))
        self.label.setText(_translate("welcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">欢迎使用学生信息管理系统</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:11pt;\">作者：王昌宏</span></p><p align=\"center\"><span style=\" font-size:11pt;\">学号：200107101</span></p><p align=\"center\"><span style=\" font-size:11pt;\">班级：2020级7班</span></p></body></html>"))
        self.pushButton.setText(_translate("welcomeWindow", "进入系统"))
        self.pushButton_2.setText(_translate("welcomeWindow", "退出系统"))
