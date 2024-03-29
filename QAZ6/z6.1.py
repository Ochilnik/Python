number = int(input("Введіть шуканий член арифметичної прогресії "))

first = 5
dif = 3
sum = first

for i in range(1, number):
    sum = sum + dif
print(sum)
