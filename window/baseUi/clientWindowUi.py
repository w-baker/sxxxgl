from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView


class Ui_clientWindow(object):
    """
    客户端Ui_clientWindow类，Ui_clientWindow类中实现了窗口的各种控件
    """
    def setupUi(self, clientWindow):
        clientWindow.setObjectName("clientWindow")
        clientWindow.resize(900, 700)
        clientWindow.setMinimumSize(QtCore.QSize(900, 700))
        clientWindow.setMaximumSize(QtCore.QSize(900, 700))
        self.centralwidget = QtWidgets.QWidget(clientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 671))
        self.tabWidget.setObjectName("tabWidget")

        # 添加信息模块
        self.add_stu = QtWidgets.QWidget()
        self.add_stu.setObjectName("add_stu")

        self.s_id = QtWidgets.QLineEdit(self.add_stu)
        self.s_id.setGeometry(QtCore.QRect(110, 100, 271, 51))
        self.s_id.setObjectName("s_id")

        self.s_name = QtWidgets.QLineEdit(self.add_stu)
        self.s_name.setGeometry(QtCore.QRect(490, 100, 271, 51))
        self.s_name.setObjectName("s_name")

        self.s_class = QtWidgets.QLineEdit(self.add_stu)
        self.s_class.setGeometry(QtCore.QRect(110, 290, 271, 51))
        self.s_class.setObjectName("s_class")

        self.s_zy = QtWidgets.QLineEdit(self.add_stu)
        self.s_zy.setGeometry(QtCore.QRect(490, 290, 271, 51))
        self.s_zy.setObjectName("s_zy")

        self.s_sex = QtWidgets.QComboBox(self.add_stu)
        self.s_sex.setGeometry(QtCore.QRect(110, 190, 271, 51))
        self.s_sex.setObjectName("s_sex")
        self.s_sex.addItem("")
        self.s_sex.addItem("")

        self.s_age = QtWidgets.QSpinBox(self.add_stu)
        self.s_age.setGeometry(QtCore.QRect(490, 190, 271, 51))
        self.s_age.setMaximum(120)
        self.s_age.setObjectName("s_age")

        self.id_label = QtWidgets.QLabel(self.add_stu)
        self.id_label.setGeometry(QtCore.QRect(30, 100, 81, 51))
        self.id_label.setTextFormat(QtCore.Qt.PlainText)
        self.id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label.setObjectName("id_label")

        self.name_label = QtWidgets.QLabel(self.add_stu)
        self.name_label.setGeometry(QtCore.QRect(410, 100, 81, 51))
        self.name_label.setTextFormat(QtCore.Qt.PlainText)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")

        self.age_lable = QtWidgets.QLabel(self.add_stu)
        self.age_lable.setGeometry(QtCore.QRect(410, 190, 81, 51))
        self.age_lable.setTextFormat(QtCore.Qt.PlainText)
        self.age_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.age_lable.setObjectName("age_lable")

        self.sex_lable = QtWidgets.QLabel(self.add_stu)
        self.sex_lable.setGeometry(QtCore.QRect(30, 190, 81, 51))
        self.sex_lable.setTextFormat(QtCore.Qt.PlainText)
        self.sex_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_lable.setObjectName("sex_lable")

        self.zy_lable = QtWidgets.QLabel(self.add_stu)
        self.zy_lable.setGeometry(QtCore.QRect(410, 290, 81, 51))
        self.zy_lable.setTextFormat(QtCore.Qt.PlainText)
        self.zy_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.zy_lable.setObjectName("zy_lable")
        self.class_lable = QtWidgets.QLabel(self.add_stu)
        self.class_lable.setGeometry(QtCore.QRect(30, 290, 81, 51))
        self.class_lable.setTextFormat(QtCore.Qt.PlainText)
        self.class_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.class_lable.setObjectName("class_lable")

        self.note = QtWidgets.QTextEdit(self.add_stu)
        self.note.setGeometry(QtCore.QRect(110, 370, 650, 61))
        self.note.setReadOnly(True)
        self.note.setObjectName("note")

        self.add_clear = QtWidgets.QPushButton(self.add_stu)
        self.add_clear.setGeometry(QtCore.QRect(280, 480, 101, 41))
        self.add_clear.setObjectName("add_clear")

        self.add_sub = QtWidgets.QPushButton(self.add_stu)
        self.add_sub.setGeometry(QtCore.QRect(490, 480, 101, 41))
        self.add_sub.setObjectName("add_sub")

        self.tabWidget.addTab(self.add_stu, "")

        # 查询所有信息模块
        self.query_all = QtWidgets.QWidget()
        self.query_all.setObjectName("query_all")
        self.tableWidget = QtWidgets.QTableWidget(self.query_all)

        self.tableWidget.setGeometry(QtCore.QRect(40, 70, 811, 531))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")

        # 定义表头
        for i in range(0, 6):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.pushButton = QtWidgets.QPushButton(self.query_all)
        self.pushButton.setGeometry(QtCore.QRect(40, 7, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.query_all, "")

        self.pushButton1 = QtWidgets.QPushButton(self.query_all)
        self.pushButton1.setGeometry(QtCore.QRect(200, 7, 101, 51))
        self.pushButton1.setObjectName("pushButton")
        self.tabWidget.addTab(self.query_all, "")

        # 查询学生信息模块
        self.query_one = QtWidgets.QWidget()
        self.query_one.setObjectName("query_one")
        # 输入框
        self.query_one = QtWidgets.QWidget()
        self.query_one.setObjectName("query_one")
        self.input_name = QtWidgets.QLineEdit(self.query_one)
        self.input_name.setGeometry(QtCore.QRect(40, 20, 321, 51))
        self.input_name.setObjectName("input_name")
        # 提交数据按钮
        self.query_by_name = QtWidgets.QPushButton(self.query_one)
        self.query_by_name.setGeometry(QtCore.QRect(440, 20, 161, 51))
        self.query_by_name.setObjectName("query_by_name")
        # 清空数按钮
        self.cleartable = QtWidgets.QPushButton(self.query_one)
        self.cleartable.setGeometry(QtCore.QRect(680, 20, 161, 51))
        self.cleartable.setObjectName("cleartable")
        self.tabWidget.addTab(self.query_one, "")
        # 数据输出控件
        self.print_stu = QtWidgets.QTextEdit(self.query_one)
        self.print_stu.setGeometry(QtCore.QRect(40, 90,  801, 531))
        self.print_stu.setReadOnly(True)
        self.print_stu.setObjectName("print_stu")

        # 修改学生信息模块
        self.update_one = QtWidgets.QWidget()
        self.update_one.setObjectName("update_one")

        #创建输入框控件
        self.update_input_id = QtWidgets.QLineEdit(self.update_one)
        self.update_input_id.setGeometry(QtCore.QRect(220, 40, 201, 51))
        self.update_input_id.setObjectName("update_input_id")
        self.update_name = QtWidgets.QLineEdit(self.update_one)
        self.update_name.setGeometry(QtCore.QRect(110, 140, 261, 51))
        self.update_name.setObjectName("update_name")
        self.update_sex = QtWidgets.QComboBox(self.update_one)
        self.update_sex.setGeometry(QtCore.QRect(500, 140, 261, 51))
        self.update_sex.setObjectName("update_sex")
        self.update_sex.addItem("")
        self.update_sex.addItem("男")
        self.update_sex.addItem("女")
        self.update_age = QtWidgets.QSpinBox(self.update_one)
        self.update_age.setGeometry(QtCore.QRect(112, 270, 261, 51))
        self.update_age.setMaximum(120)
        self.update_age.setObjectName("update_age")
        self.update_class = QtWidgets.QLineEdit(self.update_one)
        self.update_class.setGeometry(QtCore.QRect(500, 270, 261, 51))
        self.update_class.setObjectName("update_class")
        self.update_zy = QtWidgets.QLineEdit(self.update_one)
        self.update_zy.setGeometry(QtCore.QRect(110, 400, 261, 51))
        self.update_zy.setObjectName("update_zy")

        # 创建按钮控件
        self.update_sub = QtWidgets.QPushButton(self.update_one)
        self.update_sub.setGeometry(QtCore.QRect(500, 390, 101, 61))
        self.update_sub.setObjectName("update_sub")
        self.update_query_button = QtWidgets.QPushButton(self.update_one)
        self.update_query_button.setGeometry(QtCore.QRect(450, 40, 141, 51))
        self.update_query_button.setObjectName("update_query_button")
        self.update_clear = QtWidgets.QPushButton(self.update_one)
        self.update_clear.setGeometry(QtCore.QRect(660, 390, 101, 61))
        self.update_clear.setObjectName("update_clear")
        self.del_button = QtWidgets.QPushButton(self.update_one)
        self.del_button.setGeometry(QtCore.QRect(620, 40, 141, 51))
        self.del_button.setObjectName("pushButton")

        # 创建输入框对应的标签
        self.update_one_id_label = QtWidgets.QLabel(self.update_one)
        self.update_one_id_label.setGeometry(QtCore.QRect(140, 40, 81, 51))
        self.update_one_id_label.setObjectName("update_one_id_label")
        self.update_one_name_label = QtWidgets.QLabel(self.update_one)
        self.update_one_name_label.setGeometry(QtCore.QRect(30, 140, 81, 51))
        self.update_one_name_label.setObjectName("update_one_name_label")
        self.update_one_age_lable = QtWidgets.QLabel(self.update_one)
        self.update_one_age_lable.setGeometry(QtCore.QRect(420, 140, 81, 51))
        self.update_one_age_lable.setObjectName("update_one_age_lable")
        self.update_one_age_label = QtWidgets.QLabel(self.update_one)
        self.update_one_age_label.setGeometry(QtCore.QRect(30, 270, 81, 51))
        self.update_one_age_label.setObjectName("update_one_age_label")
        self.update_one_class_label = QtWidgets.QLabel(self.update_one)
        self.update_one_class_label.setGeometry(QtCore.QRect(420, 270, 81, 51))
        self.update_one_class_label.setObjectName("update_one_class_label")
        self.update_one_zy_label = QtWidgets.QLabel(self.update_one)
        self.update_one_zy_label.setGeometry(QtCore.QRect(30, 400, 81, 51))
        self.update_one_zy_label.setObjectName("update_one_zy_label")
        self.tabWidget.addTab(self.update_one, "")

        # 关于软件
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.label = QtWidgets.QLabel(self.about)
        self.label.setGeometry(QtCore.QRect(0, 50, 881, 491))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.about, "")

        clientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(clientWindow)
        self.statusbar.setObjectName("statusbar")
        clientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(clientWindow)
        self.tabWidget.setCurrentIndex(0)
        # 第一页中按钮
        self.add_clear.clicked.connect(self.s_class.clear)
        self.add_clear.clicked.connect(self.s_zy.clear)
        self.add_clear.clicked.connect(self.s_id.clear)
        self.add_clear.clicked.connect(self.s_name.clear)
        self.add_sub.clicked.connect(clientWindow.add_sub_click)

        # 第二页中按钮
        self.pushButton.clicked.connect(clientWindow.query_all_click)
        self.pushButton1.clicked.connect(clientWindow.clear_all_click)

        # 第三页中按钮
        self.cleartable.clicked.connect(clientWindow.cleartable_click)
        self.query_by_name.clicked.connect(clientWindow.query_by_name_def)

        # 第四页中按钮
        self.update_clear.clicked.connect(clientWindow.update_clear_def)
        self.update_query_button.clicked.connect(clientWindow.update_query_button_def)
        self.update_sub.clicked.connect(clientWindow.update_sub_def)
        self.del_button.clicked.connect(clientWindow.del_button_def)

        QtCore.QMetaObject.connectSlotsByName(clientWindow)

    def retranslateUi(self, clientWindow):
        font = QtGui.QFont()
        font.setPointSize(12)
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        _translate = QtCore.QCoreApplication.translate

        clientWindow.setWindowTitle(_translate("clientWindow", "学生信息管理系统"))
        # 第一页信息
        self.s_id.setText(_translate("clientWindow", "请输入学号（不超过20位的整数）"))
        self.s_id.setFont(font1)
        self.s_name.setText(_translate("clientWindow", "请输入姓名（汉字或字母）"))
        self.s_name.setFont(font1)
        self.s_class.setText(_translate("clientWindow", "请输入班级"))
        self.s_class.setFont(font1)
        self.s_zy.setText(_translate("clientWindow", "请输入所在专业"))
        self.s_zy.setFont(font1)
        self.s_sex.setItemText(0, _translate("clientWindow", "男"))
        self.s_sex.setItemText(1, _translate("clientWindow", "女"))

        self.add_sub.setText(_translate("clientWindow", "提  交"))
        self.add_sub.setFont(font)

        self.id_label.setText(_translate("clientWindow", "学 号:"))
        self.id_label.setFont(font)
        self.name_label.setText(_translate("clientWindow", "姓 名:"))
        self.name_label.setFont(font)
        self.age_lable.setText(_translate("clientWindow", "年 龄:"))
        self.age_lable.setFont(font)
        self.sex_lable.setText(_translate("clientWindow", "性 别:"))
        self.sex_lable.setFont(font)
        self.zy_lable.setText(_translate("clientWindow", "专 业:"))
        self.zy_lable.setFont(font)
        self.class_lable.setText(_translate("clientWindow", "班 级:"))
        self.class_lable.setFont(font)

        self.add_clear.setText(_translate("clientWindow", "清空"))
        self.add_clear.setFont(font)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_stu), _translate("clientWindow", "录入学生信息"))
        # 第二页信息
        # 写入表头信息
        header = ["学号", "姓名", "性别", "年龄", "班级", "专业"]
        for i in range(0, 6):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("clientWindow", header[i]))
        self.tableWidget.setSortingEnabled(False)
        # 按钮信息
        self.pushButton.setText(_translate("clientWindow", "查 询"))
        self.pushButton.setFont(font)
        self.pushButton1.setText(_translate("clientWindow", "清 空"))
        self.pushButton1.setFont(font)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.query_all), _translate("clientWindow", "查看所有学生"))
        # 第三页信息
        self.query_by_name.setText(_translate("clientWindow", "姓 名 查 询"))
        self.query_by_name.setFont(font)
        self.cleartable.setText(_translate("clientWindow", "清 除 结 果"))
        self.cleartable.setFont(font)
        self.input_name.setFont(font1)
        self.print_stu.setFont(font1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.query_one), _translate("clientWindow", "查询学生信息"))
        # 第四页信息
        self.update_input_id.setText(_translate("clientWindow", "请输入要修改的学生学号"))
        self.update_input_id.setFont(font1)
        self.update_name.setFont(font1)
        self.update_sex.setFont(font1)
        self.update_age.setFont(font1)
        self.update_class.setFont(font1)
        self.update_zy.setFont(font1)
        self.update_query_button.setText(_translate("clientWindow", "提 交 查 询"))
        self.update_query_button.setFont(font)
        self.del_button.setText(_translate("clientWindow", "删 除 学 生"))
        self.del_button.setFont(font)
        self.update_sub.setText(_translate("clientWindow", "提交修改"))
        self.update_sub.setFont(font)
        self.update_clear.setText(_translate("clientWindow", "清除输入"))
        self.update_clear.setFont(font)
        self.update_one_id_label.setText(_translate("clientWindow",
                                                    "<html><head/><body><p align=\"center\"><span style=\" "
                                                    "font-size:12pt; font-weight:600;\">学号:</span></p></body></html>"))
        self.update_one_name_label.setText(_translate("clientWindow",
                                                      "<html><head/><body><p align=\"center\"><span style=\" "
                                                      "font-size:12pt; "
                                                      "font-weight:600;\">姓名:</span></p></body></html>"))
        self.update_one_age_lable.setText(_translate("clientWindow",
                                                     "<html><head/><body><p align=\"center\"><span style=\" "
                                                     "font-size:12pt; "
                                                     "font-weight:600;\">性别:</span></p></body></html>"))
        self.update_one_age_label.setText(_translate("clientWindow",
                                                     "<html><head/><body><p align=\"center\"><span style=\" "
                                                     "font-size:12pt; "
                                                     "font-weight:600;\">年龄:</span></p></body></html>"))
        self.update_one_class_label.setText(_translate("clientWindow",
                                                       "<html><head/><body><p align=\"center\"><span style=\" "
                                                       "font-size:12pt; "
                                                       "font-weight:600;\">班级:</span></p></body></html>"))
        self.update_one_zy_label.setText(_translate("clientWindow",
                                                    "<html><head/><body><p align=\"center\"><span style=\" "
                                                    "font-size:12pt; font-weight:600;\">专业:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.update_one), _translate("clientWindow", "修改/删除学生"))
        # 第六页信息
        self.label.setText(_translate("clientWindow", "<html><head/><body><p align=\"center\"><span style=\" "
                                                      "font-size:20pt; font-weight:600; text-decoration: "
                                                      "underline;\">感谢使用学生信息管理系统</span></p><p><br/></p><p><span "
                                                      "style=\" "
                                                      "font-size:14pt;\">作者：王昌宏</span></p><p><br/></p><p><span "
                                                      "style=\" "
                                                      "font-size:14pt;\">e-mail:w.xiaohong.0817@gmail.com</span></p"
                                                      "><p><br/></p><p><span style=\" "
                                                      "font-size:14pt;\">公开：源码已完全公开到github</span></p><p><br/></p><p"
                                                      "><span style=\" font-size:14pt;\">github：</span><a "
                                                      "href=\"https://github.com/w-baker/sxxxgl_ui\"><span style=\" "
                                                      "font-size:14pt; text-decoration: underline; "
                                                      "color:#0000ff;\">https://github.com/w-baker/sxxxgl_ui</span"
                                                      "></a></p></body></html>"))
        self.label.setOpenExternalLinks(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("clientWindow", "关于"))
