import random

user_name = input("Please enter your username and press enter : ")

print("Hello " + user_name + "!!")

user_input = 0


def generate_two_random_number():
    first_number = int(random.random() * 100)
    second_number = int(random.random() * 100)
    return (first_number, second_number)


while user_input != 3:
    user_input = int(
        input(
            "Please select an option and press enter :\n1 => Addition\n2 => Subtraction\n3 => Exit"
        )
    )
    if user_input == 1:
        random_number_tuple = generate_two_random_number()
        print(random_number_tuple)
    elif user_input == 2:
        random_number_tuple = generate_two_random_number()
        print(random_number_tuple)
