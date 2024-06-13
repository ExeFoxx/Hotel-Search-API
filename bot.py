import telebot
import logging
import http.client
import json

bot = telebot.TeleBot("7065295403:AAE9KQZwaliZkNwJDCaYZ_lan04yysr4Sxw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

conn = http.client.HTTPSConnection("booking-com.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "37743181b7mshf2b9c3606c719adp155920jsn509d1764f0eb",
    'x-rapidapi-host': "booking-com.p.rapidapi.com"
}

conn.request("GET", "/v1/static/cities?country=it&page=0", headers=headers)

res = conn.getresponse()
data = res.read()

conn.close()

# Parse the response data as JSON
data_json = json.loads(data.decode('utf-8'))

bot.infinity_polling()