from telebot.types import Message
from loader import bot
from loguru import logger


@bot.message_handler(commands=['hello-world'])
@logger.catch
def hello_world(message: Message):
    """
    Функция, реагирующая на команду 'hello-world'.

    :param message: сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.reply_to(message, f"Вы ввели 'hello-world'! Введите команду /help")
