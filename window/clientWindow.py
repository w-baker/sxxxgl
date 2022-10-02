from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QMessageBox

from bean.Student import Student
from dao import StudentDao
from utils.MyException import *
from utils.utils import *
from window.baseUi.clientWindowUi import Ui_clientWindow


class ClientWindow(QMainWindow, Ui_clientWindow):
    """
    继承于自定义的Ui_clientWindow类，从而在当前类中实现Ui_clientWindow中所要用到的事件函数
    """
    def __init__(self, parent=None):
        super(ClientWindow, self).__init__(parent)
        self.query_button_flag = False
        self.setupUi(self)

    def add_sub_click(self):
        """
        添加学生的事件响应函数
        :return:
        """
        # 获取参数并进行验证
        try:
            s_id = self.s_id.text()
            if not isId(s_id):  #  不是正确的id则抛出异常
                raise IdException(s_id)

            s_name = self.s_name.text()
            if not isName(s_name):
                raise NameException(s_name)

            s_age = self.s_age.text()
            s_sex = self.s_sex.currentText()
            s_class = self.s_class.text()
            s_zy = self.s_zy.text()
        except IdException as e:
            self.note.setText(f"{e}\n请重新输入！")
        except NameException as e:
            self.note.setText(f"{e}\n请重新输入！")
        else:  # 当输入信息无误时进行数据提交
            stu = Student(s_id, s_name, s_sex, s_age, s_class, s_zy)
            result = StudentDao.add(stu)
            if result:
                self.note.setText(f"{stu}\n添加成功")
            else:
                self.note.setText(f"添加失败\n原因:{s_id}已经存在")

    def query_all_click(self):
        """
        查询所有学生信息中查询按钮的事件响应函数
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        data = StudentDao.query_all()[1]
        if not data:  # 如果数据库中不存在数据
            self.tableWidget.setRowCount(1)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem())
            self.tableWidget.setSpan(0, 0, 1, 6)
            item = self.tableWidget.item(0, 0)
            item.setText(_translate("clientWindow", "当前数据库中没有数据"))
            item.setFont(font)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
        else:
            # 查询数据库中数据
            self.tableWidget.setRowCount(len(data))
            # 创建表格并写入内容
            for i in range(0, len(data)):
                for j in range(0, len(data[i])):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem())
                    item = self.tableWidget.item(i, j)
                    item.setText(_translate("clientWindow", str(data[i][j])))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setSortingEnabled(False)

    def clear_all_click(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def cleartable_click(self):
        self.input_name.clear()
        self.print_stu.clear()

    def query_by_name_def(self):
        """
        学生查询中查询按钮的事件响应函数
        :return:
        """

        s_name = self.input_name.text()
        data = StudentDao.query_by_name(s_name)[1]
        if data:
            for item in data:
                stu = Student(item[0], item[1], item[2], item[3], item[4], item[5])
                self.print_stu.append(f"{stu}\n")
        else:
            self.print_stu.setText(f"没有查询到姓名为:{s_name}的学生信息！！！")

    def update_query_button_def(self):
        """
        修改删除中用于处理学号查询的按钮事件响应函数，查询成功后会使得输入框为只读
        :return:
        """
        intput_id = self.update_input_id.text()
        if not intput_id:
            self.msg_box = QMessageBox(QMessageBox.Warning, '警告', '请输入学号!')
            self.msg_box.exec_()
            return
        else:
            result = StudentDao.query_by_id(intput_id)[1]
            if result:
                self.update_input_id.setReadOnly(True)  # 查询到结果后学号不能修改

                self.query_button_flag = True  # 设置是否查询到信息标记

                stu = Student(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
                self.update_name.setText(stu.get_name())
                self.update_sex.setCurrentText(stu.get_sex())
                self.update_age.setValue(stu.get_age())
                self.update_class.setText(stu.get_class())
                self.update_zy.setText(stu.get_zy())
            else:
                self.msg_box = QMessageBox(QMessageBox.Warning, '警告', f"不存在学号为{intput_id}的学生")
                self.msg_box.exec_()
                self.update_input_id.clear()


    def update_sub_def(self):
        """
        修改/删除中提交修改的点击事件响应函数
        :return:
        """
        name = self.update_name.text()
        if not isName(name):
            self.msg_box = QMessageBox(QMessageBox.Warning, '警告', f"姓名只能是字母或汉字！")
            self.msg_box.exec_()
            return
        s_id = self.update_input_id.text()
        sex = self.update_sex.currentText()
        age = self.update_age.text()
        s_class = self.update_class.text()
        zy = self.update_zy.text()
        stu = Student(s_id, name, sex, age, s_class, zy)

        a = QMessageBox.question(self, '提交修改', '你确定要提交修改吗?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        if a == QMessageBox.Yes:  # 接受提交
            result = StudentDao.update(stu)[0]  # 获取提交返回值
            if result:
                msg_box = QMessageBox(QMessageBox.Information, '提示', '提交成功')
                msg_box.exec_()
                self.update_clear_def()
            else:
                msg_box = QMessageBox(QMessageBox.Information, '提示', '提交失败')
                msg_box.exec_()


    def del_button_def(self):
        """
        删除/修改中‘删除’按钮的事件响应函数
        :return:
        """
        if not self.query_button_flag: # 判断是否已经查询到学生信息
            msg_box = QMessageBox(QMessageBox.Information, '提示', '请先查询该学生信息')
            msg_box.exec_()
            return

        a = QMessageBox.question(self, '提交修改', '你确定要提交删除吗?', QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        if a == QMessageBox.Yes:  # 接受删除
            s_id = self.update_input_id.text()
            result = StudentDao.delete(s_id)
            if result:
                msg_box = QMessageBox(QMessageBox.Information, '提示', '删除成功！')
                msg_box.exec_()
            else:
                msg_box = QMessageBox(QMessageBox.Information, '提示', '删除失败！')
                msg_box.exec_()

    def update_clear_def(self):
        """
        删除/修改中‘清除输入’按钮的事件响应函数，将修改/删除界面中输入框的内容清空，并且使学号处可输入
        :return:
        """
        self.query_button_flag = False
        self.update_input_id.setReadOnly(False)
        self.update_class.clear()
        self.update_sex.clear()
        self.update_zy.clear()
        self.update_age.clear()
        self.update_name.clear()
        self.update_input_id.clear()


