windows_count = int(input("Введіть кількість вікон "))
flors_count = int(input("Введіть кількість поверхів "))


class Building:
    # your code goes here
    windows_count = windows_count
    flors_count = flors_count


w = Building.windows_count * Building.flors_count
print("Загальна кількість вікон {}".format(w))
