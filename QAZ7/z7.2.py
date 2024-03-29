number = int(input("Введіть число"))


# your code goes here
def is_even_or_odd(n):
    if n % 2 == 0:
        res = "число " + str(n) + " парне"
    else:
        res = "число " + str(n) + " непарне"
    return res


print(is_even_or_odd(number))
