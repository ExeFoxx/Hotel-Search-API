from telebot.handler_backends import State, StatesGroup


class UsersStates(StatesGroup):
    """
    Класс реализует состояние пользователя внутри сценария.
    Атрибуты заполняются во время опроса пользователя. Очищаются при каждой новой команде.

    Attributes:
        last_command (str): Команда, которую ввёл пользователь.
        city (str): Город, в котором ищем отели.
        city_id (str): id города, в котором ищем отели.
        cities (Dict): Подходящие по названию города, из которых пользователь выбирает нужный ему.
        amount_hotels (int): Количество отелей.
        need_photo (bool): Нужно ли загружать фото.
        amount_photo (int): Количество фото.
        start_date (datetime.date): Дата заезда в отель.
        end_date (datetime.date): Дата выезда из отеля.
        start_price (int): Минимальная цена за ночь.
        end_price (int): Максимальная цена за ночь.
        end_distance (float): Максимальная дистанция до центра города.
    """
    last_command = State()
    city = State()
    city_id = State()
    cities = State()
    amount_hotels = State()
    need_photo = State()
    amount_photo = State()
    start_date = State()
    end_date = State()
    start_price = State()
    end_price = State()
    end_distance = State()
