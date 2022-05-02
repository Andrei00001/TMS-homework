# 1. Оптимизировать алгоритм
# 2. Переименовать функции на:
#    1. validate_name - проверка имени
#    2. validate_age - проверка возраста
#    3. clear_whitespaces - функция очистки строки от пробелов в начале и конце
#    4. get_passport_advice - функция получения совета по замену паспорту
#    5. guess_number_game - игра "угадай число", где пользователь вводит число и пытается отгадать случайно
#    сгенерированное число от 1 до 5
# 3. Все функции валидации (`validate_name`, validate_age`) должны всегда возвращать `None, а в случае ошибки - делать
# raise Exception(текст ошибки).
# 4. Использовать функцию clear_whitespaces еще и для введенной строки, в которой должно быть число.
# 5. В функции main, необходимо отловить ошибки из функций validate_name, validate_age. Вывести пользователю: "Я поймал
# ошибку: {текст ошибки}". И если были ошибки, тогда вам необходимо заново запросить у пользователя ввод данных.
# 6. В функции main обрабатывать ошибку ValueError (не используем Exception) во время перевода строки к int.
# 7. Перед запросом данных в функции main пользователю должно печататься номер текущей попытки ввода данных.
# Пользователю отображать попытки начиная с 1, в коде попытки должны быть с 0.
# 8. Во время игры "угадай число" тоже должен быть счетчик попыток, который будет отображаться при успешно угаданному
# числу. Пользователю отображать попытки начиная с 1, в коде попытки должны быть с 0.
from random import randint


def validate_age(age1: int):
    """

    :param age1: Принимает число
    :return: Возвращает строку
    Функция проверяет корректно ли введен параметр age1
    """
    if age1 <= 0:
        raise Exception("Чёта с возрастом не то , 0 лет/год либо меньше")
    elif age1 < 14:
        raise Exception("Минимальный возраст 14 лет")


def validate_name(name1: str):
    """

    :param name1: Принимает строку
    :return: Возвращает строку
    Функция проверяет корректно ли введен параметр name1
    """
    if not name1:
        raise Exception("Пустая строка")
    elif name1.count(" ") > 1:
        raise Exception("Проверь корректно ли ввёл имя возможно много пробелов допускается только 1 пробел")
    elif len(name1) < 3:
        raise Exception(f"Минимум 3 символа")


def get_passport_advice(answer: int) -> str:
    """

    :param answer: Принимает число
    :return: Возвращает строку
    Функция принимает аргумент answer и проверяет его на совпадение с условиями
    """

    if 16 <= answer <= 17:
        return "\nнужно не забыть получить первый паспорт "
    elif 25 <= answer <= 26:
        return "\nнужно заменить паспорт "
    elif 45 <= answer <= 46:
        return "\nнужно второй раз заменить паспорт "


def guess_number_game():
    a = randint(1, 5)
    print(a)
    error_counter = 0

    while True:
        b = input("Угадай от 1 до 10: ")
        try:
            b = int(b)
        except ValueError as error:
            print(f"Oh error type conversions : {error}")
            error_counter += 1
            continue
        if b == a:
            print(error_counter + 1, "Attempt")
            break
        error_counter += 1
        print("Играем дальше Ты не угадал")


def clear_whitespaces(name) -> str:
    """
    :return: Возвращает строку
    Функция запрашивает имя и удаляет пробелы спереди и сзади строки, если они имеются
    """
    return name.strip()


def main() -> None:
    """

    :return:
    Главная функция в которой происходит ввод данных , вызов других функцих в цикле при условии,
    на основании того как отработает вызов функци выводится ответ и программа либо завершается либо продолжается
    до мамента пока пользователь не введет правильные данные

    """
    error_counter = 0
    while True:
        print(error_counter + 1, "Attempt")
        name = input("Введите своё имя: ")
        age = input("Укажите ваш возраст: ")
        error_text = ""

        name = clear_whitespaces(name)
        try:
            age = int(clear_whitespaces(age))
        except ValueError as error:
            error_counter += 1
            print(f"Oh error type conversions : {error}")
            continue

        try:
            validate_age(age)
            validate_name(name)
        except Exception as error:
            error_counter += 1
            print(f"Oh error: {error}")
            continue
        else:
            break

    text = f"Привет {name[0].upper() + name[1:]} тебе уже {age} годиков."
    prompt = get_passport_advice(age)
    if prompt:
        text += prompt
    print(text)

    guess_number_game()


if __name__ == '__main__':
    main()
