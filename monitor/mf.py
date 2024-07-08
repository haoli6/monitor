from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from monitor.Video import Video


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1606, 860)

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 210, 1591, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.video1 = QtWidgets.QLabel(self.frame)
        self.video1.setGeometry(QtCore.QRect(20, 20, 1491, 581))
        self.video1.setObjectName("video1")
        self.video1.setScaledContents(True)

        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(10, 69, 151, 131))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(0, 0, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\nfont: 14pt \"黑体\";")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 131, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\nfont: 14pt \"黑体\";")
        self.label_2.setObjectName("label_2")

        self.frame_6 = QtWidgets.QFrame(Dialog)
        self.frame_6.setGeometry(QtCore.QRect(170, 70, 261, 141))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.carnum = QtWidgets.QLabel(self.frame_6)
        self.carnum.setGeometry(QtCore.QRect(0, 0, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.carnum.setFont(font)
        self.carnum.setStyleSheet("font: 20pt \"Segoe Print\";\ncolor: rgb(255, 0, 4);")
        self.carnum.setObjectName("carnum")

        self.bodynum = QtWidgets.QLabel(self.frame_6)
        self.bodynum.setGeometry(QtCore.QRect(0, 60, 211, 31))
        self.bodynum.setStyleSheet("font: 20pt \"Segoe Print\";\ncolor: rgb(255, 0, 4);")
        self.bodynum.setObjectName("bodynum")

        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(470, 10, 631, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet(
            "color: rgb(59, 10, 255);\nbackground-color: rgb(255, 255, 255);\nfont: 36pt \"隶书\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.selectButton = QtWidgets.QPushButton(Dialog)
        self.selectButton.setGeometry(QtCore.QRect(10, 10, 151, 41))
        self.selectButton.setObjectName("selectButton")
        self.selectButton.setText("选择视频文件")
        self.selectButton.clicked.connect(self.selectVideoFile)

        self.video_thread = None

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.video1.setText(_translate("Dialog", ""))
        self.label.setText(_translate("Dialog", "车流流量:"))
        self.label_2.setText(_translate("Dialog", "人流量："))
        self.carnum.setText(_translate("Dialog", "0"))
        self.bodynum.setText(_translate("Dialog", "0"))
        self.title.setText(_translate("Dialog", "人车流量监控工具"))

    def selectVideoFile(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "选择视频文件", "", "Video Files (*.mp4 *.avi *.mov)")
        if fileName:
            self.videoFileSelected(fileName)

    def videoFileSelected(self, fileName):
        # 停止目前的线程，如果他存在的话
        if self.video_thread and self.video_thread.isRunning():
            self.video_thread.terminate()
            self.video_thread.wait()

        # 开始新的视频执行线程
        self.video_thread = Video(fileName)
        self.video_thread.send.connect(self.updateFrame)
        self.video_thread.start()

    def updateFrame(self, h, w, c, img_bytes, th_id, num1, num2):
        image = QtGui.QImage(img_bytes, w, h, w * c, QtGui.QImage.Format_RGB888)
        scaled_image = image.scaled(self.video1.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.video1.setPixmap(QtGui.QPixmap.fromImage(scaled_image))
        self.carnum.setText(str(num1))
        self.bodynum.setText(str(num2))

    def resizeEvent(self, event):
        if self.video_thread and self.video_thread.isRunning():
            self.video_thread.update_frame()
