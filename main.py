# coding: utf-8

import requests


def get_temperature(lat, lng):
    """
    Método que obetem a temperatura de uma determinada região como base nas suas coordenadas
    de latitude e longitude.

    :param lat: latitude
    :param lng: longitude
    :return: temperatura em graus celsius da latitude e longitude informada
    """

    # Verifica se latitude e longitude são numéricos
    try:
        lat = float(lat)
        lng = float(lng)
    except ValueError:
        return

    # Verifica se válidos os valores de latitude e longitude
    if (-90 <= lat <= 90) and (-180 <= lng <= 180):
        key = 'e1ee55658d4a2b28c4841e373c3b3d87'
        url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
        reponse = requests.get(url)
        data = reponse.json()
        temperature = data.get('currently').get('temperature')

        # Verifica termperatura zerada ou vazia
        if not temperature:
            return
        return int((temperature - 32) * 5.0 / 9.0)

    else:
        # Se valores inválidos de latitude ou longitude, retorna vazio
        return