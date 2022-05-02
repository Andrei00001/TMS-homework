"""
0. Исправить все нюансы, которые были озвучены во время проверки домашки на последнем уроке.
1. Создать модуль `exceptions`, в нем класс `ValidationError`, который наследуется от `Exception`. Никакие методы,
   свойства переопределять не нужно, необходимо только описать в docstring, что это класс ошибки валидации данных.
2. Создать модуль `validator`, в котором:
    1. Реализовать класс `Data`, конструктор которого принимает `name` и `age` аргументы, сохраняет их в одноименные
       переменные экземпляра класса. Так же у этого класса должен быть метод `_clear_whitespaces`, который очищает от
       пробелов в на+-чале и в конце переменные `name` и `age` у экземпляра класса. Вызывать метод `_clear_whitespaces`
       необходимо из конструктора класса.
    2. Реализовать класс `DataWithDate`, наследовавшись от класса `Data`. Конструктор должен делать то же самое, что и
       родительский класс, но дополнительно сохраяняет текущее время, когда был создан этот экземпляр класса (
       см. `datetime.utcnow`).
    3. Реализовать класс `Validator`. У класса `Validator` должны быть следующие методы:
        1. конструктор класса — в экземпляре класса создает переменную `data_history`, которая является пустым списком,
           но будет хранить объекты класса `Data`.
        2. `_validate_name` — валидация имени (скопировать код из функции `validate_name`).
        3. `_validate_age` — валидация возраста (скопировать код из функции `validate_age`).
        4. `validate` — принимает аргумент `data` (объект класса `Data`) и сохраняет в список `data_history`. Далее
           запускает методы валидации, описанные выше.

       При этом методы `_validate_name` и `_validate_age` должны брать имя и возраст из
       переменной `Validator.data_history` (самое последнее значение). А также выбрасывать исключения `ValidationError`
       вместо `Exception`. Если переменная `data_history` пуста, тогда выбрасывать исключение `ValueError`.

3. В вашем основном файле, где вся текущая домашка:
    1. В самом верху необходимо импортировать класс `Validator` из модуля `validator`.
    2. В самом верху необходимо импортировать класс `ValidationError` из модуля `exceptions`.
    3. В функции `main` до цикла создать объект класса. Вызвать метод `validate` вместо тех функций валидаций, которые
       были написаны в домашках ранее - эти функции необходимо удалить из этого файла. Обрабатывать
       ошибку `ValidationError` вместо `Exception`.
    4. После того как пользователь ввел данные, необходимо создать объект класса `DataWithDate` и далее работать только
       с ним.
    5. Теперь количество попыток ввода данных должно выводиться только в том случае, если пользователь не смог с первого
       раза ввести верные данные. (А еще придумайте как можно избавиться от счетчика попыток).
    6. После ввода верных данных и до запуска игры необходимо показать пользователю:
       1. Общее количество попыток
       2. Время первой попытки, время последней попытки
       3. Сколько времени понадобилось пользователю, чтобы от первой попытки дойти к последней (формат HH:MM:SS, где HH
        - часы, MM - минуты, SS - секунды)
"""

from random import randint
from exceptions import ValidationError
from validator import Validator
from validator import DataWithDate
from datetime import datetime

__author__ = "Andrei Sherlat"


def get_passport_advice(answer: int) -> str:
    """
    :param answer: Accepts integer argument
    :return: String error
    Function accepts answer and checks if it matches the conditions
    """

    if 16 <= answer <= 17:
        return "\nнужно не забыть получить первый паспорт "
    elif 25 <= answer <= 26:
        return "\nнужно заменить паспорт "
    elif 45 <= answer <= 46:
        return "\nнужно второй раз заменить паспорт "


def guess_number_game() -> None:
    """
    function game
    Generates a random number from 1 to 10 and asks the user to guess it until  it succeeds
    Shows the user the number of tries after guessing the number
    """
    a = randint(1, 5)
    print(a)
    error_counter = 0

    while True:
        b = input("Guess from 1 to 10: ")
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
        print("We play on, you didn't guess")


def main() -> None:
    """
    The main function in which the user enters a name and age.
Based on this data, an object of the DataWithDate class is created in case of an error.
Error information will be displayed.
And the user will be asked to enter the name and age again showing him what this input attempt is
If the data is entered correctly in relation to the data type.
An object of the Validator class is created that calls the validate function of the Validator class
and passes an object of class DataWithDate into it
If an error occurs in the correctness of data entry, an error will be displayed and the user will be shown what kind of
attempt it is and will be asked to enter data again.
If all data is entered correctly, the user's age will be checked using get_passport_advice with the age argument passed
in
If there is a match in the function, the user will display a greeting and a hint, if not, then only a greeting attacks
at the same time the information was entered
action end time
And the time for which all actions were performed on the entered data until a successful result
And also the user will need to play the game described in the guess_number_game function
    """

    error_counter = 0
    first_time = datetime.utcnow()
    object_validate = Validator()
    while True:
        if error_counter > 0:
            print(error_counter+1, "Attempt")

        name = input("Введите своё имя: ")
        age = input("Укажите ваш возраст: ")

        try:
            object_data_with_date = DataWithDate(name, age)
        except ValueError as error:
            error_counter += 1
            print(f"Oh error type conversions : {error}")
            continue

        last_time = object_data_with_date.cloc

        try:
            object_validate.validate(object_data_with_date)
            # answer = object_validate._validate_age()
            # answer = object_validate._validate_name()

            name = object_data_with_date.name
            age = object_data_with_date.age

        except ValidationError as error:
            error_counter += 1
            print(f"Oh error: {error}")
            continue

        else:
            print(first_time.strftime("%H:%M:%S"), "Время первой попытки")
            print(last_time.strftime("%H:%M:%S"), "Время последней попытки")
            delta = datetime.strptime(str(last_time - first_time), "%H:%M:%S.%f").strftime("%H:%M:%S")
            print(delta, "Понадобилось времени ")
            break

    text = f"Привет {name[0].upper() + name[1:]} тебе уже {age} годиков."
    prompt = get_passport_advice(age)

    if prompt:
        text += prompt
    print(text)

    guess_number_game()


if __name__ == '__main__':
    main()
    print(__author__)
