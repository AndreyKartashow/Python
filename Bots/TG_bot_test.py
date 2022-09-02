from asyncio import queues
from ntpath import join
import telebot
from distutils.cmd import Command
from random import *
import json
import requests


'''
pip install telebot
pip install PyTelegramBotAPI==2.2.3
pip install PyTelegramBotAPI==3.6.7
'''


films = []
# API_URL='здесь находится ссылка на поисковик'

def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii = False))
    print("Наша фильмотека успешно сохранена в файлу films.json")


def load():
    global films
    with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
    print("Фильмотека была успешно загружена")


# API_TOKEN = 'здесь должен находиться токен бота'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id, "Фильмотека была успешно загружена!")
    except:
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властелин колец")
        films.append("Санта Барбара")
        films.append("Матрица")
        bot.send_message(message.chat.id, "Фильмотека была загружена по умолчанию!")

@bot.message_handler(commands=['all'])
def start_message(message):
    bot.send_message(message.chat.id, "Вот что у нас есть:")
    bot.send_message(message.chat.id, ", ".join(films))

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    quest_join = ".".join(quest)
    data = {"queuestion_raw": [quest_join]}
    try:
        res = requests.post(API_URL, json = data, verify = False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Информация не найдена")
    # bot.send_message(message.chat.id, ", ".join(films))


bot.polling()