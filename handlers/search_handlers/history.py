from telebot.types import Message, CallbackQuery
from loader import bot
from keyboards.inline.history_action_choice import get_history_action
from database.db_controller import show_history, delete_history
from loguru import logger


@bot.message_handler(commands=['history'])
@logger.catch
def bot_history(message: Message):
    """
    Функция, реагирующая на команду 'history'.
    Показывает клавиатуру с выбором действия: 'Показать историю поиска' или 'Очистить историю'.

    :param message: Сообщение Telegram.
    """
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.from_user.id, 'Выберите действие:', reply_markup=get_history_action())


@bot.callback_query_handler(func=lambda call: call.data == 'show_history' or call.data == 'delete_history')
@logger.catch
def process_history_reply(call: CallbackQuery) -> None:
    """
    Функция, реагирующая на нажатие кнопки с выбором действия.
    В зависимости он нажатой кнопки вызывает нужную функцию: 'Показать историю поиска' или 'Очистить историю'.

    :param call: Отклик клавиатуры.
    """

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == "show_history":
        try:
            show_history(call.message, user=call.from_user.username)
        except Exception:
            bot.send_message(call.message.chat.id, text='⚠️Упс... ошибка: не могу загрузить историю поиска:')
    elif call.data == "delete_history":
        try:
            delete_history(call.message, user=call.from_user.username)
        except Exception:
            bot.send_message(call.message.chat.id, text='⚠️Упс... ошибка: не могу удалить историю поиска:')
