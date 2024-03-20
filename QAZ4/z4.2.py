costOne=6500
kurs = float(input("Input kurs: "))
sum = int(input("Input sum: "))

k = sum//(costOne*kurs)
#k = floor(k)
print('Для набору вхідних даних (курс = ',kurs,', сума = ',sum,') - кількость - ',k)
