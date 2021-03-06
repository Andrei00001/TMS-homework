from flask import url_for
from flask_login import UserMixin


class UserLogin(UserMixin):
    def fromdb(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user['id'])

    def getName(self):
        return self.__user['name'] if self.__user else "Без имени"

    def getEmail(self):
        return self.__user['email'] if self.__user else "Без email"

    def getAvatar(self, app):
        img = None
        if not self.__user['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), "rb") as file:
                    img = file.read()
            except FileNotFoundError as error:
                print("Нет фото:" + str(error))
        else:
            img = self.__user['avatar']

        return img

    def verifyExt(self, filename):
        ext = filename.rsplit('.',1)[1]
        if ext =="png" or ext == "PNG":
            return True
        return False