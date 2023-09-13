# Author Name : Vinit Kirit Jain
# Creation Date : 2023-08-30

# Question 1 : Area of circle function


# defining the area_of_circle function with radius default value as zero
def area_of_circle(radius=0):
    # checking if the radius is less than or equal to zero
    if radius <= 0:
        # return zero for 0 or negative radius
        return 0
    else:
        # defining constant pi
        PI = 3.14
        # calculating the area for a positive radius
        area = PI * (radius**2)
        # returning the calculated area
        return area


# trying some values for testing
print("area of circle")
print(area_of_circle())
print(area_of_circle(-30))
print(area_of_circle(20))


# Question 2 : Sum for loop function


# defining calculate_sum_forloop function
def calculate_sum_forloop(numbers):
    # initializing the sum as 0
    sum = 0
    # iterating through each value in the list by index
    for i in range(len(numbers)):
        # adding each number to the sum
        sum += numbers[i]
    # returning the sum
    return sum


# trying some random lists for testing
print("calculate_sum_forloop")
print(calculate_sum_forloop([1, 2, 3, 4, 5]))
print(calculate_sum_forloop([0, 0, 0]))
print(calculate_sum_forloop([-5, 3, 5]))
print(calculate_sum_forloop([]))


# Question 3 : Sum while loop function


# defining the calculate_sum_whileloop function
def calculate_sum_whileloop(numbers):
    # initializing the sum as 0
    sum = 0
    # initializing the index at 0
    i = 0
    # iterating till the length of the numbers by index
    while i < len(numbers):
        # adding to the sum each list value
        sum += numbers[i]
        # iterating the index i by 1
        i += 1
    # returning the sum
    return sum


# trying some random lists for testing
print("calculate_sum_whileloop")
print(calculate_sum_whileloop([1, 2, 3, 4, 5]))
print(calculate_sum_whileloop([0, 0, 0]))
print(calculate_sum_whileloop([-5, 3, 5]))
print(calculate_sum_whileloop([]))
