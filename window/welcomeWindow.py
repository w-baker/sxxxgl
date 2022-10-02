
from PyQt5.QtWidgets import QMainWindow, QApplication

from window.clientWindow import ClientWindow
from window.baseUi.welcomeWindowUI import Ui_welcomeWindow


class WelcomeWindow(QMainWindow, Ui_welcomeWindow):
    """
    继承于Ui_welcomeWindow类，从而实现Ui_welcomeWindow中所有控件的事件函数
    """
    def __init__(self, parent=None):
        super(WelcomeWindow, self).__init__(parent)
        self.setupUi(self)

    def toSystem(self):
        """
        进入系统按钮的点击事件函数
        :return:
        """
        self.close()
        self.clientWin = ClientWindow()
        self.clientWin.show()

    def exitSystem(self):
        """
        退出系统
        :return:
        """
        self.close()
