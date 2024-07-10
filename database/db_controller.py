import re
from telebot.types import Message, CallbackQuery
from database.models import db, User, History, SearchResult
from utils.get_hotels import get_hotel_info_str_nohtml
from datetime import datetime
from loader import bot
from typing import Callable
import functools
from keyboards.inline.history_result_choice import print_histories
from keyboards.inline.paginator import show_paginator
from utils.factories import for_history
from utils.pager_for_paginator import my_pages
from loguru import logger


@logger.catch
def save_user(message: Message) -> None:
    """
    Функция сохранения имени пользователя.
    Проверяет наличие пользователя в БД и, если его нет, заносит в БД в таблицу 'users'.

    :param message: Сообщение.
    """

    with db:
        username = message.from_user.username
        try:
            user_id = User.get(User.name == username)
        except Exception:
            user_id = None
        if not user_id:
            User(name=username).save()


@logger.catch
def save_history(func: Callable) -> Callable:
    """
     Декоратор для сохранения истории поиска в БД.
     Забирает данные из декорируемой функции и сохраняет в таблицы 'histories' и 'results'.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        now = datetime.timestamp(datetime.now())

        with db:
            History(
                date=now,
                command=kwargs.get('request_data').get('last_command'),
                city=kwargs.get('request_data').get('city'),
                start_date=kwargs.get('request_data').get('start_date'),
                end_date=kwargs.get('request_data').get('end_date'),
                from_user=kwargs.get('user')
            ).save()

        time = History.select().where(History.from_user == kwargs.get('user') and History.date == now)
        amount_nights = int((kwargs.get('request_data').get('end_date') - kwargs.get('request_data')
                             .get('start_date')).total_seconds() / 86400)
        hotels_list = []
        for hotel_id, hotel_data in kwargs.get('result_data').items():
            hotel_tup = (hotel_id, hotel_data.get('name'), hotel_data.get('price_per_night'),
                         hotel_data.get('total_price'), hotel_data.get('distance_city_center'),
                         hotel_data.get('hotel_url'), hotel_data.get('hotel_neighbourhood'), amount_nights, time)
            hotels_list.append(hotel_tup)

        with db:
            SearchResult.insert_many(hotels_list, fields=[SearchResult.hotel_id, SearchResult.hotel_name,
                                                          SearchResult.price_per_night, SearchResult.total_price,
                                                          SearchResult.distance_city_center, SearchResult.hotel_url,
                                                          SearchResult.hotel_neighbourhood, SearchResult.amount_nights,
                                                          SearchResult.from_date]
                                     ).execute()

        result_func = func(*args, **kwargs)
        return result_func
    return wrapped_func


@logger.catch
def show_history(message: Message, user: str) -> None:
    """
    Функция вывода истории поиска пользователя.
    Предлагает пользователю инлайн-клавиатуру с его прошлыми запросами из таблицы 'histories'.

    :param message: Сообщение.
    :param user: Имя пользователя Telegram (username).
    """

    with db:
        histories = [history for history in History.select().where(History.from_user == user)]
        if histories:
            bot.send_message(message.chat.id, text='Вот ваши прошлые запросы, выбирайте:',
                             reply_markup=print_histories(histories))
        else:
            bot.send_message(message.chat.id,
                             f"<b>Ваша история пуста!</b>\nВведите какую-нибудь команду!\n"
                             f"Например: <b>/help</b>",
                             parse_mode="html")


@bot.callback_query_handler(func=None, history_config=for_history.filter())
@logger.catch
def clarify_history(call: CallbackQuery) -> None:
    """
    Функция ловит нажатие кнопки с выбором старых запросов, формирует результат из БД в список.
    Затем присваивает этот список пейджеру 'my_pages'
    и вызывает пагинатор 'show_paginator', который и отобразит результат.

    :param call: Отклик клавиатуры.
    """

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

    history_date = int(re.search(r'\d+', call.data).group())
    with db:
        results = [result for result in SearchResult.select().where(SearchResult.from_date == history_date)]
        hotels_info_list = list()
        for result in results:
            hotel_data = {
                'name': result.hotel_name,
                'price_per_night': result.price_per_night,
                'total_price': result.total_price,
                'distance_city_center': result.distance_city_center,
                'hotel_url': result.hotel_url,
                'hotel_neighbourhood': result.hotel_neighbourhood
            }
            hotel_info = get_hotel_info_str_nohtml(hotel_data=hotel_data, amount_nights=result.amount_nights)
            hotels_info_list.append(hotel_info)
        my_pages.my_strings = hotels_info_list[:]
        show_paginator(call.message)


@logger.catch
def delete_history(message: Message, user: str) -> None:
    """
    Функция очистки истории поиска пользователя.

    :param message: Сообщение
    :param user: Имя пользователя Telegram (username)
    """

    with db:
        for history in History.select().where(History.from_user == user):
            history_date = History.get(History.date == history.date)
            SearchResult.delete().where(SearchResult.from_date == history_date).execute()
            History.delete_instance(history)
    bot.send_message(message.chat.id,
                     f"<b>История поиска очищена!</b>\n"
                     f"Введите какую-нибудь команду!\nНапример: <b>/help</b>",
                     parse_mode="html")
