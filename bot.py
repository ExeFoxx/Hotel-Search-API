import telebot
from telebot import types
import logging

# Предполагается, что токен бота хранится в модуле config.py
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

CAR_BRANDS = {
    "BMW": ["BMW x1 2020", "BMW 2019", "BMW 2023"],
    "Mercedes": ["Mercedes A-Class 2021"],
    "Audi": ["Audi A4 2022"],
    "Skoda": ["Skoda Octavia 2021"],
    "Clio": ["Clio 4 2019"],
    "Citroen": ["Citroen C3 2020"],
    "Peugeot": ["Peugeot 208 2021"],
    "Volkswagen": ["Volkswagen Golf 2022"]
}

CITIES = ["Подгорица", "Бар", "Цетине", "Андриевица", "Беране", "Биело-Поле", "Будва", "Даниловград", "Жабляк", "Колашин", "Котор", "Мойковац", "Никшич", "Плав", "Плевля", "Плужине", "Рожае", "Тиват", "Улцинь", "Херцег-Нови", "Шавник"]

DELIVERY_TIMES = [f"{hour}:{minute}" for hour in range(8, 21) for minute in ('00', '30')]

# Настройка логирования
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Функция для создания кнопки "Назад"
def generate_back_button():
    return types.KeyboardButton("🔙 Назад")

# Функция для отправки сообщения с кнопкой "Назад"
def send_back_button(chat_id, text):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = generate_back_button()
    markup.add(back_button)
    bot.send_message(chat_id, text, reply_markup=markup)

@bot.message_handler(commands=['start'])
def welcome(message):
    try:
        # Предполагается, что файл 'static/welcome.webp' существует в директории проекта
        with open('static/welcome.webp', 'rb') as sti:
            bot.send_sticker(message.chat.id, sti)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Скидки -%")
        item2 = types.KeyboardButton("🚗 Выбор машины")
        item3 = types.KeyboardButton("❓ Часто задаваемые вопросы")

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id,
                         f"Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>, бот созданный опытной Лисой.",
                         parse_mode='html', reply_markup=markup)
    except FileNotFoundError:
        logging.error("Файл приветственного стикера не найден.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {type(e).__name__}, {str(e)}")

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == "🔙 Назад":
        welcome(message)
        return

    rental_info = {}  # Словарь для хранения информации о заказе
    try:
        if message.chat.type == 'private':
            if message.text == 'Скидки -%':
                bot.send_message(message.chat.id, 'Сейчас у нас нет активных скидок. Пожалуйста, проверьте позже.')
            elif message.text == '🚗 Выбор машины':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for brand in CAR_BRANDS.keys():
                    if CAR_BRANDS[brand]:  # Проверяем, есть ли доступные модели
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
            elif message.text == 'Подтвердить':
                bot.send_message(message.chat.id, "Пожалуйста, укажите 'Имя', 'Фамилию', 'Номер Паспорта', год выдачи и срок действия, номер водительских прав, мессенджер для связи или местный номер.")
            else:
                # Предполагаем, что пользователь ввел личную информацию
                personal_info = message.text.split(',')
                if len(personal_info) >= 5:  # Простая проверка на количество элементов
                    rental_info['personal_info'] = {
                        'name': personal_info[0].strip(),
                        'surname': personal_info[1].strip(),
                        'passport_number': personal_info[2].strip(),
                        'driver_license': personal_info[3].strip(),
                        'contact': personal_info[4].strip()
                    }
                    # Сохраняем информацию о заказе в файл
                    with open('rental_orders.txt', 'a', encoding='utf-8') as f:
                        f.write(str(rental_info) + '\n')
                    bot.send_message(message.chat.id, "Ваш заказ успешно сохранен. Скоро с вами свяжется наш менеджер.")
                else:
                    bot.send_message(message.chat.id, "Пожалуйста, укажите всю необходимую информацию.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {type(e).__name__}, {str(e)}")

# RUN
bot.polling(none_stop=True)
