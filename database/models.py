from peewee import *
from loader import db


class BaseModel(Model):
    """ Базовый класс для создания таблиц в БД. """

    class Meta:
        database = db


class User(BaseModel):
    """
    Класс для создания таблицы 'users' в БД.

    Attributes:
        id (int): Уникальный id пользователя.
        name (str): Уникальное имя пользователя (сюда запишется username пользователя Telegram).
    """

    id = PrimaryKeyField(unique=True)
    name = CharField(unique=True)

    class Meta:
        db_table = 'users'
        order_by = 'id'


class History(BaseModel):
    """
    Класс для создания таблицы 'histories' в БД.

    Attributes:
        date (datetime.date): Дата запроса пользователя.
        command (str): Команда запроса ('lowprice', 'highprice', 'bestdeal').
        city (str): Город.
        start_date (datetime.date): Дата заселения в отель.
        end_date (datetime.date): Дата выселения из отеля.
        from_user (str): name - Уникальное имя пользователя из таблицы 'users' для связки таблиц.
    """

    date = DateField()
    command = CharField()
    city = CharField()
    start_date = DateField()
    end_date = DateField()
    from_user = ForeignKeyField(User.name)

    class Meta:
        db_table = 'histories'
        order_by = 'date'


class SearchResult(BaseModel):
    """
    Класс для создания таблицы 'results' в БД.

    Attributes:
        hotel_id (int): id отеля.
        hotel_name (str): Название отеля.
        price_per_night (float): Цена за 1 ночь в $.
        total_price (float): Итоговая стоимость за N ночей в $.
        distance_city_center (float): Расстояние до центра города.
        hotel_url (str): url-адрес отеля.
        hotel_neighbourhood (str): Район расположения отеля.
        amount_nights (int): Количество ночей.
        from_date (datetime.date): date - Уникальная дата запроса из таблицы 'histories' для связки таблиц.
    """

    hotel_id = IntegerField()
    hotel_name = CharField()
    price_per_night = FloatField()
    total_price = FloatField()
    distance_city_center = FloatField()
    hotel_url = CharField()
    hotel_neighbourhood = CharField()
    amount_nights = IntegerField()
    from_date = ForeignKeyField(History.date)

    class Meta:
        db_table = 'results'
        order_by = 'price_per_night'
