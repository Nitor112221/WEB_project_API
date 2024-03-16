import requests
from io import BytesIO

from PyQt5.QtGui import QPixmap

api_server_static_maps = "http://static-maps.yandex.ru/1.x/"
api_server_geocode = "http://geocode-maps.yandex.ru/1.x/"

apikey = "40d1649f-0493-4b70-98ba-98533de7710b"


def get_map(lon: str, lat: str, delta: str, ltype='map', flags=""):
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        'l': f"{ltype}"
    }
    if flags != "":
        params["pt"] = flags
    response = requests.get(api_server_static_maps, params=params)
    if not response:
        # обработка ошибочной ситуации
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
    img = BytesIO(response.content)
    qpixmap = QPixmap()
    qpixmap.loadFromData(img.read())
    return qpixmap


def get_coordinate(place):
    params = {
        'apikey': apikey,
        'geocode': place,
        'format': 'json'
    }

    response = requests.get(api_server_geocode, params=params)
    if response:
        json_response = response.json()

        try:
            res = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

            coords = res["Point"]["pos"]
            address = res["metaDataProperty"]["GeocoderMetaData"]["text"]

            try:
                post_index = res['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']

            except Exception:
                post_index = '-'

            return coords.split(), address, post_index
        except Exception:
            return None



    else:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
