from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.mdui import Ui_Dialog
from monitor.monitorframe import MonitorDialog

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.pixmap = QtGui.QPixmap('data/background.jpg')
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        self.resizeEvent = self.on_resize
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.users = self.load_users()

    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def goin(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if username in self.users and self.users[username] == password:
            self.monitorframe = MonitorDialog()
            self.monitorframe.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, '错误', '用户名或密码错误')

# 注册
    def register_user(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if username and password:
            if username not in self.users:
                self.users[username] = password
                self.save_users()
                QtWidgets.QMessageBox.information(self, '成功', '注册成功，请登入')
            else:
                QtWidgets.QMessageBox.warning(self, '错误', '用户名已存在')
        else:
            QtWidgets.QMessageBox.warning(self, '错误', '用户名和密码不能为空')

#登录
    def load_users(self):
        try:
            with open('users.txt', 'r') as f:
                users = {}
                for line in f:
                    line = line.strip()
                    if line:  # 确保这一行不是空的
                        parts = line.split(',')
                        if len(parts) == 2:  # 确保这一行有两个部分
                            username, password = parts
                            users[username] = password
                return users
        except FileNotFoundError:
            return {}

#在users.txt中保存用户名和密码
    def save_users(self):
        with open('users.txt', 'w') as f:
            for username, password in self.users.items():
                f.write(f'{username},{password}\n')
