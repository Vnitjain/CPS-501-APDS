import shapes

user_name = input("Please enter your username and press enter: ")
print("Hello, " + user_name + "!. Hope you are doing well!!!")


def show_menu():
    user_input = int(
        input(
            "Select a shape to calculate area or perimeter:\n1. Circle\n2. Square\n3. Rectangle\n4. Exit\n"
        )
    )
    return user_input


def show_result(geometrical_shape, perimeter, area):
    if geometrical_shape == "circle":
        print(
            "The circumference of the "
            + str(geometrical_shape)
            + " is: "
            + str(perimeter)
        )
    else:
        print(
            "THe perimeter of the " + str(geometrical_shape) + " is: " + str(perimeter)
        )
    print("The area of the " + str(geometrical_shape) + " is: " + str(area))


def main():
    show_menu()
    user_input = -1
    while user_input != 4:
        if user_input == 1:
            print("The formula for circumference of circle is 2*pi*radius.")
            print("The formula for area of circle is pi*(radius**2).")
            radius_of_circle = float(
                input("Please enter the radius of the circle and press enter: ")
            )
            circumference_of_circle = shapes.circumference_of_circle(radius_of_circle)
            area_of_circle = shapes.area_of_circle(radius_of_circle)
            show_result("circle", circumference_of_circle, area_of_circle)
        elif user_input == 2:
            print("The formula for perimeter of square is 4*length.")
            print("The formula for area of rectangle is length**2.")
            length_of_square = float(
                input("Please enter the length of the square and press enter: ")
            )
            perimeter_of_square = shapes.perimeter_of_square(length_of_square)
            area_of_square = shapes.area_of_square(length_of_square)
            show_result("square", perimeter_of_square, area_of_square)
        elif user_input == 3:
            print("The formula for perimeter of rectangle is 2*(length+width).")
            print("The formula for area of rectangle is length*width.")
            length_of_rectangle = float(
                input("Please enter the length of the rectangle and press enter: ")
            )
            width_of_rectangle = float(
                input("Please enter the width of the rectangle and press enter: ")
            )
            perimeter_of_rectangle = shapes.perimeter_of_rectangle(
                length_of_rectangle, width_of_rectangle
            )
            area_of_rectangle = shapes.area_of_rectangle(
                length_of_rectangle, width_of_rectangle
            )
            show_result("rectangle", perimeter_of_rectangle, area_of_rectangle)
        user_input = show_menu()
    print("Thank you!!")


main()
