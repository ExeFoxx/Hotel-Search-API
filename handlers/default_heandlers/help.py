from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot
from states.search_info import UsersStates
from loguru import logger


@bot.message_handler(commands=['help'])
@logger.catch
def bot_help(message: Message):
    """
    Функция, реагирующая на команду 'help'. Выводит сообщение со списком команд.

    :param message: сообщение Telegram
    """

    bot.delete_state(message.from_user.id, message.chat.id)
    text = [f'<b>/{command}</b> - {desk}' for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, '\n'.join(text), parse_mode='html')


@bot.message_handler(state=UsersStates.last_command)
@logger.catch
def bot_a_help(message: Message):
    """
    Функция, ожидающая ввод новой команды после предыдущего опроса..

    :param message: сообщение Telegram
    """

    bot.delete_state(message.from_user.id, message.chat.id)
    text = [f'<b>/{command}</b> - {desk}' for command, desk in DEFAULT_COMMANDS]
    bot.send_message(message.from_user.id, '\n'.join(text), parse_mode='html')
