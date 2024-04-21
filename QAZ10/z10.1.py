input_database_name = input("Введіть ім'я бази даних ")
new_database_name = input("Введіть нове ім'я бази даних ")


class Database:
    # your code goes here
    def __init__(self, database_name):
        self._connected_to_database = False
        self.__database_name = database_name
        return

    def get_connected_to_database(self):
        return self._connected_to_database

    def set_connected_to_database(self, connection_state):
        print(
            "Неможливо змінити значення connected_to_database за допомогою присвоєння. Використайте метод connect_to_database"
        )
        return

    def get_database_name(self):
        return self.__database_name

    def set_database_name(self, value):
        self.__database_name = value.upper()
        return

    def connect_to_database(self):
        self._connected_to_database = True
        print("Під'єднано до бази даних")


db = Database(input_database_name)
print(db._connected_to_database)
print(db.get_connected_to_database())
db.set_connected_to_database(True)

db.connect_to_database()
print(db._connected_to_database)
print(db.get_connected_to_database())

print(db.get_database_name())
db.set_database_name(new_database_name)
print(db.get_database_name())
