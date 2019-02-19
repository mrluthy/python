import random


def get_location(num):
    return [input("choose a location you want to ride to: ") for _ in range(num)]


def locations():
    number = int(input("How many locations would you like to input: "))
    location_list = get_location(number)

    return locations


print(locations())