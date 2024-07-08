from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1377, 817)
        Dialog.setStyleSheet("")

        # 标题
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(290, 80, 751, 71))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(241 238 246);\nfont: 48pt \"隶书\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        # 用户名输入
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(500, 300, 361, 41))
        self.username.setPlaceholderText("请输入用户名")
        self.username.setObjectName("username")

        # 密码输入
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(500, 360, 361, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("请输入密码")
        self.password.setObjectName("password")

        # 登录按钮
        self.go = QtWidgets.QPushButton(Dialog)
        self.go.setGeometry(QtCore.QRect(570, 610, 211, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(22)
        self.go.setFont(font)
        self.go.setStyleSheet(
            "\nQPushButton\n{\n    background-color: #473C8B;\n    border-style: outset;\n    border-width: 2px;\n    border-radius:5px;\n    border-color: #8B7355;\n    color:white;\n    font: 22pt \"华文新魏\";\n    padding: 5px;\n}\nQPushButton:hover\n{\n    background-color: rgb(0, 150, 0);\n}\nQPushButton:pressed\n{\n    background-color: #FF6A6AF;\n    border-style: inset;\n}\nQPushButton:!enabled{\n    background-color: rgb(100, 100, 100);\n    border-style: inset;\n}")
        self.go.setObjectName("go")

        # 注册按钮
        self.register = QtWidgets.QPushButton(Dialog)
        self.register.setGeometry(QtCore.QRect(570, 690, 211, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(22)
        self.register.setFont(font)
        self.register.setStyleSheet(
            "\nQPushButton\n{\n    background-color: #473C8B;\n    border-style: outset;\n    border-width: 2px;\n    border-radius:5px;\n    border-color: #8B7355;\n    color:white;\n    font: 22pt \"华文新魏\";\n    padding: 5px;\n}\nQPushButton:hover\n{\n    background-color: rgb(0, 150, 0);\n}\nQPushButton:pressed\n{\n    background-color: #FF6A6AF;\n    border-style: inset;\n}\nQPushButton:!enabled{\n    background-color: rgb(100, 100, 100);\n    border-style: inset;\n}")
        self.register.setObjectName("register")

        self.retranslateUi(Dialog)
        self.go.clicked.connect(Dialog.goin)  
        self.register.clicked.connect(Dialog.register_user)  
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "人车流量监控工具"))
        self.go.setText(_translate("Dialog", "登入"))
        self.register.setText(_translate("Dialog", "注册"))
