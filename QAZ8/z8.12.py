line = input("Введіть рядок ")
rulet = ("ы", "ъ", "ё", "э")
n = len(line)
flag = False


for i in range(n):
    if line[i] in rulet:
        flag = True
if flag == False:
    print("Дякуємо за замовлення!")
else:
    print("Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!")
