from datetime import datetime
from exceptions import ValidationError


class Data:
    """
    Object initialization class
    """

    def __init__(self, name: str, age: str):
        """
        :param name: Accepts a string
        :param age: Accepts a string
        The class constructor in which variables are initialized and processed using a function _clear_whitespaces
        """
        self.name = name
        self.age = age
        self._clear_whitespaces()
        self.age = int(self.age)

    def _clear_whitespaces(self):
        """
        Overwrites a string with leading and trailing spaces removed if any
        """
        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    """
    Child class Data
    """

    def __init__(self, name, age):
        """
        :param name: Accepts a string from Data with super().__init__(name, age)
        :param age: Accepts a integer from Data with super().__init__(name, age)
        This is a class constructor that initializes variables from the Date class and writes down the object's
        initialization time
        """

        super().__init__(name, age)
        self.cloc = datetime.utcnow()


class Validator:
    """
    Class validator data that initializes
    """

    def __init__(self):
        """
        This is a class constructor the initializes the list to store object DataWithDate
        """
        self.data_history: list[Data] = []

    def _validate_name(self):
        """
        function validate name checks the name for correct input
        :return valid name
        """

        if not self.data_history:
            raise ValueError("No object passed, don't touch local functions")

        name = self.data_history[-1].name
        if not name:
            raise ValidationError("Empty string")

        elif name.count(" ") > 1:
            raise ValidationError("Check if the name you entered is correct Many spaces are possible,only 1 is allowed")

        elif len(name) < 3:
            raise ValidationError(f"Minimum 3 characters")

    def _validate_age(self):
        """
        function validate age checks the age for correct input
        :return valid age
        """

        if not self.data_history:
            raise ValueError(f"No object passed, don't touch local functions")

        age = self.data_history[-1].age
        if age <= 0:
            raise ValidationError("Something wrong with age 0 years or less")

        elif age < 14:
            raise ValidationError("Minimum age 14 years")

    def validate(self, data: Data):
        """
        function validate accepts an object class DataWithDate and writes it to list data_history then launches function
        _validate_name and _validate_age, which take the last element of the list and process it
        :return: tuple of valid name and age
        """

        self.data_history.append(data)
        self._validate_name()
        self._validate_age()
