# Calling Functions Example
# def my_method():
#     user_input = input("please enter yes")
#     if user_input == "yes":
#         second_method(user_input)
#     print(input("please try again"))
#
#
# def second_method(user_input):
#     print(user_input)
#
#
# my_method()

def prompt_function():
    list_of_responses = []

    while True:
        try:
            another_response = input("Please enter a direction using n,s,e,w : ")
            if len(another_response) != 1 or another_response.lower() not in ("n", "s", "e", "w"):
                raise ValueError
        except ValueError:
            print(f"That is not a correct input, {another_response} is not a correct input. \n"
                  f"Please only use n, e, s, or w : ")
        else:
            list_of_responses.append(another_response.lower())

            if len(list_of_responses) == 10:
                break

    return list_of_responses


def did_I_return_home(list_of_directions):
    return list_of_directions.count('n') == list_of_directions.count('s') and list_of_directions.count(
        'e') == list_of_directions.count('w')


print(did_I_return_home(prompt_function()))


# x = 0
# while x < 10:
#     x += 1
#     print(x)

# def my_function(loop_limit):
#     x = 0
#     response = []
#     while x < loop_limit:
#         x += 1
#         response.append(input("please input a direction "))
#     print(response)
#
#
# my_function(3)


# my_list = [1, 2, 3, 4, 5, 6]
# def new_function(loop_limit):
#     response = []
#     for x in range(0, loop_limit):
#         response.append(input("asdfasfsafsf"))
#         while True:
#             if len(response[0]) != 1:
#                 input("try again")
#     print(response)
#
# new_function(3)

# grocery_list = ["milk", "donuts", "cereal]"]
#
# for grocery in grocery_list:
#     if grocery == "donuts":
#         continue
#     print(grocery)

