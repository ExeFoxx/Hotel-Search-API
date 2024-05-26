import telebot
from telebot import types
import logging
from config import TOKEN
from CAR import CAR_BRANDS
from CITIES import CITIES

from questions import questions
from Answers import Answers
bot = telebot.TeleBot(TOKEN)

DELIVERY_TIMES = [f"{hour}:{minute}" for hour in range(8, 20) for minute in ('00', '30')]

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def generate_back_button():
    return types.KeyboardButton("🔙 Назад")

def send_back_button(chat_id, text):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = generate_back_button()
    markup.add(back_button)
    bot.send_message(chat_id, text, reply_markup=markup)

STATE_NAME = 1
STATE_SURNAME = 2
STATE_PASSPORT_NUMBER = 3
STATE_DRIVER_LICENSE = 4
STATE_CONTACT = 5
DELIVERY_TIME = 6

user_data = {}
user_states = {}

def get_user_state(user_id):
    return user_states.get(user_id, None)

def update_user_state(user_id, state):
    user_states[user_id] = state

def clear_user_state(user_id):
    user_states.pop(user_id, None)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    try:
        with open('static/welcome.webp', 'rb') as sti:
            bot.send_sticker(message.chat.id, sti)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Скидки -%")
        item2 = types.KeyboardButton("🚗 Выбор машины")
        item3 = types.KeyboardButton("❓ Часто задаваемые вопросы")
        item4 = types.KeyboardButton("Instagram📷")
        item5 = types.KeyboardButton("Как Пользоваться Ботом❓")
        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(message.chat.id,
                         f"Добро пожаловать в АвтоАренду, {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>, бот от ExeFox.",
                         parse_mode='html', reply_markup=markup)
    except FileNotFoundError:
        logging.error("Файл приветственного стикера не найден.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {type(e).__name__}, {str(e)}")


@bot.message_handler(func=lambda message: message.text == "❓ Часто задаваемые вопросы")
def handle_start(message):
    # Создаем клавиатуру с кнопками вопросов
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    questions = ["Вопрос 1", "Вопрос 2", "Вопрос 3"]  # Замените на фактические вопросы
    for question in questions:
        markup.add(types.KeyboardButton(question))

    # Добавляем кнопку "Назад"
    markup.add(types.KeyboardButton("Назад"))

    # Отправляем пользователю сообщение
    bot.send_message(message.chat.id, "Привет! Выберите вопрос:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Вопрос 1")
def handle_question_1(message):
    # Отправляем ответ на вопрос 1
    bot.send_message(message.chat.id, "Ответ на вопрос 1: ...")  # Замените на фактический ответ


# Добавьте обработчики для остальных вопросов (Вопрос 2, Вопрос 3) аналогично








@bot.message_handler(func=lambda message: message.text == "Instagram📷")
def handle_instagram_button(message):
    instagram_url = "https://www.instagram.com/autoarenda_org/"
    instagram_image_url = "https://th.bing.com/th/id/OIG1.Ox7kojaGCSw8UJMRhAKW?pid=ImgGn"  # Замените на фактический URL изображения

    # Создаем кнопку с ссылкой на Instagram
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Перейти в Instagram", url=instagram_url)
    markup.add(button)

    # Отправляем изображение с кнопкой
    bot.send_photo(message.chat.id, instagram_image_url, reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == 'Подтвердить')
def ask_for_name(message):
    update_user_state(message.from_user.id, STATE_NAME)
    msg = bot.send_message(message.chat.id, "Укажите Имя:")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    if get_user_state(message.from_user.id) == STATE_NAME:
        if message.text.strip() and message.text != 'Подтвердить':
            user_data[message.from_user.id] = {'name': message.text}
            update_user_state(message.from_user.id, STATE_SURNAME)
            msg = bot.send_message(message.chat.id, "Укажите Фамилию:")
            bot.register_next_step_handler(msg, process_surname_step)
        else:
            msg = bot.send_message(message.chat.id, "Ошибка: введите имя.")
            bot.register_next_step_handler(msg, process_name_step)

def process_surname_step(message):
    if get_user_state(message.from_user.id) == STATE_SURNAME:
        if message.text.strip() and message.text != 'Подтвердить':
            user_data[message.from_user.id]['surname'] = message.text
            update_user_state(message.from_user.id, STATE_PASSPORT_NUMBER)
            msg = bot.send_message(message.chat.id, "Укажите Номер Паспорта:")
            bot.register_next_step_handler(msg, process_passport_step)
        else:
            msg = bot.send_message(message.chat.id, "Ошибка: введите фамилию.")
            bot.register_next_step_handler(msg, process_surname_step)

def process_passport_step(message):
    if get_user_state(message.from_user.id) == STATE_PASSPORT_NUMBER:
        if message.text.strip() and message.text != 'Подтвердить':
            user_data[message.from_user.id]['passport_number'] = message.text
            update_user_state(message.from_user.id, STATE_DRIVER_LICENSE)
            msg = bot.send_message(message.chat.id, "Укажите номер водительских прав:")
            bot.register_next_step_handler(msg, process_driver_license_step)
        else:
            msg = bot.send_message(message.chat.id, "Ошибка: введите номер паспорта.")
            bot.register_next_step_handler(msg, process_passport_step)

def process_driver_license_step(message):
    if get_user_state(message.from_user.id) == STATE_DRIVER_LICENSE:
        if message.text.strip() and message.text != 'Подтвердить':
            user_data[message.from_user.id]['driver_license'] = message.text
            update_user_state(message.from_user.id, STATE_CONTACT)
            msg = bot.send_message(message.chat.id, "Укажите мессенджер для связи или местный номер:")
            bot.register_next_step_handler(msg, process_contact_step)
        else:
            msg = bot.send_message(message.chat.id, "Ошибка: введите номер водительских прав.")
            bot.register_next_step_handler(msg, process_driver_license_step)

def process_contact_step(message, process_time_step):
    if get_user_state(message.from_user.id) == STATE_CONTACT:
        if message.text.strip() and message.text != 'Подтвердить':
            user_data[message.from_user.id]['contact'] = message.text
            update_user_state(message.from_user.id, DELIVERY_TIME)
            msg = bot.send_message(message.chat.id, "Выберите время:")
            bot.register_next_step_handler(msg, process_time_step)
        else:
            msg = bot.send_message(message.chat.id, "Ошибка: введите контактные данные.")
            bot.register_next_step_handler(msg, process_contact_step)

@bot.message_handler(func=lambda message: get_user_state(message.from_user.id) == STATE_CONTACT)
def process_contact_step(message):
    if message.text:
        user_data[message.from_user.id]['contact'] = message.text
        bot.send_message(message.chat.id, "Спасибо, ваш заказ принят.")
        save_rental_info(user_data[message.from_user.id])
        clear_user_state(message.from_user.id)
        user_data.pop(message.from_user.id, None)
    else:
        msg = bot.send_message(message.chat.id, "Ошибка: введите контактные данные.")
        bot.register_next_step_handler(msg, process_contact_step)

def save_rental_info(rental_info):
    try:
        with open('rental_orders.txt', 'a', encoding='utf-8') as f:
            f.write(str(rental_info) + '\n')
    except Exception as e:
        logging.error(f"Ошибка при сохранении информации о заказе: {type(e).__name__}, {str(e)}")

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == "🔙 Назад":
        welcome(message)
        return

    rental_info = {}
    try:
        if message.chat.type == 'private':
            if message.text == 'Скидки -%':
                bot.send_message(message.chat.id, 'Сейчас у нас нет активных скидок. Пожалуйста, проверьте позже.')
            elif message.text == '🚗 Выбор машины':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for brand in CAR_BRANDS.keys():
                    if CAR_BRANDS[brand]:
                        item = types.KeyboardButton(brand)
                        markup.add(item)
                back_button = generate_back_button()
                markup.add(back_button)
                bot.send_message(message.chat.id, "Выберите марку автомобиля:", reply_markup=markup)
            elif message.text in CAR_BRANDS.keys():
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for model in CAR_BRANDS[message.text]:
                    item = types.KeyboardButton(model)
                    markup.add(item)
                back_button = generate_back_button()
                markup.add(back_button)
                rental_info['brand'] = message.text
                bot.send_message(message.chat.id, f"Вы выбрали {message.text}. Теперь выберите модель и год:", reply_markup=markup)
            elif any(model in message.text for model in sum(CAR_BRANDS.values(), [])):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for city in CITIES:
                    item = types.KeyboardButton(city)
                    markup.add(item)
                back_button = generate_back_button()
                markup.add(back_button)
                rental_info['model'] = message.text
                bot.send_message(message.chat.id, f"Вы выбрали {message.text}. Теперь выберите город:", reply_markup=markup)
            elif message.text in CITIES:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for time in DELIVERY_TIMES:
                    item = types.KeyboardButton(time)
                    markup.add(item)
                back_button = generate_back_button()
                markup.add(back_button)
                rental_info['city'] = message.text
                bot.send_message(message.chat.id, "Укажите время доставки от 8:00 до 20:00. Доставка бесплатно:", reply_markup=markup)
            elif message.text in DELIVERY_TIMES:
                rental_info['time'] = message.text
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                confirm_button = types.KeyboardButton("Подтвердить")
                markup.add(confirm_button)
                bot.send_message(message.chat.id, "Пожалуйста, подтвердите ваш заказ, нажав кнопку 'Подтвердить'.", reply_markup=markup)
            else:
                send_back_button(message.chat.id, "Пожалуйста, используйте кнопки для навигации.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {type(e).__name__}, {str(e)}")



bot.polling(none_stop=True)
