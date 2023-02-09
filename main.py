#!/usr/bin/env python3

import os
import telebot
from telebot import types
import time

#API_TOKEN=os.environ['API_TOKEN']
#REMOTE_IP=os.environ['REMOTE_IP']

global RunPosts
global REMOTE_IP
global status

RunPosts="False"
REMOTE_IP=""
status=""

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['check'])
def check_status(message: telebot.types.Message):
     if RunPosts == "True":
         bot.send_message(message.chat.id,'Bot running status is: '+RunPosts+' And IP is '+REMOTE_IP+'')
     else:
         bot.send_message(message.chat.id,'Bot running status is: '+RunPosts+' And IP is '+REMOTE_IP+'')

@bot.message_handler(commands=['stop'])
def stop(message: telebot.types.Message):
    global RunPosts
    global REMOTE_IP
    if message.text == '/stop':
        RunPosts="False"
        REMOTE_IP=""
        print('Set to False')

# Handle '/start' and '/help'
@bot.message_handler(commands=['ping'])
def ping_manual(message):
    bot.send_message(message.chat.id, """\
Hi there, I am Ping bot.
Enter IP address and i will bring you the status!\
""")
    global RunPosts
    if message.text == '/ping':
        RunPosts = "True"
        print('Set to True')
    bot.register_next_step_handler(message, ping_ip);

def ping():
        global status
        ret = os.system('ping -c 4 -n -q ' + REMOTE_IP)
        if ret == 0:
            print("OK")
            status = "OK"
            return "The power is UP, ip addr is: " + REMOTE_IP
        else:
            print("DOWN")
            status = "DOWN"
            return "The power is DOWN, ip addr is: " + REMOTE_IP

def ping_ip(message):
    global REMOTE_IP
    REMOTE_IP = str(message.text)
    check=""
    while True:
        if RunPosts == "False":
            break
#        if status is not check:
#            bot.send_message(message.chat.id,ping())
        bot.send_message(message.chat.id,ping())
        check=(status)
        time.sleep(30)

bot.infinity_polling(timeout=10, long_polling_timeout=5)

