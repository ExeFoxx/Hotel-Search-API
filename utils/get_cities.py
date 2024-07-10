from typing import Dict, Union
from utils.api_reqiest import request_to_api
from config_data.config import RAPID_API_HEADERS, RAPID_API_ENDPOINTS
import re
import json
from loguru import logger


@logger.catch
def parse_cities_group(city: str) -> Union[Dict[str, str], None]:
    """
    Функция делает запрос в request_to_api и десериализирует результат. Если запрос получен и десериализация прошла -
    возвращает обработанный результат в виде словаря - подходящие города и их id, иначе None.

    :param city: Город для поиска.
    :return: None или словарь с результатом: {'city_name': 'city_id'}
    """

    querystring = {"q": city, "locale": "ru_RU", "langid": "1033", "siteid": "300000001"}

    response = request_to_api(
        method_type='GET',
        url=RAPID_API_ENDPOINTS['cities-groups'],
        payload=querystring,
        headers=RAPID_API_HEADERS)
    data_site = json.loads(response.text)

    cities = dict()

    if data_site.get('sr'):
        city_lst = data_site.get('sr')
        for elem in city_lst:
            for k, v in elem.items():
                if k == 'type' and (v == 'CITY' or v == 'MULTICITY'):
                    city_id = elem.get('gaiaId')
                    city_full_name = elem.get('regionNames').get('fullName')
                    cities[city_full_name] = city_id

    return cities
