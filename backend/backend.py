import requests
from io import BytesIO

from PyQt5.QtGui import QPixmap

api_server = "http://static-maps.yandex.ru/1.x/"

apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}"


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


def get_coordinate(place):
    geocoder_request += f'&geocode={place}&format=json'

    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        return toponym_coodrinates
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
