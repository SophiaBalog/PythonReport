import os
import random

from .load_json import JsonService



class UsersService:
    def __init__(self, current_user):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.normpath(os.path.join(current_dir, '..', 'storage', 'users.json'))
        self.avatars = JsonService('storage/avatars.json').read_json()
        self.users = JsonService(file_path).read_json()
        self.file_path = file_path

        if isinstance(current_user, dict):
            self.current_user_name = current_user.get('name')
        else:
            self.current_user_name = current_user

    def get_user(self):
        if not self.users:
            return None

        for user in self.users:
            if str(user.get('name')).strip() == str(self.current_user_name).strip():
                return user
        return None

    def get_all_users(self):
        """Повертає весь масив словників"""
        return self.users

    def update_avatar(self):
        for user in self.users:
            if str(user.get('name')).strip() == str(self.current_user_name).strip():
                user['avatar'] = random.choice(self.avatars)

                JsonService(self.file_path).dump_json(self.users)
                return user

        return None
