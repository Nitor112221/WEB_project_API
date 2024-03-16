import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from data.ui_py_design.main_ui import Ui_MainWindow
import backend.backend as backend
from PyQt5.QtCore import Qt


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('API Application')
        self.lon = 37.530887
        self.lat = 55.703118
        self.ltype = 'map'
        self.setFixedSize(self.size())
        self.delta = 0.002
        self.point = ""
        self.update_map()

        self.type_map.currentTextChanged.connect(self.update_view_map)
        self.pushButton.clicked.connect(self.search_place)
        self.pushButton_reset.clicked.connect(self.reset_place)

    def update_view_map(self):
        if self.type_map.currentText() == 'Схема':
            self.ltype = 'map'
        elif self.type_map.currentText() == 'Спутник':
            self.ltype = 'sat'
        elif self.type_map.currentText() == 'Гибрид':
            self.ltype = 'sat,skl'
        self.update_map()

    def update_map(self):
        pixmap = backend.get_map(lon=str(self.lon), lat=str(self.lat), delta=str(self.delta),
                                 ltype=self.ltype, flags=self.point)
        if pixmap is None:
            print('Неудачный запрос :(, попробуйте сново')
            return
        self.label_map.setPixmap(pixmap)

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

    def search_place(self):
        place = self.lineEdit.text()
        result = backend.get_coordinate(place)
        self.lon = float(result[0][0])
        self.lat = float(result[0][1])
        self.point = f"{self.lon},{self.lat}"
        self.label_place.setText(f"Адрес: {result[1]}")
        self.update_map()

    def reset_place(self):
        self.lon = 37.530887
        self.lat = 55.703118
        self.point = ""
        self.lineEdit.setText("")
        self.label_place.setText("Адрес:")
        self.update_map()


app = QApplication(sys.argv)
ex = MainApplication()
ex.show()
sys.exit(app.exec())
