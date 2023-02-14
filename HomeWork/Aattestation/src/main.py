from src.note import Note


def start_program():
    """Запуск программы"""
    Note().show_into()
    while True:
        stop = Note().start_program()
        if stop:
            break


if __name__ == '__main__':
    start_program()