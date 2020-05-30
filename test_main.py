from main import *
from unittest.mock import patch
import pytest


# TESTE DE CONVERSÃO FAHRENHITE P/ CELSIUS

list_for_test_conversion = [
    ("-14.235004", "-51.92528", 62, 16),
    ("-17.235004", "-41.92528", 59, 15),
    ("-4.235004", "-57.92528", 50, 10),
    ("-25.235004", "-78.92528", 41, 5)
]

@pytest.mark.parametrize("lat, lng, temperature, expected", list_for_test_conversion)
def test_get_temperature_by_lat_lng(lat, lng, temperature, expected):
    """
    Teste automatizado da classe da função get_temperature() para validação
    da conversão fahrenhite-celsius

    :param mock_requests: requisição mockada
    :param lat: latitude de teste
    :param lng: longitude de teste
    :param expected: valor esperado para a latitude e longitude informada
    """
    with patch("main.requests.get") as mock_requests:
        expected_result = {
            "currently": {
                "temperature": temperature
            }
        }

        # Determina o resultado esperado através do mock
        mock_requests.return_value.json.return_value = expected_result

        resp = get_temperature(lat, lng)
        assert resp == expected


# TESTE SE VALORES NÃO VÁLIDOS DE LATITUDE E LONGITUDE

list_for_test_lat_lng = [
    ("-91", "-51.92528"),
    ("-17.235004", "182"),
    ("97", "-57.92528"),
    ("-95", "-188")
]

@pytest.mark.parametrize("lat, lng", list_for_test_lat_lng)
def test_invalid_lat_lng(lat, lng):
    """
    Teste automatizado da função get_temperature() para validação dos valores
    de latitude e longitude

    :param lat: latitude
    :param lng: longitude
    """
    resp = get_temperature(lat, lng)

    assert resp is None
