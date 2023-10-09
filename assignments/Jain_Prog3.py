# Name : Vinit Kirit Jain
# Creation Date : 2023-10-08
""" Brief Description :
    Writing a program to display a menu containing three geometrical shapes and waiting for the user to enter their dimensions to then display the 
    perimeter/circumference and the area of the shape.
"""

# importing the shapes.py file to use their functions
import shapes

# asking the user for their name
user_name = input("Please enter your username and press enter: ")
# greeting the user by using their name
print("Hello, " + user_name + "!. Hope you are doing well!!!")


# function for showing the menu
def show_menu():
    # asking the user to select a shape and press enter and converting it to integer
    user_input = int(
        input(
            "Select a shape to calculate area or perimeter and then press enter:\n1. Circle\n2. Square\n3. Rectangle\n4. Exit\n"
        )
    )
    # returning the users input in integer
    return user_input


# function to show the result
def show_result(geometrical_shape, perimeter, area):
    # if the shape is circle using a different string
    if geometrical_shape == "circle":
        print(
            "The circumference of the "
            + str(geometrical_shape)
            + " is: "
            + str(perimeter)
        )
    else:
        # using different string for the other shapes
        print(
            "THe perimeter of the " + str(geometrical_shape) + " is: " + str(perimeter)
        )
    # showing the area of the shape
    print("The area of the " + str(geometrical_shape) + " is: " + str(area) + "\n")


# defining a function to process the choice of the user
def process_choice(choice):
    # running a while loop until exit choice is received
    while choice != 4:
        # if the choice is circle
        if choice == 1:
            # printing the formulae for circumference and area of circle
            print("The formula for circumference of circle is 2*pi*radius.")
            print("The formula for area of circle is pi*(radius**2).")
            # asking the user for the radius of the circle and converting it to float
            radius_of_circle = float(
                input("Please enter the radius of the circle and press enter: ")
            )
            # using the shapes file to get the circumference of circle
            circumference_of_circle = shapes.circumference_of_circle(radius_of_circle)
            # using the shapes file to get the area of the cirlce
            area_of_circle = shapes.area_of_circle(radius_of_circle)
            # showing the final result
            show_result("circle", circumference_of_circle, area_of_circle)
        # if the choice is square
        elif choice == 2:
            # printing the formulae for perimeter and area of square
            print("The formula for perimeter of square is 4*length.")
            print("The formula for area of square is length**2.")
            # asking the user for length of square end convert it to float
            length_of_square = float(
                input("Please enter the length of the square and press enter: ")
            )
            # calculating the perimeter and area by calling the functions from the shape.py file
            perimeter_of_square = shapes.perimeter_of_square(length_of_square)
            area_of_square = shapes.area_of_square(length_of_square)
            # printing the final result
            show_result("square", perimeter_of_square, area_of_square)
        # if the choice is rectangle
        elif choice == 3:
            # printing the formulae for the perimeter and area of rectangle
            print("The formula for perimeter of rectangle is 2*(length+width).")
            print("The formula for area of rectangle is length*width.")
            # asking the user for length and width of the rectangle
            length_of_rectangle = float(
                input("Please enter the length of the rectangle and press enter: ")
            )
            width_of_rectangle = float(
                input("Please enter the width of the rectangle and press enter: ")
            )
            # calculating the perimeter and area by calling the functions from the shape.py file
            perimeter_of_rectangle = shapes.perimeter_of_rectangle(
                length_of_rectangle, width_of_rectangle
            )
            area_of_rectangle = shapes.area_of_rectangle(
                length_of_rectangle, width_of_rectangle
            )
            # printing the final result
            show_result("rectangle", perimeter_of_rectangle, area_of_rectangle)
        # showing the menu
        choice = show_menu()
    # printing thank you at the end of the code
    print("Thank you!!")


# defining a main function
def main():
    # taking the user input with show menu method
    user_input = show_menu()
    # process the user entered option
    process_choice(user_input)


# calling the main function
main()
