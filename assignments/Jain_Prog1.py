# Name : Vinit Kirit Jain
# Date of creation : 2023-09-02
# Programming Assignment 1 : Body Mass Index (BMI) Calculator

"""
Brief description :
BMI calculator calculates the Body Mass Index (BMI) for a user and provides an output based on the height and weight values entered.
"""


# asking the user their name
user_name = input("Please enter your name and then press enter : ")

# greeting the user
print("Hello, " + user_name + "!! Welcome to the BMI calculator!!")

# asking the user their height in meters and typecasting to float
user_height = float(input("Please enter your height in meters and then press enter : "))

# asking the user their weight in kilograms and typecasting to float
user_weight = float(input("Please enter your weight in kilograms and then press enter : "))

# a function to calculate BMI while taking height and weight as arguments
def calculate_BMI(height, weight):
    # calculating BMI using the formula
    bmi_result = weight / (height**2)

    # returning the result
    return bmi_result

# passing the user height and weight to BMI calculator function
bmi_result = calculate_BMI(user_height, user_weight)

# printing the bmi result
print("Your BMI result is " + str(bmi_result))

# interpreting the bmi and printing the result
if bmi_result < 18.4:
    print("Your BMI is low, which may require medical attention.")
elif bmi_result > 24.6:
    print("Your BMI is high, which may require medical attention.")
else:
    print("Your BMI is normal")
