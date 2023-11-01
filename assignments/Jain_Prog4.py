# Name : Vinit Kirit Jain
# Creation Date : 2023-10-22
""" Brief Description :
    This program is a math practice tool that allows users to practice four math operations: addition, subtraction, multiplication, and division. It prompts the user to choose an operation, the number of digits for the numbers involved, and the number of practice attempts. The program generates random numbers for the chosen operation, asks the user for their answer, provides feedback, and tracks the user's performance. The results are stored in a report that can be displayed upon the user's request. The program continues to operate until the user chooses to exit.
"""
# declaring an empty list to store the report of each operation
report = []

# importing the random library to generate random numbers
import random

# asking the user their name
user_name = input("Please enter your username and press enter : ")

# greeting the user by using their username
print("Hello " + user_name + "!!")


# declaring a function to generate random numbers
def generate_random_numbers(number_of_digits):
    random_numbers_tuple = (
        int(random.random() * (10 * number_of_digits)),
        int(random.random() * (10 * number_of_digits)),
    )
    print("The random numbers are: ", end="")
    print(random_numbers_tuple, sep=" ")
    return random_numbers_tuple


# defining a function to show the menu and take the input and return the user input
def show_menu():
    menu_items = [
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Division",
        "5. Present & Report",
        "6. Exit",
    ]
    for i in menu_items:
        print(i)
    user_input = int(input("Please select an option and press enter: "))
    return user_input


# defining a function to ask user about the number of digits for each operaion
def show_digit_selection_menu():
    digit_selection = ["1. 1 Digit", "2. 2 Digits", "3. 3 Digits"]
    for i in digit_selection:
        print(i)
    user_input = int(input("Please select the number of digits and press enter: "))
    return user_input


# defining a function to ask user about the number of attempts for each operaion
def operation_repeat_count():
    operations = int(
        input("Please enter the number of times to perform this operation: ")
    )
    return operations


# declaring a function to check if the input is equal to the expected result
def check_if_input_is_equal(expected_result, actual_result):
    positive_reinforcers = [
        "Excellent",
        "Very Good",
        "Well Done",
        "Awesome",
        "Good Job",
        "Correct",
    ]
    negative_reinforcers = [
        "Try Again. ",
        "OOPS. ",
        "Not Quite. ",
        "Look at it Again. ",
        "Sorry. ",
    ]
    # comparing the two results
    if expected_result == actual_result:
        # printing a positive message for correct answer
        print(random.choice(positive_reinforcers) + "\nPress enter to continue.\n")
        return True
    else:
        # printing a negative message for incorrect answer with correct solution
        print(
            random.choice(negative_reinforcers)
            + "The correct answer is: "
            + str(expected_result)
            + "\nPress enter to continue.\n"
        )
        return False


# initializing the user input to zero
user_input = -1
digit_selection = -1

# using while to end the loop if the user enters 3 and continue if 1 or 2 is entered
while user_input != 6:
    # if user input is 1 showing the random numbers and asking for input
    if user_input == 1:
        digit_selection = show_digit_selection_menu()
        operation_count = operation_repeat_count()
        # adding operation to the list to initilize the temporary list
        report_list = ["Addition", 0, 0]
        for i in range(operation_count):
            print("\nAttempt No. " + str(i + 1))
            random_number_tuple = generate_random_numbers(digit_selection)
            sum_input = int(input("Please enter the sum and press enter: "))
            expected_sum = random_number_tuple[0] + random_number_tuple[1]
            is_equal = check_if_input_is_equal(expected_sum, sum_input)
            report_list[2] = report_list[2] + 1
            # if the answer entered is correct show them a positive response if not then let them attempt again and show a negative message
            if is_equal:
                report_list[1] = report_list[1] + 1
            else:
                print(
                    "The random numbers are: "
                    + str(random_number_tuple[0])
                    + " "
                    + str(random_number_tuple[1]),
                )
                new_input = int(input("\nPlease enter your solution again: "))
                report_list[2] = report_list[2] + 1
                if check_if_input_is_equal(expected_sum, new_input):
                    report_list[1] = report_list[1] + 1
        # adding the temporary list to the main report to keep track of all the operations
        report.append(report_list)
    elif user_input == 2:
        digit_selection = show_digit_selection_menu()
        operation_count = operation_repeat_count()
        # adding operation to the list to initilize the temporary list
        report_list = ["Subtraction", 0, 0]
        for i in range(operation_count):
            print("Attempt No. " + str(i + 1))
            random_number_tuple = generate_random_numbers(digit_selection)
            # if the answer entered is correct show them a positive response if not then let them attempt again and show a negative message
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
                is_equal = check_if_input_is_equal(
                    expected_difference, difference_input
                )
                report_list[2] = report_list[2] + 1
                if is_equal:
                    report_list[1] = report_list[1] + 1
                else:
                    print(
                        "The random numbers are: "
                        + str(random_number_tuple[0])
                        + " "
                        + str(random_number_tuple[1]),
                        end="",
                    )
                    new_input = int(input("\nPlease enter your solution again: "))
                    report_list[2] = report_list[2] + 1
                    if check_if_input_is_equal(expected_difference, new_input):
                        report_list[1] = report_list[1] + 1
                # adding the temporary list to the main report to keep track of all the operations
                report.append(report_list)
    elif user_input == 3:
        digit_selection = show_digit_selection_menu()
        operation_count = operation_repeat_count()
        # adding operation to the list to initilize the temporary list
        report_list = ["Multiplication", 0, 0]
        for i in range(operation_count):
            print("\nAttempt No. " + str(i + 1))
            random_number_tuple = generate_random_numbers(digit_selection)
            sum_input = int(input("Please enter the product and press enter: "))
            expected_sum = random_number_tuple[0] * random_number_tuple[1]
            is_equal = check_if_input_is_equal(expected_sum, sum_input)
            report_list[2] = report_list[2] + 1
            # if the answer entered is correct show them a positive response if not then let them attempt again and show a negative message
            if is_equal:
                report_list[1] = report_list[1] + 1
            else:
                print(
                    "The random numbers are: "
                    + str(random_number_tuple[0])
                    + " "
                    + str(random_number_tuple[1]),
                )
                new_input = int(input("\nPlease enter your solution again: "))
                report_list[2] = report_list[2] + 1
                if check_if_input_is_equal(expected_sum, new_input):
                    report_list[1] = report_list[1] + 1
        # adding the temporary list to the main report to keep track of all the operations
        report.append(report_list)
    elif user_input == 4:
        digit_selection = show_digit_selection_menu()
        operation_count = operation_repeat_count()
        report_list = ["Division", 0, 0]
        for i in range(operation_count):
            print("\nAttempt No. " + str(i + 1))
            random_number_tuple = generate_random_numbers(digit_selection)
            sum_input = float(input("Please enter the division and press enter: "))
            expected_sum = random_number_tuple[0] / random_number_tuple[1]
            is_equal = check_if_input_is_equal(expected_sum, sum_input)
            report_list[2] = report_list[2] + 1
            # if the answer entered is correct show them a positive response if not then let them attempt again and show a negative message
            if is_equal:
                report_list[1] = report_list[1] + 1
            else:
                print(
                    "The random numbers are: "
                    + str(random_number_tuple[0])
                    + " "
                    + str(random_number_tuple[1]),
                )
                new_input = float(input("\nPlease enter your solution again: "))
                report_list[2] = report_list[2] + 1
                if check_if_input_is_equal(expected_sum, new_input):
                    report_list[1] = report_list[1] + 1
        report.append(report_list)
    elif user_input == 5:
        if report.count == 0:
            print("Empty List")
        else:
            print("\nReport\n")
            for i in report:
                print("Operation: " + str(i[0]))
                print("Numer of correct entries: " + str(i[1]))
                print("Number of tries: " + str(i[2]), end="\n\n")
    # displaying the menu and taking the input from the user
    user_input = show_menu()
# thanking the user indicating the end of code
print("Thank you for playing!!!")
