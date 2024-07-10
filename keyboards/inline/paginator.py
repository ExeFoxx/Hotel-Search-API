from loader import bot
from telegram_bot_pagination import InlineKeyboardPaginator
from utils.pager_for_paginator import my_pages
from loguru import logger
from telebot.types import Message, CallbackQuery


@logger.catch
def show_paginator(message: Message) -> None:
    """
    Функция, запускающая пагинатор.

    :param message:  сообщение Telegram.
    """

    bot.delete_message(message.chat.id, message.message_id)
    send_page(message)


@bot.callback_query_handler(func=lambda call: call.data.split('#')[0] == 'hotel')
@logger.catch
def pages_callback(call: CallbackQuery) -> None:
    """
    Функция, реагирующая на нажатие кнопки с пагинацией.

    :param call: отклик клавиатуры.
    """

    page = int(call.data.split('#')[1])
    bot.delete_message(call.message.chat.id, call.message.message_id)
    send_page(call.message, page)


@logger.catch
def send_page(message: Message, page: int = 1) -> None:
    """
    Функция отправляет нужную страницу пагинатора с клавиатурой и ожидает нажатия на кнопку перелистывания.

    :param message: сообщение Telegram.
    :param page: номер страницы для отображения.
    """

    paginator = InlineKeyboardPaginator(len(my_pages.my_strings), current_page=page, data_pattern='hotel#{page}')
    bot.send_message(message.chat.id, my_pages.my_strings[page-1],
                     reply_markup=paginator.markup, parse_mode='Markdown', disable_web_page_preview=True)
