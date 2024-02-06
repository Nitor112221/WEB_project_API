import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from data.ui_py_design.main_ui import UiMainWindow
import backend.backend as backend
from PyQt5.QtCore import Qt


class MainApplication(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('API Application')
        self.lon = 37.530887
        self.lat = 55.703118
        self.setFixedSize(self.size())
        self.delta = 0.002
        self.update_map()

    def update_map(self):
        pixmap = backend.get_map(lon=str(self.lon), lat=str(self.lat), delta=str(self.delta))
        if pixmap is None:
            print('Неудачный запрос :(, попробуйте сново')
            return
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.delta -= 0.0005
        elif event.key() == Qt.Key_PageDown:
            self.delta += 0.0005
        self.delta = min(1., max(0., self.delta))

        if event.key() == Qt.Key_Down:
            self.lat -= self.delta * 2
        elif event.key() == Qt.Key_Up:
            self.lat += self.delta * 2
        elif event.key() == Qt.Key_Left:
            self.lon -= self.delta * 2
        elif event.key() == Qt.Key_Right:
            self.lon += self.delta * 2
        if self.lat > 90:
            self.lat -= 180
        elif self.lat < -90:
            self.lat += 180
        if self.lon > 90:
            self.lon -= 180
        elif self.lon < -90:
            self.lon += 180
        self.update_map()


app = QApplication(sys.argv)
ex = MainApplication()
ex.show()
sys.exit(app.exec())
