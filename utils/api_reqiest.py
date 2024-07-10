import json
import requests
from requests.models import Response
from typing import Dict, Union
from loguru import logger


@logger.catch
def request_to_api(method_type, url, payload, headers):

    if method_type == 'GET':
        return get_request(
            method_type=method_type,
            url=url,
            querystring=payload,
            headers=headers
        )
    else:
        return post_request(
            method_type=method_type,
            url=url,
            payload=payload,
            headers=headers
        )


def get_request(method_type, url, querystring, headers):
    try:
        response = requests.request(
            method_type,
            url=url,
            params=querystring,
            headers=headers,
            timeout=15
        )
        if response.status_code == requests.codes.ok:
            return response
    except Exception:
        print('Ошибка запроса "get_request"')


def post_request(method_type, url, payload, headers):
    try:
        response = requests.request(
            method_type,
            url=url,
            json=payload,
            headers=headers,
            timeout=15
        )
        if response.status_code == requests.codes.ok:
            return response
    except Exception:
        print('Ошибка запроса "get_request"')
