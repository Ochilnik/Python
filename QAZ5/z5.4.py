temp = int(input("Input temp: "))

if temp <= 0:
    print("Лід")
else:
    if temp >= 100:
        print("Пара")
    else:
        print("Вода")
