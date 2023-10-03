# Author: Vinit Kirit Jain
# Assignment: Lab 5 M4
# Date: 2023-09-20
# Class:


# Question 1: create a list of random numbers between 0 and 10 of length n, use random.random()

# importing the random library
import random


def create_random_list(n):
    # creating a blank list
    l = []
    # iterating through range given as the input
    for i in range(n):
        # generating random numbers from 0,10 including both 0 and 10
        random_number = random.randint(0, 11)
        # appending the number to the final list
        l.append(random_number)
    # returning the final list with random numbers
    return l


# Question 2: take a list l and iterate through it. Return a list where every corresponding number of l is the floor of it

# importing the math library
import math


def iterate_floor(l):
    # declaring an empty result list
    result_list = []
    # iterating through input list
    for i in l:
        # finding the floor value for each entry in the input list and assigning to variable floor value
        floor_value = math.floor(i)
        # appending the floor values to the result list
        result_list.append(floor_value)
    # returning the result list with floor value
    return result_list


# Question 3: create a dictionary using two lists: authors and books.
def create_dictionary(authors, books):
    # create a blank dictionary
    dictionary = {}
    # iterating through the values of authors list and adding each value to the final dictionary
    for i in range(len(authors)):
        # adding each author with book name to the dictionary as key value pair
        dictionary[authors[i]] = books[i]
    # returning the final dictionary
    return dictionary


# Question 4: search the dictionary using a string, return index
def find_index(book, dictionary):
    # iterating throught each key in the dictionary
    for i in dictionary:
        # using the key to find the value and comparing it to the required book value
        if dictionary[i] == book:
            # if the entry is found return the author/key back
            return i


authors = ["stephen hawking", "daniel kahneman", "donald knuth", "andrew tanenbaum"]
books = [
    "a brief history in time",
    "thinking, fast and slow",
    "the art of computer programming",
    "computer networks",
]
book = "the art of computer programming"

# call each function and print output
# question 1 output
print(create_random_list(5))
# question 2 output
print(iterate_floor([1.01, 2.99]))
# question 3 output
dictionary = create_dictionary(authors, books)
print(dictionary)
# question 4 output
print(find_index(book, dictionary))
