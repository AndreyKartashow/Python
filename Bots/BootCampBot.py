from distutils.cmd import Command
from random import *
import json


films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii = False))
    print("Наша фильмотека успешно сохранена в файлу films.json")


def load():
    with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
    print("Фильмотека была успешно загружена")


try:
    load()
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Санта Барбара")
    films.append("Матрица")


while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Фильмотека начала работать")
    elif command == "/stop":
        print("Фильмотека закончила свою работу, заходите к нам еще!")
        save()
        break
    elif command == "/all":
        print("Вот список всех фильмов")
        print(films)
    elif command == "/add":
        new_film = input("Введите название фильма ")
        films.append(new_film)
        print(f"Фильм {new_film} добавлен")
    elif command == "/delete":
        film_remove = input("Введите фильм, который хотите удалить из списка ")
        '''
        if film_remove in films:
            films.remove(film_remove)
            print("Фильм удален из списка")
        else:
            print("Такого фильма нет в списке")
        '''
        try:
            films.remove(film_remove)
            print("Фильм удален из списка")
        except:
            print("Такого фильма нет в списке")
    elif command == "/random":
        # rnd_film = randint(0, len(films)-1)
        # print(f"Вам предложен фильм {films[rnd_film]}")
        print (f"Вам предложен фильм <<{choice (films)}>>")
    elif command == "/help":
        print("Здесь какой то мануал")
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Неопознанная команда. Изучите мануал с помощью команды /help")
