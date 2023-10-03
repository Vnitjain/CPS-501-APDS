# Name : Vinit Kirit Jain
# Creation Date : 2023-09-17
""" Brief Description :
    Writing a program to display a menu to the user and asking them to enter a guess based on the two random numbers shown. 
    Showing a positive message if the answer is correct and a negative message other wise.
"""


# importing the random library to generate random numbers
import random

# asking the user their name
user_name = input("Please enter your username and press enter : ")

# greeting the user by using their username
print("Hello " + user_name + "!!")


# declaring a function to generate random numbers
def generate_two_random_number():
    # generating the first number
    first_number = int(random.random() * 100)
    # generating the second number
    second_number = int(random.random() * 100)
    # swapping the numbers to make sure there are no negative numbers during subtraction
    if second_number > first_number:
        # swapping two variables
        first_number, second_number = second_number, first_number
    # returning the numbers as a tuple
    return (first_number, second_number)


# declaring a function to check if the input is equal to the expected result
def check_if_input_is_equal(expected_result, actual_result):
    # comparing the two results
    if expected_result == actual_result:
        # printing a positive message for correct answer
        print("Your answer is correct! Well done.")
    else:
        # printing a negative message for incorrect answer with correct solution
        print("Sorry, the correct answer is: " + str(expected_result) + ".")
    # pausing and waiting for the user to press enter
    input("Press enter to continue.\n")


# initializing the user input to zero
user_input = 0

# using while to end the loop if the user enters 3 and continue if 1 or 2 is entered
while user_input != 3:
    # if user input is 1 showing the random numbers and asking for input
    if user_input == 1:
        # generate two random number by calling the generate function and getting the tuple
        random_number_tuple = generate_two_random_number()
        # printing the two numbers from the tuple
        print(
            "The two numbers are : "
            + str(random_number_tuple[0])
            + ", "
            + str(random_number_tuple[1])
        )
        # asking the user to guess the sum
        sum_input = int(input("Please enter the sum and press enter: "))
        # calculating the expected sum
        expected_sum = random_number_tuple[0] + random_number_tuple[1]
        # calling the check method to compare the two numbers and give the output accordingly
        check_if_input_is_equal(expected_sum, sum_input)
    elif user_input == 2:
        # generate two random number by calling the generate function and getting the tuple
        random_number_tuple = generate_two_random_number()
        # printing the two numbers from the tuple
        print(
            "The two numbers are : "
            + str(random_number_tuple[0])
            + ", "
            + str(random_number_tuple[1])
        )
        # if the random numbers are equal, printing the message and continuing
        if random_number_tuple[0] == random_number_tuple[1]:
            print("Both numbers are the same and the difference is 0")
        else:
            # asking the user to guess the difference
            difference_input = int(
                input("Please enter the difference and press enter: ")
            )
            # calculating the expected difference
            expected_difference = random_number_tuple[0] - random_number_tuple[1]
            # calling the check method to compare the two numbers and give the output accordingly
            check_if_input_is_equal(expected_difference, difference_input)
    # displaying the menu and taking the input from the user
    user_input = int(
        input(
            "Please select an option and press enter :\n1 => Addition\n2 => Subtraction\n3 => Exit\n"
        )
    )
# thanking the user indicating the end of code
print("Thank you for playing!!!")
