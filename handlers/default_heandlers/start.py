from telebot.types import Message
from loader import bot
from database.db_controller import save_user
from loguru import logger
import requests


@bot.message_handler(commands=['start'])
@logger.catch
def bot_start(message: Message) -> None:

    """
    Функция, реагирующая на команду 'start'. Выводит приветственное сообщение.

    :param message: сообщение Telegram
    """

    save_user(message)
    bot.delete_state(message.from_user.id, message.chat.id)
    image_url = 'https://th.bing.com/th/id/OIG4.Wdk8p5BSuhBcrOKvGRWd?pid=ImgGn'
    response = requests.get(image_url)
    if response.status_code == 200:
        bot.send_photo(message.chat.id, response.content, caption=f"👋 Здраствуйте, {message.from_user.username}! 🙋‍♂️\n"
                                                                  f"Я телеграмм Бот для быстрого поиска Отелей! 🏨\n"
                                                                  f"Можете ввести какую-нибудь команду! 🤔\n"
                                                                  f"Например: <b>/help</b> 📝", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Failed to get the image")


@bot.message_handler(commands=['service'])
@logger.catch
def bot_service(message: Message) -> None:
    """
    Функция, реагирующая на команду 'service'. Выводит информацию о сервисе.
    """
    bot.send_message(message.chat.id, "Сервис: поиск отелей 🏨\n"
                                      "Возможности:\n"
                                      "- поиск отелей в любом городе 🗺️\n"
                                      "- поиск отелей с определенной ценой 💸\n"
                                      "- получение информации о отеле 📊\n"
                                      "Если у вас есть вопросы или вам нужна помощь, обратитесь к нам\n"
                                      "Телеграмм Бот был создан @Jeremiazz. 💡\n"
                                      "Если у вас есть вопросы или предложения, можете написать мне!\n"
                                      "Можете ввести какую-нибудь команду! 🤔\n"
                                      "Например: <b>/help</b> 📝", parse_mode = "html")