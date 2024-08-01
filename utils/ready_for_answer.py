from loader import bot
from typing import Dict, List, Union
from telebot.types import Message, InputMediaPhoto
from utils.get_hotels import parse_hotels, process_hotels_info, get_hotel_info_str, get_hotel_info_str_nohtml
from utils.get_photos import parse_photos, process_photos
from utils.pager_for_paginator import my_pages
from database.db_controller import save_history
from keyboards.inline.paginator import show_paginator
from loguru import logger
import time


@logger.catch()
def low_high_price_answer(message: Message, data: Dict, user: str) -> None:
    """
    Функция делает запросы на парсинг отелей и на обработку полученных данных.
    Если данные получены - вызывает функцию show_info.
    Если в результате какого-либо из запросов получает None - показывает сообщение об ошибке.

    :param message: Сообщение Telegram
    :param data: словарь с данными запроса (город, даты поездки, нужны ли фото)
    :param user: имя пользователя Telegram (username)
    """
    adults_count = data.get('adults_count', 1)
    children_count = data.get('children', 0)
    amount_nights = int((data['end_date'] - data['start_date']).total_seconds() / 86400)

    if data.get('last_command') == 'lowprice':
        sort_order_text = f"самых дешевых отелей в городе <b>{data['city']}</b>\n"
        sort_index = 1
    elif data.get('last_command') == 'review':
        sort_order_text = f"отелей с лучшими отзывами посетителей в городе <b>{data['city']}</b>\n"
        sort_index = 1
    else:
        sort_order_text = f"В ценовом диапазоне <b>от {data['start_price']}$ до {data['end_price']}$</b>\n" \
                f"Максимальная удаленность от центра: <b>{data['end_distance']} Км</b>\n"
        sort_index = 2

    reply_str = f" Ок, ищем: <b>топ {data['amount_hotels']}</b> " \
                f"{sort_order_text}" \
                f"{f'Нужно загрузить фото' if data['need_photo'] else f'Фото не нужны'}" \
                f" — <b>{data['amount_photo']}</b> штук\n" \
                f"Длительность поездки: <b>{amount_nights} ноч.</b> " \
                f"Количество взрослых: <b>{adults_count}</b>.\n" \
                f"Количество детей: <b>{children_count}</b>." \
                f"(с {data['start_date']} по {data['end_date']})."
    loading_animation = ['⌛']
    bot.send_message(message.chat.id, reply_str, parse_mode="html")

    for char in loading_animation:
        bot.send_message(message.chat.id, char, parse_mode="html", disable_web_page_preview=True)

    hotels = parse_hotels(data)
    if hotels:
        result_dict = process_hotels_info(hotels)
        if sort_index == 1:
            if result_dict:
                show_info(message=message, request_data=data, result_data=result_dict, user=user,
                          amount_nights=amount_nights)
            else:
                bot.send_message(message.chat.id, '⚠️ Не удалось загрузить информацию по отелям города!')

        elif sort_index == 2:
            if result_dict:
                new_result_dict = dict()
                for hotel_id, hotel_data in result_dict.items():
                    if len(new_result_dict.keys()) >= data.get('amount_hotels'):
                        break
                    current_distance = hotel_data.get('distance_city_center')
                    if not current_distance:
                        continue
                    if current_distance <= data.get('end_distance'):
                        new_result_dict[hotel_id] = hotel_data
                if new_result_dict:
                    show_info(message=message, request_data=data, result_data=new_result_dict, user=user,
                              amount_nights=amount_nights)
                else:
                    bot.send_message(message.chat.id, '⚠️ Ничего не нашлось! Измените критерии поиска!')
            else:
                bot.send_message(message.chat.id, '⚠️ По вашему запрос ничего не нашлось! Измените критерии поиска!')
    else:
        bot.send_message(message.chat.id, '⚠️ Ошибка. Попробуйте ещё раз!')


@logger.catch()
def get_photos(message: Message, hotel_id: int, amount_photo: int) -> Union[List[str], None]:
    """
    Функция делает запросы на парсинг фото и на обработку полученных данных.
    В результате каждого из запросов может прийти None, тогда выдается сообщение об ошибке и возвращается None

    :param message: сообщение Telegram
    :param hotel_id: id отеля
    :param amount_photo: количество фото
    :return: photos_list - список с url фото или None
    """

    photos_info_list = parse_photos(hotel_id)
    if photos_info_list:
        photos_list = process_photos(photos_info_list, amount_photo)
        if photos_list:
            return photos_list
    bot.send_message(message.chat.id, '⚠️ Ошибка загрузки фото.')
    return None


@save_history
@logger.catch
def show_info(
        message: Message, request_data: Dict, result_data: Dict[int, Dict], user: str, amount_nights: int
) -> None:
    """
    Функция вывода информации по найденным отелям.
    Если пользователь задал вывод фото - Отправляет медиа группу (bot.send_media_group)
    Иначе составляет список со строковой информацией по отелям. Затем присваивает этот список пейджеру 'my_pages'
    и вызывает пагинатор 'show_paginator', который и отобразит результат.

    :param message: Сообщение Telegram
    :param request_data: словарь с данными запроса (город, даты поездки, нужны ли фото)
    :param result_data: словарь с найденными отелями.
    :param user: Имя пользователя Telegram (username) - перехватывается и используется только в декораторе
    для сохранения истории.
    :param amount_nights: Количество ночей.
    """

    hotels_info_list = list()

    for hotel_id, hotel_data in result_data.items():
        if request_data['need_photo']:
            photo_urls = get_photos(message, hotel_id, request_data['amount_photo'])
            if photo_urls:
                hotel_info_str = get_hotel_info_str_nohtml(hotel_data, amount_nights)
                photos = [
                    InputMediaPhoto(media=url, caption=hotel_info_str) if index == 0 else InputMediaPhoto(media=url)
                    for index, url in enumerate(photo_urls)
                ]
                bot.send_media_group(message.chat.id, photos)
            else:
                hotel_info_str = get_hotel_info_str(hotel_data, amount_nights)
                bot.send_message(message.chat.id, hotel_info_str, parse_mode="html", disable_web_page_preview=True)
        else:
            hotel_info_str = get_hotel_info_str_nohtml(hotel_data, amount_nights)
            hotels_info_list.append(hotel_info_str)

    if not request_data['need_photo'] and hotels_info_list:
        my_pages.my_strings = hotels_info_list[:]
        show_paginator(message)