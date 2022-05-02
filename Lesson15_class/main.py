class Car:
    __number_of_wheels: int = 4
    __side_mirrors: int = 2
    color: str = "white"

    def drive(self, a=0):
        return a

    def info(self):
        return f"{self.__number_of_wheels}-Колеса, {self.__side_mirrors} -Зеркала {self.color} - Цвет {self.drive()}-" \
               f"Едет со скоростью"


class BMW(Car):

    def __init__(self):
        super().__init__()

    def drive(self, a=100):
        return a


class Audi(Car):

    def __init__(self):
        super().__init__()

    def drive(self, a=140):
        print("Audi")
        return a


car = Car()
bmw = BMW()
audi = Audi()
bmw.color = "red"
print(bmw.drive(200))
print(bmw.info())


class Airplane:
    number_of_engines: int = 1
    engine_type_of_engines: str = "Propeller"
    __spid: int = 0

    @property
    def drive(self):
        return self.__spid

    @drive.setter
    def drive(self, a: int):
        self.__spid = a
        return self.__spid

    def info(self):
        return f"{self.number_of_engines}-Кол-во двигателей, {self.engine_type_of_engines} - Тип двигателя  {self.drive}-" \
               f"Летит со скоростью"


class Airplane1(Airplane):

    def __init__(self):
        super().__init__()


class Airplane2(Airplane):

    def __init__(self):
        super().__init__()


a = Airplane()
print(a.info())
a1 = Airplane1()
a1.drive = 100
print(a1.info())
