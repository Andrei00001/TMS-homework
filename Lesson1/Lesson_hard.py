from random import randint

a = randint(1, 10)

print(a)
# dhaklshdg

def ZD(i):
    while True:
        if int(input("Введите число:")) == i:
            print("Угадал")
            break
        else:
            print("Не угадал")


ZD(a)
