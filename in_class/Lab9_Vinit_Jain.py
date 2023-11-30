# Name: Vinit Jain
# Date: 2023-11-01
# Class: CPS501
# Assignment: Lab 9

# re - regular expression
import re
from functools import wraps

# Today we will be working on decorators, regular expressions.
# For each I will provide you an example on how each works and what I am looking for.
# Decorators allow you to pass a function through a wrapper that can access
# the functions arguments and run code as well as the function passed into it
# example:


def example_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Start: ")
        func(*args, **kwargs)
        print("Finish: ")

    return wrapper


@example_decorator
def printHelloWorld(number):
    for i in range(number):
        print("Hello World")


printHelloWorld(2)

# Q1: Write a decorator that measures and prints the time taken by a function to execute.
# and then define another function, decorate it with the decorator and run it.
# Don't forget to use @wraps(func) as in the example above

# importing time module to measure the time for the function to execute
import time


# decorator function to take in the input function and then call it
def measure_time(func):
    # using in built wraps decarator to pass in the function to be called
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        # passing the arguments from the input funtion and then calling it
        func(*args, **kwargs)
        end = time.time() - start
        # printing the measured time
        print("Time taken: " + str(round(end, 3)) + " s")

    return wrapper


# using the decorator to measure time
@measure_time
def count_till_n(n):
    for i in range(n):
        print(i)


count_till_n(50)

# A regular expression is a sequence of characters that defines a search pattern
# https://docs.python.org/3/library/re.html
# For the next two questions, the link above contains all information to answer them correctly.

# Regular expression example:

text = "apple;banana,orange:grape"
pattern = r"[;,:]"
result = re.split(pattern, text)
print(result)

# vs. :

text = "apple;banana,orange:grape"
pattern = r"[;,]"
result = re.split(pattern, text)
print(result)

# Q2: define the pattern to search the string for the word python
text = "Python is fun, isn't Python?"
#'Python' will be the pattern that needs to be recognized
pattern = r"Python"

# iterating through all the results of the re finditer function
for match in re.finditer(pattern, text):
    start, end = match.span()
    # printing the start and end index of the pattern
    print(f"Found '{pattern}' at index: {start}-{end}")
# Found 'Python' at index: 0-6
# Found 'Python' at index: 21-27

# Q3: Return list of all words in the sentence, no punctuation
text = "Hello, world! How is your day?"
# using this pattern where we have specified one or more occurrences of a to z characters and A to Z characters
pattern = r"[a-zA-z]+"
tokens = re.findall(pattern, text)
print(tokens)
# Output: ['Hello', 'world', 'How', 'is', 'your', 'day']
