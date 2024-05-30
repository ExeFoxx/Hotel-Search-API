import json
import telebot
from telebot import types
import logging
from config import TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)


user_data = {}
user_delivery_times = {}
user_states = {}

booking_data_file = 'booking_data.txt'

def get_user_state(user_id):
    return user_states.get(user_id, None)


def update_user_state(user_id, state):
    user_states[user_id] = state


def clear_user_state(user_id):
    user_states.pop(user_id, None)


def generate_back_button():
    return types.KeyboardButton("🔙 Назад")


logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    try:
        with open('static/welcome.webp', 'rb') as sti:
            bot.send_sticker(message.chat.id, sti)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Скидки -%")
        item2 = types.KeyboardButton("Оставить Заявку🚗")
        item3 = types.KeyboardButton("❓Часто задаваемые вопросы")
        item4 = types.KeyboardButton("Instagram📷")
        item5 = types.KeyboardButton("Как Пользоваться Ботом❓")
        markup.add(item1, item2, item3, item4, item5, )

        bot.send_message(message.chat.id,
                         f"Добро пожаловать в АвтоАренду, {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>, бот от ExeFox.",
                         parse_mode='html', reply_markup=markup)
    except FileNotFoundError:
        logging.error("Файл приветственного стикера не найден.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {type(e).__name__}, {str(e)}")


def send_back_button(chat_id, text):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = generate_back_button()
    markup.add(back_button)
    bot.send_message(chat_id, text, reply_markup=markup)


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


@bot.message_handler(func=lambda message: message.text == "Instagram📷")
def handle_instagram_button(message):
    instagram_url = "https://www.instagram.com/autoarenda_org/"
    instagram_image_url = "https://th.bing.com/th/id/OIG1.Ox7kojaGCSw8UJMRhAKW?pid=ImgGn"  # Замените на фактический URL изображения


    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Перейти в Instagram", url=instagram_url)
    markup.add(button)

    # Отправляем изображение с кнопкой
    bot.send_photo(message.chat.id, instagram_image_url, reply_markup=markup)


def save_rental_info(rental_info):
    try:
        with open('rental_orders.txt', 'a', encoding='utf-8') as f:
            f.write(str(rental_info) + '\n')
    except Exception as e:
        logging.error(f"Ошибка при сохранении информации о заказе: {type(e).__name__}, {str(e)}")


def save_to_file(filename, data):
    try:
        with open(filename, 'a') as f:
            f.write(str(data) + '\n')
    except Exception as e:
        logging.error(f"Ошибка при сохранении данных: {type(e).__name__}, {str(e)}")


@bot.message_handler(func=lambda message: message.text == 'Оставить Заявку🚗')
def handle_message(message):
    if message.text == 'Оставить Заявку🚗':
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("Toyota", callback_data='brand_1'),
                   InlineKeyboardButton("Ford", callback_data='brand_2'),
                   InlineKeyboardButton("Honda", callback_data='brand_3'),
                   InlineKeyboardButton("Volkswagen", callback_data='brand_4'))
        markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
        bot.send_message(message.from_user.id, 'Select a car brand', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Invalid command')




    user_data = 'BMW'
    with open('booking_data.txt', 'w') as f:
        f.write(str(user_data))

@bot.callback_query_handler(func=lambda call: True)
def handle_message(call):
    if call.data.startswith('brand_'):
        handle_callback_query(call)
    elif call.data.startswith('model_'):
        callback_query_handler_year(call)
    elif call.data.startswith('year'):
        select_month(call)
    elif call.data.startswith('month'):
        show_delivery_times(call)
    elif call.data.startswith('month'):
        confirm_booking(call)
    elif call.data == 'main_menu':
        bot.send_message(call.message.chat.id, 'Back to main menu')
        with open('booking_data.txt', 'w') as f:
            f.write('')
    elif call.data.startswith('time'):
        confirm_booking(call)
        with open('booking_data.txt', 'w') as f:
            f.write(json.dumps(user_data))


def handle_callback_query(call):
    if call.data.startswith('brand_'):
        selected_car_brand = int(call.data[6:]) - 1
        car_brands = ["Toyota", "Ford", "Honda", "Volkswagen"]
        car_models = {
            "Toyota": ["Corolla", "Camry", "RAV4", "Highlander"],
            "Ford": ["Focus", "Fusion", "Mustang", "Explorer"],
            "Honda": ["Civic", "Accord", "CR-V", "Pilot"],
            "Volkswagen": ["Golf", "Jetta", "Passat", "Tiguan"]
        }
        markup = InlineKeyboardMarkup()
        for i in range(len(car_models[car_brands[selected_car_brand]])):
            markup.row(InlineKeyboardButton(car_models[car_brands[selected_car_brand]][i], callback_data=f"model_{i+1}"))
        markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
        bot.send_message(call.message.chat.id, 'Select a car model', reply_markup=markup)
    elif call.data.startswith('model_'):
        selected_car_model = int(call.data[6:]) - 1
        bot.send_message(call.message.chat.id, f"You selected {call.data[6:]}", reply_markup=InlineKeyboardMarkup())
    elif call.data == 'main_menu':
        bot.send_message(call.message.chat.id, 'Main menu', reply_markup=InlineKeyboardMarkup())




def callback_query_handler_year(call):
    markup = InlineKeyboardMarkup()
    for i in range(1):
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("2024", callback_data=f'year'),
                   InlineKeyboardButton("2025", callback_data=f'year'),
                   InlineKeyboardButton("2026", callback_data=f'year'))
        markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
        bot.send_message(call.message.chat.id, 'Please select a year', reply_markup=markup)
    with open('booking_data.txt', 'w') as f:
        f.write(str(user_data))

def select_month(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("January", callback_data=f"month_1"),
                   InlineKeyboardButton("February", callback_data=f"month_2"),
                   InlineKeyboardButton("March", callback_data=f"month_3"),
                   InlineKeyboardButton("April", callback_data=f"month_4"),
                   InlineKeyboardButton("May", callback_data=f"month_5"))
    markup.row(InlineKeyboardButton("June", callback_data=f"month_6"),
                   InlineKeyboardButton("July", callback_data=f"month_7"),
                   InlineKeyboardButton("August", callback_data=f"month_8"),
                   InlineKeyboardButton("September", callback_data=f"month_9"),
                   InlineKeyboardButton("October", callback_data=f"month_10"))
    markup.row(InlineKeyboardButton("November", callback_data=f"month_11"),
                   InlineKeyboardButton("December", callback_data=f"month_12"))
    markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
    bot.send_message(call.message.chat.id, 'Please select a month', reply_markup=markup)

    if call.data.startswith('month_'):
        user_data['selected_month'] = call.data[6:]
    save_user_data()

def save_user_data():
    with open('booking_data.txt', 'w') as f:
        f.write(str(user_data))

def show_delivery_times(call):
    markup = InlineKeyboardMarkup()
    for hour in range(0, 24, 3):
        markup.row(InlineKeyboardButton(f"{hour}:00", callback_data=f"time_{hour}:00"),
                   InlineKeyboardButton(f"{hour}:30", callback_data=f"time_{hour}:30"),
                   InlineKeyboardButton(f"{hour+1}:00", callback_data=f"time_{hour+1}:00"),
                   InlineKeyboardButton(f"{hour+1}:30", callback_data=f"time_{hour+1}:30"),
                   InlineKeyboardButton(f"{hour+2}:00", callback_data=f"time_{hour+2}:00"))
    bot.send_message(call.message.chat.id, 'Select a time', reply_markup=markup)
    with open('booking_data.txt', 'w') as f:
        f.write(str(user_data))


def confirm_booking(call):
    bot.send_message(call.message.chat.id, 'Booking confirmed!')
    with open('booking_data.txt', 'w') as f:
        f.write(str(user_data))
    bot.send_message(call.message.chat.id, 'Your booking details: \nModel: {}\nBrand: {}\nYear: {}\nMonth: {}\nTime: {}'.format(user_data.get('model', 'N/A'), user_data.get('brand', 'N/A'), user_data.get('year', 'N/A'), user_data.get('month', 'N/A'), call.data[5:]))


if __name__ == '__main__':
    bot.polling(none_stop=True)
