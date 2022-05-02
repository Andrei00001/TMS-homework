import calc
from decimal import Decimal, InvalidOperation
from exceptions import WrongInput, UnknownOperator


def func_cl(number_one, operator, number_two) -> str | int:
    """
    The function takes 3 parameters, looks at which operator is entered, and calls the subsequent functions described
    in the calc module
    If the operator is not found, it raises an error
    :param number_one:
    :param operator: оператор операции над числами
    :param number_two:
    :return: Возвращает либо ошибку либо результат выполненной функции
    """
    if operator == "+":
        return calc_object.addition(number_one, number_two)

    elif operator == "-":
        return calc_object.subtraction(number_one, number_two)

    elif operator == "/":
        return calc_object.division(number_one, number_two)

    elif operator == "*":
        return calc_object.multiplication(number_one, number_two)

    else:
        raise UnknownOperator("Invalid operator")


def len_list(number_lis) -> int | Decimal | str:
    """
    Function to check the length of the list, display errors, reset the last value of the data buffer
    :param number_lis:
    :return:
    """
    if number_lis[0] == "c":
        calc_object.last_memory = 0
        return "cleanse"

    if len(number_lis) == 2:
        numder_1 = calc_object.last_memory
        operator = number_lis[0]
        numder_2 = Decimal(number_lis[-1])

    elif len(number_lis) == 3:
        numder_1 = Decimal(number_lis[0])
        operator = number_lis[1]
        numder_2 = Decimal(number_lis[-1])

    else:
        raise WrongInput("Input error")

    calc_object.last_memory = func_cl(numder_1, operator, numder_2)
    return calc_object.last_memory


def main():
    """
    Loop function, asks for numbers, calls subsequent functions, formats the entered data into a list, displays errors.
    :return:
    """
    while True:

        number = input("Enter the number: ")

        list_number = number.strip().split(" ")

        try:
            a = len_list(list_number)
            # print(type(a))
            print(a)

        except WrongInput as error:
            print(error)
        except UnknownOperator as error:
            print(error)
        except InvalidOperation as error:
            print(f"Data conversion error\n{error}")


if __name__ == '__main__':
    calc_object = calc.Calculator()

    main()
