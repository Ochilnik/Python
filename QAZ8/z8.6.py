str_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

# your code goes here
value = input("Введіть елемент ")
if value in str_set:
    str_set.remove(value)
print(str_set)
