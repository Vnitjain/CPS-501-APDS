# function to calculate the area of circle
def area_of_circle(radius):
    area = 3.14 * radius**2
    return area


# function to calculate the circumference of circle
def circumference_of_circle(radius):
    circumference = 3.14 * (radius * 2)
    return circumference


# function to calculate the area of square
def area_of_square(length_of_side):
    area = length_of_side**2
    return area


# function to calculate the perimeter of square
def perimeter_of_square(length_of_side):
    perimeter = 4 * length_of_side
    return perimeter


# function to calculate the area of rectangle
def area_of_rectangle(length_of_side, width_of_side):
    area = length_of_side * width_of_side
    return area


# function to calculate the perimeter of rectangle
def perimeter_of_rectangle(length_of_side, width_of_side):
    perimeter = (2 * length_of_side) + (2 * width_of_side)
    return perimeter
