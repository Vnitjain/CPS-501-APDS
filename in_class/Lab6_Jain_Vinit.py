#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:11:53 2023

@author: Vinit Jain
@assignment: Lab 6 M4
"""

# importing the random library to generate random numbers
import random


# defining a function to generate a two digit random number
def generate_random_number():
    return int(random.random() * 10)


# Q1: Define a matrix of size m and n using lists inside of list and initialize it
# with random numbers. m = rows, n = columns
def create_matrix(m, n):
    # defining a blank matrix
    matrix = []
    # running a loop to add the rows
    for i in range(m):
        # defining a temporary list for the columns in the rows
        temp_list = []
        for j in range(n):
            # adding the random generated number to the temporary list
            temp_list.append(generate_random_number())
        # adding the temporary list to the matrix as a new row
        matrix.append(temp_list)
    # returning the matrix
    return matrix


print(create_matrix(15, 15))


# Q2 : Sets - given a list of items see if there are any duplicates. Only use lists and comparisons.
# Return a bool


def is_a_set(list1):
    # iterating throught the list and comparing each element with other elements
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            # if there are duplicates return false immediately
            if list1[i] == list1[j]:
                return False
    # return true if the loop goes through with any duplicates
    return True


print(is_a_set([1, 2, 3, 4]))
# Q3 : Return a list of n random numbers


def return_list(n):
    # defining an empty list to hold random numbers
    random_number_list = []
    for i in range(n):
        # appending n number of random numbers to the list
        random_number_list.append(generate_random_number())
    # returning the random list
    return random_number_list


random_list = return_list(5)
print(random_list)

# Q4 : Traverse the list one by one and find the minimum number


def return_minimum(list1):
    # using the first element as the minimum number
    min = list1[0]
    # iterating throught the list and finding the minimum number
    for i in range(1, len(list1)):
        # if the number is smaller than minimum assign a new value to minimum
        if list1[i] < min:
            min = list1[i]
    # returning miniumum value
    return min


print(return_minimum(random_list))


# Q5 : Design a stack that supports push, pop. Then initilaze it and fill it with 10 random numbers.
# then delete last three elements and print the stack
# This mean creating a class with the methods: push, pop


class Stack:
    # declaring blank list in constructor
    def __init__(self):
        self.stack = []

    # adding a random numbers to the stack
    def push(self):
        self.stack.append(generate_random_number())

    # popping the last element of the list
    def pop(self):
        return self.stack.pop()


new_stack = Stack()

new_stack.push()
new_stack.push()
new_stack.push()
new_stack.push()
new_stack.push()
new_stack.pop()
print(new_stack.stack)
