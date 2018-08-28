import telebot
from telebot import apihelper

#github acc = 'login: artpybot, password: koro6879849'

apihelper.proxy = {'https':'socks5://392458818:I28QRPUZ@deimos.public.opennetwork.cc:1090'}

bot = telebot.TeleBot('621757628:AAEjOkcNkeewArGDcGMqXfJKuG1tkT5feJo')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Стартую, еба!')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Помоги себе сам!')

@bot.message_handler(commands=['найти'])
def send_welcome(message):
    bot.reply_to(message, 'www.google.ru - гугл хуюгл')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()