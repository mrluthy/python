import math

class Bottles:
    def unit_conversion():
        user_measurement_choice = None
        while user_measurement_choice is None:
            user_input = input("Enter 1 to change from Gallons to Liters OR Enter 2 to change from Liters to Gallons: ")
            try:
                user_measurement_choice= int(user_input)
            except ValueError:
                print("That is not a correct input. \n ")

        while user_measurement_choice > 2:
            try:
                print("That is not a correct input.")
                user_measurement_choice = int(input(
                    "Please Enter 1 to change from Gallons to Liters OR Enter 2 to change from Liters to Gallons:"))
            except ValueError:
                print()
        if user_measurement_choice == 1:
            milk = None
            while milk is None:
                user_input = input("Please enter the amount of milk in gallons: ")
                try:
                    milk = float(user_input)
                except ValueError:
                    print("That is not a correct input. Please enter the amount of milk in gallons. ")
            percent = None
            while percent is None:
                user_input = input("Please enter the minimum percent to be filled within the range of .01 to 1: ")
                try:
                    percent = float(user_input)
                except ValueError:
                    print(
                        "That is not a correct input. Please enter the minimum percent to be filled as an integer.\n ")
            while percent > 1:
                try:
                    print("Error::")
                    percent = float(input("Please enter a number in the range of .01 to 1: "))
                except ValueError:
                    print()
            liters = milk * 3.78541
            total_bottles = liters / percent
            remainder, bottles = math.modf(total_bottles)
            add_to_each_bottle = remainder / bottles
            new_percent = percent + add_to_each_bottle
            return bottles, new_percent
        elif user_measurement_choice == 2:
            milk = None
            while milk is None:
                user_input = input("Please enter the amount of milk in liters: ")
                try:
                    milk = float(user_input)
                except ValueError:
                    print("That is not a correct input. Please enter the amount of milk in liters. ")
            percent = None
            while percent is None:
                user_input = input("Please enter the minimum percent to be filled within the range of .01 to 1: ")
                try:
                    percent = float(user_input)
                except ValueError:
                    print(
                        "That is not a correct input. Please enter the minimum percent to be filled as an integer.\n ")
            while percent > 1:
                try:
                    print("Error::")
                    percent = float(input("Please enter a number in the range of .01 to 1: "))
                except ValueError:
                    print()
            liters = milk * 0.264172
            total_bottles = liters / percent
            remainder, bottles = math.modf(total_bottles)
            add_to_each_bottle = remainder / bottles
            new_percent = percent + add_to_each_bottle
            return bottles, new_percent
        else:
            print("you suck, try again")
    print(unit_conversion())