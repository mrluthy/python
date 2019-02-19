# def walk_length(walk):
#     print("You need to take a 10 minute walk and return to the same place you started.\n"
#     "Please enter in all the directions of your walk using n, e, s, w, with each direction being 1 minute of travel. ")
#     excluded_characters = set("1234567890qazxcdrfvgtbmhjkloppiuy;',./!@#$%^&*()_+=-<>?:")
#     inputted_characters = []
#     travel = 0
#     for travel_iteration in iter(walk, ''):
#         travel.append(str(travel_iteration))
#         walk = input("Enter a direction: ")
#         while set(walk).issubset(excluded_characters) or len(walk) > 1:
#             print("That is not an accepted input.")
#             walk = input("Enter a direction: ")
#
#         else:
#             inputted_characters.append(walk)
#             travel += 1
#     if inputted_characters.count('n') == inputted_characters.count('s') and inputted_characters.count(
#             'e') == inputted_characters.count('w') and len(inputted_characters) == 10:
#         return "You came back and made your appointment!"
#     elif inputted_characters.count('n') != inputted_characters.count('s') and len(
#             inputted_characters) == 10 or inputted_characters.count('e') != inputted_characters.count('w') and len(
#             walk) == 10:
#         return "You took a ten minute walk but did not return to your appointment"
#
#
# print(walk_length(""))


def walk_length():
    walk = input("You need to take a 10 minute walk and return to the same place you started.\n"
                 "Please enter the directions of your walk using n, e, s, w,  \n"
                 "with each direction being 1 minute of travel: ")
    conditionals(walk)


def conditionals(walk):
    while walk in ("n", "e", "w", "s") and len(walk) == 10:
        # print(input("That is not a valid input, please try again: "))
        print("you completed your 10 minute walk and returned to your appointment!")
    # if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10:
    #     print("you completed your 10 minute walk and returned to your appointment!")


walk_length()
