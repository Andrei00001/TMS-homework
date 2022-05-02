"""

Домашка до понедельника:
 1. Доделать последнюю домашку
 2. В файл сохранять теперь данные в формате json
 3.Разобраться как сериализовать datetime в json (Гугл, а потом написать подробно в комменте почему именно так)
 4.*Написать класс валидатора, написать валидацию для пароля: минимум 4 символа, минимум один заглавный символ,
   минимум один прописной символ, минимум одна цифра, минимум один спецсимвол. Хэшировать пароль любым алгоритмом на
   выбор, обосновать в комменте выбор алгоритма (можно хоть свой сделать). Написать метод валидации почты. Вместо логина
   у вас должен быть ввод почтового адреса. """
from authenticator import Authenticator, Validator
from random import randint
from exceptions import RegistrationError, AuthorizationError

author = "Andrei Sherlat"


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


def cycle(func):
    """
    The decarator takes a main function and runs it in a loop until its value is true
    :param func:
    :return:
    """

    def wrapper():
        while True:
            if func():
                break

    return wrapper


@cycle
def main() -> bool:
    """
    The main function that in a loop asks the user to enter a username and password and then processes the data through
    classes
    :return: None
    """

    if object_authenticator.login:
        print("Authorization")
    else:
        print("Registration")

    login = input("Enter login: ")
    password = input("Enter password: ")

    if object_authenticator.login:

        try:
            object_authenticator.authorize(login, password)

        except AuthorizationError as error:
            print(error)

            return False

        cloc = object_authenticator.last_success_login_at.strftime("%d.%m.%Y %H:%M:%S")
        print(f"Hi: {object_authenticator.login[0].upper() + object_authenticator.login[1:]} "
              f"Time of successful authorization: {cloc} "
              f"You tried to login: {object_authenticator.errors_count} times")
    else:

        try:

            object_authenticator.registrate(Validator(login, password))
        except RegistrationError as error:
            print(error)
            return False

    guess_number_game()
    return True


if __name__ == '__main__':
    """
    ternary operator inside which the Authenticator object will be created and starts main
    """
    object_authenticator = Authenticator()
    main()
