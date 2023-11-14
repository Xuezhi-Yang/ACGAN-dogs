from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPixmap
import sys
import mygan
from PIL import Image


class MyWindow:
    def __init__(self):
        self.window = uic.loadUi('./window.ui')
        self.window.setFixedSize(1200, 640)
        self.window.pushButton.clicked.connect(self.getdog)
        self.window.textBrowser.setStyleSheet("background-color: transparent;border: none;")


    def getdog(self):
        index = self.window.lineEdit.text()
        if index.isdigit():
            index = int(index)
            index %=100
            img = mygan.genarate_100_dogs(index)
            # img.show()
            img = QImage(img.tobytes(), img.width, img.height, QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            self.window.label_2.setPixmap(img)
        else:
            self.window.label_2.clear()
            self.window.label_2.setText('请输入数字')
        


if __name__ == '__main__':
    app = QApplication(sys.argv)

    Window = MyWindow()
    Window.window.show()

    app.exec()
