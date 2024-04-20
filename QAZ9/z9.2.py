car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")


class Cars:
    # your code goes here
    list_of_cars = []


Cars.list_of_cars.append(car_1)
Cars.list_of_cars.append(car_2)
Cars.list_of_cars.append(car_3)

string = " та ".join(Cars.list_of_cars)
print("Список авто: {}".format(string))
