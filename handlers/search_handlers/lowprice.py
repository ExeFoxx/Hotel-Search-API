from loader import bot
from telebot.types import Message
from states.search_info import UsersStates
from handlers import survey_handlers
from loguru import logger


@bot.message_handler(commands=['lowprice'])
@logger.catch
def bot_low_price(message: Message) -> None:
    """
    Функция, реагирующая на команду 'lowprice'.
    Записывает состояние пользователя 'last_command' и предлагает ввести город для поиска отелей.

    :param message: Сообщение Telegram
    """

    bot.delete_state(message.from_user.id, message.chat.id)  # перед началом опроса зачищаем все собранные состояния
    bot.set_state(message.from_user.id, UsersStates.cities, message.chat.id)
    bot.send_message(message.from_user.id, 'Введите город')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_command'] = 'lowprice'
