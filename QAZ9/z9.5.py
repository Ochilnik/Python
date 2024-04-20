name = input("Введіть ім'я користувача  ")
new_name = input("Введіть нове ім'я користувача ")
new_last_name = input("Введіть нове прізвище користувача ")
new_second_name = input("Введіть нове по батькові користувача ")


class User:
    # your code goes here
    count_users = 0

    def __init__(self, n) -> None:
        self.name = n
        User.count_users += 1
        return

    def change_username(self, username):
        self.name = username
        return

    @classmethod
    def get_count(cls):
        print(cls.count_users)
        return

    @staticmethod
    def prepare_name(name, last_name, second_name):
        string = format(last_name + " " + name[0].upper() + "." + second_name[0].upper() + ".")
        return string


new_username = User.prepare_name(new_name, new_last_name, new_second_name)

user1 = User(name)
print(user1.name)
print(User.count_users)
print(user1.count_users)
user1.change_username(new_username)
print(user1.name)


user2 = User(name)
print(User.count_users)
print(user2.count_users)
