number = int(input("Введіть число "))
digits = dict()

for i in range(0, number + 1):
    digits[i] = i * i
print(digits)
