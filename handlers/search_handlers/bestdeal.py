from telebot.types import Message
from loader import bot
from states.search_info import UsersStates
from handlers import survey_handlers
from loguru import logger


@bot.message_handler(commands=['bestdeal'])
@logger.catch
def bot_best_deal(message: Message):
    """
    Функция, реагирующая на команду 'bestdeal'.
    Записывает состояние пользователя 'last_command' и предлагает ввести город для поиска отелей.

    :param message: Сообщение Telegram
    """

    bot.delete_state(message.from_user.id, message.chat.id)
    bot.set_state(message.from_user.id, UsersStates.cities, message.chat.id)
    bot.send_message(message.from_user.id, 'Введите город')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_command'] = 'bestdeal'
