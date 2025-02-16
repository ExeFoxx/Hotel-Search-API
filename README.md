# RapidApi Python Telegram-bot ()

Telegram-бот для анализа сайта [Hotels.com](https://www.hotels.com/) и поиска подходящих пользователю отелей. Работает с API от [Hotels.com](https://www.hotels.com/)

Программа написана на языке **Python** в рамках курсовой работы к курсу Python-basic.

- **Language** (язык): Russian
- **Author** (Автор): @Jeremiazz


## Как запустить бота:
- Установить зависимости: `pip install -r requirements.txt`
- Создать telegram-бота у [BotFather](https://t.me/BotFather) и получить токен
- Получить ключ от rapidapi:
    - Зарегистрироваться на сайте [rapidapi.com](https://rapidapi.com/apidojo/api/hotels4/)
    - Перейти в API Marketplace → категория Travel → Hotels (либо просто перейти по прямой ссылке на документацию [Hotels API Documentation](https://rapidapi.com/apidojo/api/hotels4/))
    - Нажать кнопку **Subscribe to Test**
    - Забрать KEY-
- Создать файл **.env** и прописать там BOT_TOKEN и RAPID_API_KEY так.
- Запустить бота: `python main.py`



## Возможности бота:

**Бот реагирует на команды:**

- **/start** — Запустить бота
- **/help** — Вывести справку
- **/lowprice** — Вывести Топ самых дешёвых отелей в городе
- **/highprice** — Вывести Топ самых дорогих отелей в городе
- **/bestdeal** — Настраиваемый поиск отелей
- **/history** — История поиска
- **/service** — Выводит информацию о сервисе

## Принцип работы

После ввода команд **/lowprice** и **/highprice** бот проводит опрос пользователя:
- город для поездки
- дата заселения в отель и дата выселения
- количество отелей для вывода результата (максимум 10)
- нужно ли загрузить фото отеля
    - количество фото (максимум 10)


При вводе команды **/bestdeal** дополнительно запрашивается:
- диапазон цен в $ за 1 ночь
- максимальная удаленность от центра города


При удачных запросах ведется история поиска. Все запросы и их результат сохраняется в базе данных.

При вводе команды **/history** пользователю предлагается уточнить действие:
- Показать историю поиска — будет показана вся история поисковых запросов пользователя. При нажатии на конкретный запрос выводится результат того поиска.
- Очистить историю — вся история поиска будет удалена из базы данных.
