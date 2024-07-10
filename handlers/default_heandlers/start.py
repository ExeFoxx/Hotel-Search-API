from telebot.types import Message
from loader import bot
from database.db_controller import save_user
from loguru import logger


@bot.message_handler(commands=['start'])
@logger.catch
def bot_start(message: Message) -> None:
    """
    Функция, реагирующая на команду 'start'. Выводит приветственное сообщение.

    :param message: сообщение Telegram
    """

    save_user(message)
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, f"👋 Здраствуйте, {message.from_user.username}! 🙋‍♂️\n"
                                      f"Я телеграмм Бот для быстрого поиска Отелей! 🏨\n"
                                      f"Можете ввести какую-нибудь команду! 🤔\n"
                                      f"Например: <b>/help</b> 📝", parse_mode="html")
