from colorama import init


from colorama import Fore

from src.methods import Method


class Note:
    COOMAND_TEXT = "Список команд:\n" \
                   "add - добавить новую запись запись\n" \
                   "show - показать все записи\n" \
                   "filter - фильтровать записи по дате\n" \
                   "delete - удалить запись\n" \
                   "edit - изменить запись\n" \
                   "exit - выйти из программы"

    def __init__(self):
        init()
        self.methods = Method()
        self.commands = {
            'add': self.cmd_add,
            'show': self.cmd_show,
            'delete': self.cmd_delete,
            'edit': self.cmd_edit,
            'filter': self.cmd_filter,
            'exit': self.cmd_exit
        }

    def start_program(self):
        """Основной интерфейс программы"""
        print(Fore.YELLOW + self.COOMAND_TEXT)
        cmd = self.get_command()
        if self.is_correct_cmd(cmd):
            stop = self.commands.get(cmd)()
            if stop:
                return stop
        else:
            print(Fore.RED + f"Вы ввели неверную команду - {cmd}")

    @staticmethod
    def get_command():
        """Получение команды от пользователя"""
        cmd = input(Fore.MAGENTA + ">> ")
        return cmd

    @staticmethod
    def is_correct_cmd(cmd):
        """Проверка на корректность команды"""
        if cmd in ['add', 'show', 'filter', 'delete', 'edit', 'exit']:
            return True
        return False

    def cmd_add(self):
        """Обработчик команды add"""
        title, body = self.get_data_note()
        self.methods.render_note(title, body)
        print(Fore.GREEN + f"Заметка {title} - успешно добавлена!\n")

    def cmd_show(self):
        """Обработчик команды show"""
        notes = self.methods.get_note_all()
        if notes is None:
            print(Fore.RED + "Записей нет, добавь новую!")
        else:
            self.show_notes(notes)

    def cmd_delete(self):
        """Обработчик команды delete"""
        note_pk = self.get_pk_note()
        if self.methods.correct_note_pk(note_pk):
            note = self.methods.delete_json(note_pk)
            self.show_note(note)
            print(Fore.GREEN + "Запись успешно удалена!\n")
        else:
            print(Fore.RED + "Записи с таким номером нет!\n")

    def cmd_edit(self):
        """Обработчик команды edit"""
        note_pk = self.get_pk_note()
        if self.methods.correct_note_pk(note_pk):
            title, body = self.get_new_data_note()
            note = self.methods.edit_note(note_pk, title, body)
            self.show_note(note)
            print(Fore.GREEN + "Успешно изменено!\n")
        else:
            print(Fore.RED + "Запись с таким номером отсутствует!\n")

    def get_date(self):
        """Получение даты"""
        while True:
            print(Fore.YELLOW + "Введите дату в формате: день.месяц.год")
            date = input(Fore.MAGENTA + '>> ')
            date_list = date.split(".")
            if self.check_separator(date_list):
                if date_correct := self.check_date(date_list):
                    return date_correct
            print(Fore.RED + "Проверти разделите межу: день.месяц.год!\n"
                             f"Вы ввели - {date}")

    def check_date(self, date_list: list):
        """Проверка даты на корректность"""
        day = self.check_day(date_list[0])
        month = self.check_month(date_list[1])
        year = self.check_year(date_list[2])
        if not all([day, month, year]):
            return False
        return f'{day}/{month}/{year}'

    def cmd_filter(self):
        """Обработчик команды filter"""
        date_note = self.get_date()
        notes = self.methods.filter_date_notes(date_note)
        if isinstance(notes, list):
            self.show_notes(notes)
        else:
            print(Fore.RED + notes, end="\n")

    @staticmethod
    def cmd_exit():
        """Обработчик команды exit"""
        print(Fore.GREEN + "Выход из программы")
        return True

    @staticmethod
    def check_separator(date):
        """Проверка разделителя меду значениями даты """
        if len(date) == 3 and isinstance(date, list):
            return True
        return False

    @staticmethod
    def check_day(day: str):
        """Проверка дня на корректность"""
        try:
            int_day = int(day)
            if int_day > 31 or int_day == 0:
                print(Fore.RED + "Номер дня недели должен быть: от 1 до 31\n"
                                 f"Вы ввели - {day}")
                return False
            if day[0] == '0':
                return day[1]
            return day
        except ValueError:
            print(Fore.RED + f"Вы ввели неверное значение для дня - {day}")
            return False

    @staticmethod
    def check_month(month: str):
        """Проверка месяца на корректность"""
        if month in ['0', '']:
            print(Fore.RED + "Месяц не может быть меньше 1")
            return False
        if month[0] == '0':
            format_month = month[1]
        else:
            format_month = month
        try:
            int_month = int(format_month)
            if int_month > 12 or int_month < 1:
                print(Fore.RED + "Проверьте корректность месяца, месяц должен быть: от 1 до 12\n"
                                 f"Вы ввели {month}")
                return False
            return format_month
        except ValueError:
            print(Fore.RED + f"Вы ввели неверное значение для месяца - {month}")
            return False

    @staticmethod
    def check_year(year: str):
        """Проверка год на корректность"""
        if len(year) <= 2:
            format_year = '20' + year
        else:
            format_year = year
        try:
            int_year = int(format_year)
            if int_year < 2023:
                print(Fore.RED + "Значение года не может быть меньше чем 2023!\n"
                                 f"Вы ввели - {year}")
                return False
            return format_year
        except ValueError:
            print(Fore.RED + f"Вы ввели неверное значение для года - {year}")
            return False

    def get_pk_note(self):
        """Получения pk от пользователя"""
        notes = self.methods.get_note_all()
        self.show_min_info(notes)
        while True:
            print(Fore.YELLOW + "Введите номер заметки")
            value_pk = input(Fore.MAGENTA + '>> ')
            if note_pk := self.check_pk(value_pk):
                return note_pk

    @staticmethod
    def check_pk(value_pk):
        """Проверка первичного ключа"""
        if value_pk.isdigit() and value_pk != '0':
            return value_pk
        return False

    @staticmethod
    def show_note(note):
        """Выводит одну запись"""
        if isinstance(note, dict):
            print(Fore.GREEN + f'Заметка: {note["title"]}')
        else:
            print(Fore.RED + note)

    @staticmethod
    def show_notes(notes):
        """Выводит список записей"""

        if isinstance(notes, dict):
            for note_pk, value in notes.items():
                print(Fore.YELLOW + f"\nНомер: {note_pk}"
                                    f"{value['title']}\n"
                                    f"{value['body']}\n"
                                    f"{value['date']} {value['time']}")
        else:
            for note in notes:
                for note_pk, value in note.items():
                    print(Fore.YELLOW + f"\nНомер: {note_pk}"
                                        f"{value['title']}\n"
                                        f"{value['body']}\n"
                                        f"{value['date']} {value['time']}")
        print(Fore.BLUE + '-' * 15)

    @staticmethod
    def show_min_info(notes):
        """Выводит краткую информацию о заметке"""
        print(Fore.BLUE + '-' * 15)
        for note_pk, value in notes.items():
            print(Fore.YELLOW + f"Номер: {note_pk} - {value['title'][:10]}")
            print(Fore.BLUE + '-' * 15)

    @staticmethod
    def get_data_note():
        """Получение информации для заметки"""
        print(Fore.YELLOW + 'Названия заметки')
        title = input(Fore.MAGENTA + '>> ')
        print(Fore.YELLOW + 'Контент заметки')
        body = input(Fore.MAGENTA + ">> ")
        return title, body

    @staticmethod
    def get_new_data_note():
        """Получение информации для изменения заметки"""
        print(Fore.YELLOW + 'Новое названия заметки')
        title = input(Fore.MAGENTA + '>> ')
        print(Fore.YELLOW + 'Новый контент заметки')
        body = input(Fore.MAGENTA + ">> ")
        return title, body

    @staticmethod
    def show_into():
        """Вывод названия программы"""
        print(Fore.MAGENTA + "Draft Notes")