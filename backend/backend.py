import requests
from io import BytesIO
from PIL import Image

api_server = "http://static-maps.yandex.ru/1.x/"


def get_map(lon: str, lat: str, delta: str):
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)
    if not response:
        # обработка ошибочной ситуации
        return None
    img = Image.open(BytesIO(
        response.content))
    return img
