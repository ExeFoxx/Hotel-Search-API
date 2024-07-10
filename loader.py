from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

from peewee import SqliteDatabase
from loguru import logger

storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
db = SqliteDatabase('search_history.db')
logger.add(config.LOG_PATH, format="{time}, {level}, {message}", level="DEBUG", rotation="1 week", compression="zip")
