from telebot import TeleBot
from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS
from loguru import logger


@logger.catch
def set_default_commands(bot: TeleBot) -> None:
    """
    Функция создает меню из команд.
    :param bot: TeleBot
    """

    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
