from operator import call


import telebot
from telebot import types
import logging
from config import TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot(TOKEN)
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@bot.message_handler(commands=['start'])
def welcome(message):
    try:
        with open('static/welcome.webp', 'rb') as sti:
            bot.send_sticker(message.chat.id, sti)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Скидки -%"),
                    types.KeyboardButton("Оставить Заявку🚗"),
                    types.KeyboardButton("❓Часто задаваемые вопросы"),
                    types.KeyboardButton("Instagram📷"),
                    types.KeyboardButton("Как Пользоваться Ботом❓"))

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


user_data = {}
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

city = {
1: 'Подгорица',
2: 'Бар',
3: 'Цетине',
4: 'Андриевица',
5: 'Беране',
6: 'Биело-Поле',
7: 'Будва',
8: 'Даниловград',
9: 'Жабляк',
10: 'Колашин',
11: 'Котор',
12: 'Мойковац',
13: 'Никшич',
14: 'Плав',
15: 'Плевля',
16: 'Плужине',
17: 'Рожае',
18: 'Тиват',
19: 'Улцинь',
20: 'Херцег-Нови',
21: 'Шавник'
}




@bot.message_handler(func=lambda message: message.text == 'Оставить Заявку🚗')
def get_first_name(message):
    user_data['first_name'] = message.text
    bot.send_message(message.chat.id, 'Пожалуйста, введите свое Имя:')
    bot.register_next_step_handler(message, get_second_name_input)

def get_second_name_input(message):
    user_data['first_name'] = message.text
    bot.send_message(message.chat.id, 'Пожалуйста, введите свою Фамилию:')
    bot.register_next_step_handler(message, get_last_name_input)

def get_last_name_input(message):
    user_data['last_name'] = message.text
    bot.send_message(message.chat.id, 'Пожалуйста, введите свой номер телефона:')
    bot.register_next_step_handler(message, get_phone_number_input)

def get_phone_number_input(message):
    user_data['phone_number'] = message.text
    user_data['full_name'] = f"{user_data['first_name']} {user_data['last_name']}"
    bot.send_message(message.chat.id, 'Выберете Марку Машины:')
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Toyota", callback_data="brand_1"),
               InlineKeyboardButton("Ford", callback_data='brand_2'),
               InlineKeyboardButton("Honda", callback_data='brand_3'),
               InlineKeyboardButton("Volkswagen", callback_data='brand_4'))
    markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
    bot.send_message(message.chat.id, 'Выберете Марку Машины', reply_markup=markup)






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
        bot.send_message(call.message.chat.id, f'Вы выбрали день {user_data["day"]}.')
        show_delivery_times(call)
    elif call.data.startswith('time'):
        user_data['time'] = call.data[5:]
        select_city(call)
    elif call.data.startswith('city'):
        city_number = int(call.data[5:])
        user_data['city'] = city_number
        city_names = {'1': 'Подгорица', '2': 'Бар', '3': 'Цетине', '4': 'Андриевица', '5': 'Беране', '6': 'Биело-Поле',
                      '7': 'Будва', '8': 'Даниловград', '9': 'Жабляк', '10': 'Колашин', '11': 'Котор', '12': 'Мойковац',
                      '13': 'Никшич', '14': 'Плав', '15': 'Плевля', '16': 'Плужине', '17': 'Рожае', '18': 'Тиват',
                      '19': 'Улцинь', '20': 'Херцег-Нови', '21': 'Шавник'}
        user_data['city_name'] = city_names.get(str(city_number), 'Unknown city')

        confirm_booking(call)


def andle_callback_query(call):
    if call.data.startswith('brand_'):
        selected_car_brand = int(call.data[6:]) - 1
        markup = InlineKeyboardMarkup()
        for i in range(0, len(car_models[car_brands[selected_car_brand]]), 2):
            if i + 1 < len(car_models[car_brands[selected_car_brand]]):
                markup.row(InlineKeyboardButton(car_models[car_brands[selected_car_brand]][i], callback_data=f"model_{i+1}"),
                           InlineKeyboardButton(car_models[car_brands[selected_car_brand]][i+1], callback_data=f"model_{i+2}"))
            else:
                markup.row(InlineKeyboardButton(car_models[car_brands[selected_car_brand]][i], callback_data=f"model_{i+1}"))
        markup.row(InlineKeyboardButton("Back to main menu", callback_data='main_menu'))
        bot.send_message(call.message.chat.id, 'Выберите модель машины', reply_markup=markup)
    elif call.data.startswith('model_'):
        # не обновляйте user_data['brand']
        selected_car_model = int(call.data[6:]) - 1
        bot.send_message(call.message.chat.id, f"Вы выбрали {call.data[6:]}", reply_markup=InlineKeyboardMarkup())
    elif call.data == 'main_menu':
        # не обновляйте user_data['brand']
        bot.send_message(call.message.chat.id, 'Главное Меню', reply_markup=InlineKeyboardMarkup())



def callback_query_handler_year(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("2024", callback_data=f'year_2024'),
                   InlineKeyboardButton("2025", callback_data=f'year_2025'),
                   InlineKeyboardButton("2026", callback_data=f'year_2026'))
    markup.row(InlineKeyboardButton("Назад в Меню", callback_data='main_menu'))
    bot.send_message(call.message.chat.id, 'Выберите год подачи машины', reply_markup=markup)

def select_month(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Январь", callback_data=f"month_1"),
                   InlineKeyboardButton("Февраль", callback_data=f"month_2"),
                   InlineKeyboardButton("Март", callback_data=f"month_3"),
                   InlineKeyboardButton("Апрель", callback_data=f"month_4"),
                   InlineKeyboardButton("Май", callback_data=f"month_5"))
    markup.row(InlineKeyboardButton("Июнь", callback_data=f"month_6"),
                   InlineKeyboardButton("Июль", callback_data=f"month_7"),
                   InlineKeyboardButton("Август", callback_data=f"month_8"),
                   InlineKeyboardButton("Сентябрь", callback_data=f"month_9"),
                   InlineKeyboardButton("Октябрь", callback_data=f"month_10"))
    markup.row(InlineKeyboardButton("Ноябрь", callback_data=f"month_11"),
                   InlineKeyboardButton("Декабрь", callback_data=f"month_12"))
    markup.row(InlineKeyboardButton("Назад в Меню", callback_data='main_menu'))
    bot.send_message(call.message.chat.id, 'Выберите месяц подачи машины', reply_markup=markup)


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
    bot.send_message(call.message.chat.id, 'Выберите день подачи машины', reply_markup=markup)

def show_delivery_times(call):
    markup = InlineKeyboardMarkup()
    for i in range(7, 20, 3):
        markup.row(
            InlineKeyboardButton(f"{i}:00", callback_data=f"time_{i}:00"),
            InlineKeyboardButton(f"{i+1}:00", callback_data=f"time_{i+1}:00"),
            InlineKeyboardButton(f"{i+2}:00", callback_data=f"time_{i+2}:00")
        )
    bot.send_message(call.message.chat.id, 'Выберите время подачи машины', reply_markup=markup)

def select_city(call):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("Подгорица", callback_data=f"city_1"),
                   InlineKeyboardButton("Бар", callback_data=f"city_2"),
                   InlineKeyboardButton("Цетине", callback_data=f"city_3"),
                   InlineKeyboardButton("Андриевица", callback_data=f"city_4"))
    markup.row(InlineKeyboardButton("Беране", callback_data=f"city_5"),
                   InlineKeyboardButton("Биело-Поле", callback_data=f"city_6"),
                   InlineKeyboardButton("Будва", callback_data=f"city_7"),
                   InlineKeyboardButton("Даниловград", callback_data=f"city_8"))
    markup.row(InlineKeyboardButton("Жабляк", callback_data=f"city_9"),
                   InlineKeyboardButton("Колашин", callback_data=f"city_10"),
                   InlineKeyboardButton("Котор", callback_data=f"city_11"),
                   InlineKeyboardButton("Мойковац", callback_data=f"city_12"))
    markup.row(InlineKeyboardButton("Никшич", callback_data=f"city_13"),
                   InlineKeyboardButton("Плав", callback_data=f"city_14"),
                   InlineKeyboardButton("Плевля", callback_data=f"city_15"),
                   InlineKeyboardButton("Плужине", callback_data=f"city_16"))
    markup.row(InlineKeyboardButton("Рожае", callback_data=f"city_17"),
                   InlineKeyboardButton("Тиват", callback_data=f"city_18"),
                   InlineKeyboardButton("Улцинь", callback_data=f"city_19"),
                   InlineKeyboardButton("Херцег-Нови", callback_data=f"city_20"))
    markup.row(InlineKeyboardButton("Вернутся в меню", callback_data='main_menu'))
    bot.send_message(call.message.chat.id, 'Выберите город', reply_markup=markup)




def get_first_last_name(user_name):
    user_name_parts = user_name.split()
    return user_name_parts[0], user_name_parts[-1]


def confirm_booking(call):
    bot.send_message(call.message.chat.id, 'Бронирование подтверждено! С вами скоро свяжется наш менеджер.\n')
    with open('output.txt', 'a', encoding='utf-8') as f:
        f.write(f'{" " * 12}🚗 Данные бронирования 🚗{" " * 20}\n')
        f.write('**************************************************\n')
        f.write(f'Марка: {user_data.get("brand")} 🚗\n')
        f.write(f'{"=" * 50}\n')
        f.write(f'Модель: {user_data.get("model")} 🏎️\n')
        f.write(f'{"=" * 50}\n')
        f.write(f'Год: {user_data.get("year")} \n')
        f.write(f'{"=" * 50}\n')
        f.write(f'Месяц подачи машины: {user_data.get("month_name")} 📅\n')
        f.write(f'{"=" * 50}\n')
        f.write(f'День подачи машины: {user_data.get("day")} \n')
        f.write(f'⏰ Время подачи машины: {user_data.get("time")} ⏰\n')
        f.write(f'{"=" * 50}\n')
        f.write(f'🏠 Город: {city[int(call.data[5:]) - 0]} \n')
        f.write('**************************************************\n')
    bot.send_message(call.message.chat.id, f'Ваши данные бронирования:\n\n{"-" * 50}\n\nМарка: {user_data.get("brand")} 🚗\nМодель: {user_data.get("model")} 🏎️\nГод: {user_data.get("year")} \nМесяц подачи машины: {user_data.get("month_name")} 📅\nДень подачи машины: {user_data.get("day")} \n\nВаше Имя в Телеграмме: {call.from_user.full_name}\n\nВремя подачи машины: {user_data.get("time")} \n\nГород: {city[int(call.data[5:]) - 0]} 🏠\n\n Мы ждём вас ! 👥')
    bot.send_message(866323263,
                     f'Ваши данные бронирования:\n\n{"-" * 50}\n\nМарка: {user_data.get("brand")} 🚗\nМодель: {user_data.get("model")} 🏎️\nГод: {user_data.get("year")} \nМесяц подачи машины: {user_data.get("month_name")} 📅\nДень подачи машины: {user_data.get("day")} \n\nИмя Клиента Телеграмм: {call.from_user.full_name}\n\nВремя подачи машины: {user_data.get("time")} \n\nГород: {city[int(call.data[5:]) - 0]} 🏠\n\n Мы ждём вас ! 👥')
    bot.send_message(call.message.chat.id, 'Если у вас возникнут вопросы или проблемы с бронированием, пожалуйста, позвоните нам по номеру ☎️ 99999999999')

    name = user_data.get('first_name')
    surname = user_data.get('last_name')
    phone_number = user_data.get('phone_number')

    bot.send_message(call.message.chat.id, f'Ваше имя в Телеграмме: {name} {surname}')
    bot.send_message(call.message.chat.id, f'Ваш номер телефона: {phone_number}')

if __name__ == '__main__':
    bot.polling(none_stop=True)