miles = float(input("Введіть кількість миль"))


# your code goes here
def convert_miles_to_km(mil):
    km = round(mil * 1.6, 2)
    return km
print(convert_miles_to_km(miles))
