number = int(input("Введіть число"))

i = 0
while i <= number:
    if i % 2 == 0:
        print(i * i)
    else:
        print(i)
    i = i + 1
