import requests
import os
import sys
import json
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt as Q


api_key = "5d666306-8732-43c4-a011-a9cc7afada11"



class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(os.path.join("api_yandex_map", "task1", "main.ui"), self)
        
        self.btnShow.clicked.connect(self.set_image)
        
    def set_image(self):
        try:
            self.z = min(11, max(1, int(self.ms.text())))
        except Exception:
            print("Empty scale field")
            print("I'll set 1 how scale")
            self.z = 1
        
        req = requests.get(
            f"https://static-maps.yandex.ru/1.x/?ll={self.lg.text()},{self.wd.text()}&z={self.z}&l=map"
        )
        
        if not req:
            print("Error in request")
            quit()
        
        with open("map.png", "wb") as file:
            file.write(req.content)
        
        pixmap = QPixmap("map.png")
        self.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec_())
