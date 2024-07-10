from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from loguru import logger


@logger.catch
def get_history_action() -> InlineKeyboardMarkup:
    """
    Клавиатура с кнопками - выбор действия с историей поиска.
    :return: клавиатура InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Показать историю поиска', callback_data='show_history'),
        InlineKeyboardButton(text='Очистить историю', callback_data='delete_history')
    )
    return keyboard
