# Домашка до понедельника (берём уже то, что вы сделали к последнему уроку):
#
# 0. Обязательно к прочтению Дзен python.
# 1. Создать несколько функций на проверку введённых данных:
# - Проверка имени
# - Проверка возраста
# Функции должны возвращать строку с ошибкой. Если функции вернули ошибки, нужно вывести пользователю ошибки.
# 2. Улучшить проверку имени: в имени между буквами допускается только 1 пробел.
# 3. Сделать совет по получению или замене паспорта (эта задача больше не является со звездочкой) в отдельной функции
# , которая возвращает строку.
# 4. Создать функцию main, в которой будут вызовы всех остальных функций, ввод данных и прочее.
# 5. Создать цикл до тех пор, пока пользователь не введёт верные данные без ошибок.
# 6. Создать функцию, которая очищает введённые данные от лишних пробелов в начале и в конце строки.
# 7. Все функции должны иметь документацию (docstring) (вспоминаем второй урок) и аннотации.
#
#
# И по классике — ограничения:
# - Разрешается использовать только два раза print.
# - Нельзя использовать глобальные переменные.

from random import randint
import re


def age_check(age1: int, name1: str) -> str | None:
    """

    :param age1: Принимает число
    :param name1: Принимает строку
    :return: Возвращает строку
    Функция проверяет корректно ли введен параметр age1
    """
    if age1 <= 0:
        return f"Чёта с возрастом не то , 0 лет/год либо меньше"
    elif age1 < 14 and len(name1) < 3:
        return f"Минимальный возраст 14 лет или Проверь коректно ли ввел имя"
    elif age1 < 14:
        return f"Минимальный возраст 14 лет"


def name_check(name1: str) -> str | None:
    """

    :param name1: Принимает строку
    :return: Возвращает строку
    Функция проверяет корректно ли введен параметр name1
    """
    if name1.count(" ") > 1:
        return "Проверь корректно ли ввёл имя возможно много пробелов допускается только 1 пробел"
    elif len(name1) < 3:
        return f"Минимум 3 символа"


def hint_or_greeting(answer: int, name: str) -> str | None:
    """

    :param name: Принимает строку
    :param answer: Принимает число
    :return: Возвращает строку
    Функция принимает аргумент answer и проверяет его на совпадение с условиями
    """
    text = f"Привет {name[0].upper() + name[1:]} тебе уже {answer} годиков"
    if 16 <= answer <= 17:
        return text+"\nнужно не забыть получить первый паспорт "
    elif 25 <= answer <= 26:
        return text+"\nнужно заменить паспорт "
    elif 45 <= answer <= 46:
        return text+"\nнужно второй раз заменить паспорт "
    return text


def play():
    a = randint(1, 10)
    print(a)
    while True:
        b = int(input("Угадай от 1 до 10: "))
        if b == a:
            break
        print("Играем дальше Ты не угадал")


def clear_name(name) -> str:
    """
    :return: Возвращает строку
    Функция запрашивает имя и удаляет пробелы спереди и сзади строки, если они имеются
    """
    return name.strip(" ")


def main() -> str:
    """

    :return:
    Главная функция в которой происходит ввод данных , вызов других функцих в цикле при условии,
    на основании того как отработает вызов функци выводится ответ и программа либо завершается либо продолжается
    до мамента пока пользователь не введет правильные данные

    """
    repeat_text = "Вводи заново"
    while True:
        name = input("Введите своё имя: ")
        name = clear_name(name)
        age = int(input("Укажите ваш возраст: "))
        param_age = age_check(age, name)
        param_name = name_check(name)
        error = None
        if param_age is not None:
            error = param_age + "\n" + repeat_text
        elif param_name is not None:
            error = param_name + "\n" + repeat_text
        if error is not None:
            print(error)
        else:
            # break
            # Можно грохнуть цикл через break и вынести в не цикла вызов игры и вывод инфы но, какой смысл если
            # вызовется функция с игрой и вернётся значение функции что соответственно закончит вообще какие либо
            # действия в функции
            play()
            return hint_or_greeting(age, name)


def is_palindrome() -> bool:
    """

    :return:
    Првоеряет слово либо строку на палиндром
    """
    # Ввод строки
    line = input("Введите стркоу для проверки на полиндром: ")
    i = 0
    j = len(line) - 1
    # Создаем (*регулярное выражение) которое возвращает нам set(для экономии места если не оборачивать вернёт list)
    # со всеми буквами которые возможны в данной строке
    # result = set(re.findall(r"[a-zA-ZёЁА-Яа-я]", line))
    # print(result)
    if not line:
        print("Ты ничего не ввёл")
        return False
    else:
        while i < j:
            # Циклы на провеку а не идёт ли несколько некоректных символов подряд как с переди так и сзади
            if len(line) == line.count(" "):
                print("Ты ввёл только пробелы вроде как это не палидром ")
                return False
            while not line[i].isalpha():
                i += 1
            while not line[j].isalpha():
                j -= 1
            # Проверка на совпадение символов , если не совпала сразу возвращает False, если совпало идёт до момента пока
            # i(позиция символа с начала ) меньше j(позиция символа с конца) двигаясь в центр
            if line[i].lower() != line[j].lower():
                return False
            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    print(main())
    # print(is_palindrome())