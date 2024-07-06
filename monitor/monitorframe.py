from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from monitor.mf import Ui_Dialog
from monitor.Video import Video

class MonitorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.th1 = Video('data/vd1.mp4')
        # 绑定信号与槽函数
        self.th1.send.connect(self.showimg)
        self.th1.start()

    def showimg(self, h, w, c, b, th_id, num1, num2):
        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        if th_id == 1:
            # 自动缩放
            width = self.ui.video1.width()
            height = self.ui.video1.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.video1.setPixmap(scale_pix)
            # str(num) 类型转换
            self.ui.carnum.setText(str(num1))
            self.ui.bodynum.setText(str(num2))