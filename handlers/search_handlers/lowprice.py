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
    Записывает состояние пользователя 'last_command' и предлагает ввести количество взрослых.

    :param message: Сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)  # очищаем состояния перед новым опросом
    bot.set_state(message.from_user.id, UsersStates.adults_count, message.chat.id)
    bot.send_message(message.from_user.id, 'Сколько взрослых будет путешествовать?')

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_command'] = 'lowprice'


@bot.message_handler(state=UsersStates.adults_count)
def set_adults_count(message: Message):
    """
    Устанавливает количество взрослых.
    """
    try:
        adults_count = int(message.text)
        if adults_count < 1:
            raise ValueError

        bot.set_state(message.from_user.id, UsersStates.children_count, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['adults_count'] = adults_count

        bot.send_message(message.from_user.id, 'Сколько детей будет путешествовать? (Введите 0, если нет)')
    except ValueError:
        bot.send_message(message.from_user.id, 'Пожалуйста, введите корректное количество взрослых.')


@bot.message_handler(state=UsersStates.children_count)
def set_children_count(message: Message) -> None:
    """
    Устанавливает количество детей и спрашивает их возраст.
    """
    try:
        children_count = int(message.text)
        if children_count < 0:
            raise ValueError

        bot.set_state(message.from_user.id, UsersStates.children_age, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['children'] = children_count

        if children_count > 0:
            bot.send_message(message.from_user.id, 'Введите возраст детей через запятую (например, 5,7):')
        else:
            bot.send_message(message.from_user.id, 'Введите город:')
            bot.set_state(message.from_user.id, UsersStates.cities, message.chat.id)

    except ValueError:
        bot.send_message(message.from_user.id, 'Пожалуйста, введите корректное количество детей.')


@bot.message_handler(state=UsersStates.children_age)
def set_children_age(message: Message) -> None:
    """
    Устанавливает возраст детей.
    """
    try:
        children_ages = list(map(int, message.text.split(',')))

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['children_ages'] = children_ages

        bot.send_message(message.from_user.id, 'Введите город:')
        bot.set_state(message.from_user.id, UsersStates.cities, message.chat.id)

    except ValueError:
        bot.send_message(message.from_user.id, 'Пожалуйста, введите корректные возраста детей через запятую.')
