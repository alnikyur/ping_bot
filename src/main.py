#!/usr/bin/env python3

import os
import telebot
from telebot import types
import time

API_TOKEN="5535550610:AAErrMycyTPXWmTCuM4u_wHsXrU1qAWwlxo"
REMOTE_IP="127.0.0.1"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def run(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("/ping")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Welcome to PING bot!', reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(0.5)
    msg = '''
PING bot menu:
====================
Ping → /ping
Help → /help
Regards,
Bots
====================
    '''
    bot.send_message(message.chat.id, msg)

def ping_():
    ret = os.system('ping -c 4 -t 3 -n -q {} > /dev/null'.format(REMOTE_IP))
    if ret == 0:
        return "The power is UP"
    return "The power is DOWN"

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(0.5)
    bot.send_message(message.chat.id, ping_())

bot.infinity_polling(timeout=10, long_polling_timeout=5)