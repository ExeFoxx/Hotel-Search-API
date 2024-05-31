import telebot
from telebot import types
import logging
from config import TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot(TOKEN)






booking_data_file = 'booking_data.txt'







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
    bot.send_photo(message.chat.id, instagram_image_url, reply_markup=markup)


car_brands = ["Toyota", "Ford", "Honda", "Volkswagen"]
car_models = {
    "Toyota": ["Corolla", "Camry", "RAV4", "Highlander"],
    "Ford": ["Focus", "Fusion", "Mustang", "Explorer"],
    "Honda": ["Civic", "Accord", "CR-V", "Pilot"],
    "Volkswagen": ["Golf", "Jetta", "Passat", "Tiguan"]
}

brand = {
    'brand_1': 'Toyota',
    'brand_2': 'Ford',
    'brand_3': 'Honda',
    'brand_4': 'Volkswagen'
}

user_data = {}
@bot.message_handler(func=lambda message: message.text == 'Оставить Заявку🚗')
def handle_message(message):
    if message.text == 'Оставить Заявку🚗':
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("Toyota", callback_data="brand_1"),
                   InlineKeyboardButton("Ford", callback_data='brand_2'),
                   InlineKeyboardButton("Honda", callback_data='brand_3'),
                   InlineKeyboardButton("Volkswagen", callback_data='brand_4'))
        markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
        bot.send_message(message.from_user.id, 'Select a car brand', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Invalid command')



@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data.startswith('brand_'):
        user_data['brand'] = {
            '1': 'Toyota',
            '2': 'Ford',
            '3': 'Honda',
            '4': 'Volkswagen'
        }[call.data[6:]]
        andle_callback_query(call)
    elif call.data.startswith('model_'):
        user_data['model'] = {
            "Toyota": ["Corolla", "Camry", "RAV4", "Highlander"],
            "Ford": ["Focus", "Fusion", "Mustang", "Explorer"],
            "Honda": ["Civic", "Accord", "CR-V", "Pilot"],
            "Volkswagen": ["Golf", "Jetta", "Passat", "Tiguan"]
        }[user_data['brand']][int(call.data[6:]) - 1]
        callback_query_handler_year(call)
    elif call.data.startswith('year'):
        user_data['year'] = call.data[5:]
        select_month(call)
    elif call.data.startswith('month'):
        user_data['month'] = int(call.data[6:])  # Convert to int
        month_names = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
                       9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
        user_data['month_name'] = month_names.get(user_data['month'], 'Unknown month')
        day_selector(call)
    elif call.data.startswith('day'):
        user_data['day'] = int(call.data[4:])  # Convert to int
        bot.send_message(call.message.chat.id, f'You selected day {user_data["day"]}.')
        show_delivery_times(call)
    elif call.data == 'main_menu':
        bot.send_message(call.message.chat.id, 'Back to main menu')
    elif call.data.startswith('time'):
        confirm_booking(call)


def andle_callback_query(call):
    if call.data.startswith('brand_'):
        selected_car_brand = int(call.data[6:]) - 1
        markup = InlineKeyboardMarkup()
        for i in range(len(car_models[car_brands[selected_car_brand]])):
            markup.row(InlineKeyboardButton(car_models[car_brands[selected_car_brand]][i], callback_data=f"model_{i+1}"))
        markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
        bot.send_message(call.message.chat.id, 'Select a car model', reply_markup=markup)
    elif call.data.startswith('model_'):
        # не обновляйте user_data['brand']
        selected_car_model = int(call.data[6:]) - 1
        bot.send_message(call.message.chat.id, f"You selected {call.data[6:]}", reply_markup=InlineKeyboardMarkup())
    elif call.data == 'main_menu':
        # не обновляйте user_data['brand']
        bot.send_message(call.message.chat.id, 'Main menu', reply_markup=InlineKeyboardMarkup())




def callback_query_handler_year(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("2024", callback_data=f'year_2024'),
                   InlineKeyboardButton("2025", callback_data=f'year_2025'),
                   InlineKeyboardButton("2026", callback_data=f'year_2026'))
    markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
    bot.send_message(call.message.chat.id, 'Выберете год подачи машины', reply_markup=markup)

def select_month(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Январь", callback_data=f"month_1"),
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
    bot.send_message(call.message.chat.id, 'Выберете месяц подачи машины', reply_markup=markup)


def day_selector(call):
    markup = InlineKeyboardMarkup()
    days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    for day in range(0, len(days), 5):
        markup.row(InlineKeyboardButton(days[day], callback_data=f'day_{days[day]}'),
                   InlineKeyboardButton(days[day+1], callback_data=f'day_{days[day+1]}'),
                   InlineKeyboardButton(days[day+2], callback_data=f'day_{days[day+2]}'),
                   InlineKeyboardButton(days[day+3], callback_data=f'day_{days[day+3]}'),
                   InlineKeyboardButton(days[day+4], callback_data=f'day_{days[day+4]}'))
    bot.send_message(call.message.chat.id, 'Выберете день подачи машины', reply_markup=markup)

def show_delivery_times(call):
    markup = InlineKeyboardMarkup()
    for hour in range(0, 24, 3):
        markup.row(InlineKeyboardButton(f"{hour}:00", callback_data=f"time_{hour}:00"),
                   InlineKeyboardButton(f"{hour}:30", callback_data=f"time_{hour}:30"),
                   InlineKeyboardButton(f"{hour+1}:00", callback_data=f"time_{hour+1}:00"),
                   InlineKeyboardButton(f"{hour+1}:30", callback_data=f"time_{hour+1}:30"),
                   InlineKeyboardButton(f"{hour+2}:00", callback_data=f"time_{hour+2}:00"))
    bot.send_message(call.message.chat.id, 'Выберете время подачи машины', reply_markup=markup)




def confirm_booking(call):
    bot.send_message(call.message.chat.id, 'Бронирование подтверждено! С вами скоро свяжется наш менеджер')
    with open('output.txt', 'a', encoding='utf-8') as f:
        f.write(f'Марка: {user_data.get("brand")}\nМодель: {user_data.get("model")}\nГод: {user_data.get("year")}\nМесяц подачи машины: {user_data.get("month_name")}\nДень подачи машины: {user_data.get("day")}\nВремя подачи машины: {call.data[5:]}\n\n')
    bot.send_message(call.message.chat.id, f'Ваши данные бронирования: \nМарка: {user_data.get("brand")}\nМодель: {user_data.get("model")}\nГод: {user_data.get("year")}\nМесяц подачи машины: {user_data.get("month_name")}\nДень подачи машины: {user_data.get("day")}\nВремя подачи машины: {call.data[5:]}')

if __name__ == '__main__':
    bot.polling(none_stop=True)
