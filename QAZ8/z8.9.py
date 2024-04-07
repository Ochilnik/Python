user = {
'name': 'sergii',
'age': 100500,
'country': 'Ukraine'
}

key = input("Введіть ім'я ключа ")
new_key = input("Введіть нове ім'я ключа ")

# your code goes here       
if key in user:
    user[new_key]=user[key]
    del user[key]
    print(user)
else:
    print("Шуканого ключа немає")
