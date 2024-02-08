import requests
from io import BytesIO

from PyQt5.QtGui import QPixmap

api_server = "http://static-maps.yandex.ru/1.x/"


def get_map(lon: str, lat: str, delta: str, ltype='map'):
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        'l': f"{ltype}"
    }
    response = requests.get(api_server, params=params)
    if not response:
        # обработка ошибочной ситуации
        return None
    img = BytesIO(response.content)
    qpixmap = QPixmap()
    qpixmap.loadFromData(img.read())
    return qpixmap
