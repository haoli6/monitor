from PyQt5.QtCore import QThread, pyqtSignal
import cv2 as cv
from access_token.car import vehicle_detect

class Video(QThread):
    send = pyqtSignal(int, int, int, bytes, int, int, int)  # 信号发送

    def __init__(self, video_id):
        super().__init__()
        self.video_id = video_id
        self.dev = cv.VideoCapture(video_id)
        # if not self.dev.isOpened():
        #     print(f"Error: Cannot open video {video_id}")

    def run(self):
        while self.dev.isOpened():
            ret, frame = self.dev.read()
            if not ret:
                print('Error: Failed to capture frame')
                break

            # 调用车辆检测和识别函数
            frame, num, num2 = vehicle_detect(frame)
            # 获取帧的高度、宽度和通道数
            h, w, c = frame.shape

            # 将帧转换为字节数据
            img_bytes = frame.tobytes()

            # 发送信号
            self.send.emit(h, w, c, img_bytes, 0, num, num2)  # 这里的 0 是占位符，表示 th_id 没有实际用途
            # 睡眠10ms
            QThread.usleep(10000)

        self.dev.release()
        cv.destroyAllWindows()
