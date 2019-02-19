def walk_length(walk):
    print("You need to take a 10 minute walk and return to the same place you started.\n"
          "Please enter the directions of your walk using n, e, s, w, with each direction being 1 minute of travel. ")
    expected_characters = "newsNEWS"
    inputed_characters = []
    travel = 0
    while travel < 10:
        walk = input("Enter a direction: ")
        while walk not in expected_characters:
            print("That is not an accepted input.")
            walk = input("Enter a direction: ")
        else:
            inputed_characters.append(walk)
            travel += 1
    if inputed_characters.count('n') == inputed_characters.count('s') and inputed_characters.count(
            'e') == inputed_characters.count('w') and len(inputed_characters) == 10:
        return "You came back and made your appointment!"
    elif inputed_characters.count('n') != inputed_characters.count('s') and len(
            inputed_characters) == 10 or inputed_characters.count('e') != inputed_characters.count('w') and len(
            walk) == 10:
        return "You took a ten minute walk but did not return to your appointment"
print(walk_length(""))



# while milk is None:
#     user_input = input("Please enter the amount of milk in gallons: ")
#     try:
#         milk = float(user_input)
#     except ValueError:
#         print("That is not a correct input. Please enter the amount of milk in gallons. ")