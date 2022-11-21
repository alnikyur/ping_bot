import time
import os
import telebot
from telebot import types

API_TOKEN=os.environ['API_TOKEN']

# make a connection to bot
bot = telebot.TeleBot(API_TOKEN)
# start and help command
@bot.message_handler(commands=["start"])
def run(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("/ping")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Welcome to PING bot!', reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(0.5)
    msg = '''
PING bot
---------
Ping → /ping
Help → /help
Regards,
Bots
---------
    '''
    bot.send_message(message.chat.id, msg)

import psutil
import subprocess

@bot.message_handler(commands=['ping'])
def nginx_status(message):
    bot.send_chat_action(message.chat.id, "typing")
    time.sleep(0.5)
    cmd = "sh ping.sh"
    ping_status = subprocess.check_output(cmd, shell=True).decode('UTF-8')
    msg = ping_status
    bot.send_message(message.chat.id,msg)

# listen to telegram commands
#bot.polling(none_stop=True, interval=2)
bot.infinity_polling(timeout=10, long_polling_timeout=5)

