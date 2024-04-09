number = int(input("Введіть число "))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# your code goes here
res = False
for i in a:
    if number == a[i]:
        res = True
if res == True:
    print("Введене число - існує")
else:
    print("Введене число - не існує")
