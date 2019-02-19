def walk_length(walk):
    if walk == '':
        walk = input("You need to take a 10 minute walk and return to the same place you started.\n"
                     "Please enter the directions of your walk using n, e, s, w, with each direction being 1 minute of travel: ")
    expected_characters = "newsNEWS"
    expected_characters.split()
    while walk not in expected_characters:
        expected_characters = print("That is not a correct input!")
        walk = input("You need to take a 10 minute walk and return to the same place you started.\n"
                     "Please enter the directions of your walk using n, e, s, w, with each direction being 1 minute of travel: ")

    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10:
        return "You came back and made your appointment!"
    elif walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) > 10:
        return "You came back but were gone too long and missed your appointment!"
    elif walk.count('n') != walk.count('s') and len(walk) < 10 or walk.count('e') != walk.count('w') and len(walk) < 10:
        return "You did not travel long enough and didn't return to the appointment"
    elif walk.count('n') != walk.count('s') and len(walk) > 10 or walk.count('e') != walk.count('w') and len(walk) > 10:
        return "You were gone too long and did not return to your appointment"
    elif walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) < 10:
        return "You arrived too early!"


print(walk_length(""))
