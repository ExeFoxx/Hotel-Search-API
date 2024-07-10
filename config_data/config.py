import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', "Топ самых дешёвых отелей в городе"),
    ('highprice', "Топ самых дорогих отелей в городе"),
    ('bestdeal', "Настраиваемый поиск отелей"),
    ('history', "История поиска")
)
RAPID_API_URL = "https://hotels4.p.rapidapi.com/v2/get-meta-data"
RAPID_API_HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}
RAPID_API_ENDPOINTS = {
    "cities-groups": "https://hotels4.p.rapidapi.com/locations/v3/search",
    "hotel-list": "https://hotels4.p.rapidapi.com/properties/v2/list",
    "hotel-photos": "https://hotels4.p.rapidapi.com/properties/v2/detail"
}

LOG_PATH = os.path.abspath(os.path.join('logs', 'debug.log'))
