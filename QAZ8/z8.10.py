last_name = input("Введіть прізвище ")
name = input("Введіть ім'я ")
second_name = input("Введіть по батькові ")

# your code goes here
if len(last_name) == 0 or len(name) == 0 or len(second_name) == 0:
    print("Не введений ключовий параметр")
else:
    print(f"{last_name.title()} {name[0].upper()}.{second_name[0].upper()}.")
