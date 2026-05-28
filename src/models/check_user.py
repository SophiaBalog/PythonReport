from .load_json import JsonService
import re
import flet as ft
import random
import datetime

class LoginUser:
    def __init__(self,username,password):
        self.username = username.strip().lower()
        self.password = password.strip().lower()
        self.users = JsonService('storage/users.json').read_json()

    def check(self, page: ft.Page):
        for user in self.users:
            if (
                    (user['email'] == self.username or user['name'] == self.username)
                    and user['password'] == self.password
            ):
                page.session.store.set("user", user)
                return True
        return False


class RegisterUser:
    def __init__(self,username,user_email,password):
        self.username = username.strip().lower()
        self.password = password.strip().lower()
        self.user_email = user_email.strip()
        self.users = JsonService('storage/users.json').read_json()
        self.avatars = JsonService('storage/avatars.json').read_json()

    def is_valid_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern,self.user_email) is not None

    def is_valid_password(self):
        return len(self.password) >= 6



    def check(self):
        if not self.is_valid_email():
            return {
                'success': False,
                'message': 'Некоректний email'
            }

        if not self.is_valid_password():
            return {
                'success': False,
                'message': 'Пароль має бути мінімум 6 символів'
            }

        for user in self.users:
            if user['email'] == self.user_email:
                return {
                    'success':False,
                    'message': 'email вже зареєстровано'
                }
            elif user['name'] == self.username:
                return {
                    'success':False,
                    'message': "ім'я користувача зайняте"
                }

        else:
            self.users.append({
                "email": self.user_email,
                "name": self.username,
                "password": self.password,
                "avatar":f"{random.choice(self.avatars)}",
                "data":f"{datetime.date.today()}"
            })
            JsonService('storage/users.json').dump_json(self.users)
            return{
                'success':True,
                'message':""
            }