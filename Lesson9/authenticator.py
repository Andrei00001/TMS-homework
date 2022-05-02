from datetime import datetime
import os.path
from exceptions import AuthorizationError, RegistrationError
import json
import hashlib
import uuid
import re


class Validator:
    """
    A class that accepts the entered login and password, as well as hashing the password.
    """
    errors_count: int = 0

    def __init__(self, login, password):
        # key variable for password hashing
        self.salt = uuid.uuid4().hex

        self.login = login
        self.password = password

        self.valid_login(self.login)
        self.valid_password(self.password)
        self.convert_password_hesh()

    @classmethod
    def valid_login(cls, login) -> None:
        """
        The function that accepts the entered login checks it against the pattern, otherwise an error occurs.
        :param login:
        :return:
        """
        if len(re.findall(r".+@.+\..+", login)) != 1:
            cls.errors_count += 1
            raise RegistrationError("Login like @._")

    @classmethod
    def valid_password(cls, password) -> None:
        """
        The function that accepts the entered password checks it for pattern matching, otherwise an error occurs.
        :param password:
        :return:
        """
        if len(set(re.findall(r"[^A-z0-9А-яЁё ]", password))) == 0 or \
                len(set(re.findall(r"[a-zа-яё]", password))) == 0 or \
                len(set(re.findall(r"[A-ZА-ЯЁ]", password))) == 0 or \
                len(set(re.findall(r"[0-9]", password))) == 0 or \
                len(password) < 4:
            cls.errors_count += 1
            raise RegistrationError("Password must be at least 4 characters, at least one uppercase character, at least"
                                    " one uppercase character, at least one number, at least one special character")

    def convert_password_hesh(self) -> None:
        """
        Password hashing function. Writes to a dictionary variable the hash of the password and the key by which it
        hashed.
        :return:
        """
        self.password = {"key": self.salt,
                         "hesh": hashlib.sha512(self.salt.encode() + self.password.encode()).hexdigest()}


class Authenticator:
    """
    Class Authenticator does all the basic work
    """

    def __init__(self):
        """
        The class constructor, in which the class attributes are initialized, checks for the existence of a file; if
        the file exists, it calls the read function.
        """

        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0

        if self._is_auth_file_exist():
            self._read_auth_file()

    @staticmethod
    def _is_auth_file_exist() -> bool:
        """
        The function checks if the file is created or not
        :return: true/false
        """
        return os.path.isfile("auth.json")

    def _read_auth_file(self) -> None:
        """
        This function reads information from a file auth.json
        :return: None
        """
        with open("auth.json", "r") as file:
            data = json.load(file)
            self.login = data["login"]
            self._password = data["password"]
            self.last_success_login_at = datetime.fromisoformat(data["time"])
            self.errors_count = int(data["errors_count"])

    def authorize(self, login, password) -> None:
        """
        This function takes strings if the file exists, checks them against the value in the written file. The password
        match is checked by hashing the input and the value from the file. If the entered information and the
        information from the file do not match, the number of errors increases and the file is overwritten.
        :param login:  takes a string
        :param password: takes a string
        :return: None
        """
        if login and password:
            key = dict(self._password)["key"]
            password = hashlib.sha512(key.encode() + password.encode()).hexdigest()
        if login != self.login or password != dict(self._password)["hesh"]:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError("You will not pass\n")

        else:
            self.errors_count += 1
            self._update_auth_file()
            raise AuthorizationError("Enter login or password\n")

    def registrate(self, data: Validator) -> None:
        """
        This function takes an object of the Validator class. Writes valid data to the value of the login password and
        errors. Calls the _update_auth_file function
        :param data:
        :return: None
        """
        if self.login:
            self.errors_count += 1
            self._update_auth_file()
            raise RegistrationError("Can't re-register")

        self.login = data.login
        self._password = data.password
        self.errors_count += data.errors_count
        self._update_auth_file()

    def _update_auth_file(self) -> None:
        """
        This function creates and overwrites the error password login and time values in a file.
        :return: None
        """
        with open("auth.json", "w") as file:
            self.last_success_login_at = datetime.utcnow()
            data = {"login": self.login,
                    "password": self._password,
                    # сереализовать в .json можно только стандартные типы данных, а именно:
                    # dict
                    # list, tuple
                    # str
                    # int, float
                    # True
                    # False
                    # None
                    "time": datetime.utcnow().isoformat(" "),
                    "errors_count": self.errors_count
                    }

            json.dump(data, file)
