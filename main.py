import sys

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':  # 系统入口函数
    from window.welcomeWindow import WelcomeWindow
    app = QApplication(sys.argv)
    myWin = WelcomeWindow()
    myWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    pass