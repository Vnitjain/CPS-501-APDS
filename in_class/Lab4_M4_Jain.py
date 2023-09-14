# Author Name : Vinit Kirit Jain
# Creation Date : 2023-09-13

# Q1: Given a string s, find the length of the longest substring without repeating characters.

# importing time library to measure time
import time

# starting the timer
start_time = time.time()

# declaring and assigning input string
given_string = "jcmoiniadknopu"

# defining the longest non repeating substring
def longest_non_repeating_substring(input_string):
    # declaring a blank max substring which will keep the longest substring
    max_length_substring = ""
    # using two indices i and j to iterate through the string
    for i in range(len(input_string)):
        # declaring a blank list to keep track of all the characters already visited and it will be reset every iteration
        visited_characters_list = []
        for j in range(i,len(input_string)):
            # if the current character is not visited adding it to the visited list
            if input_string[j] not in visited_characters_list:
                # add the newly encountered character to the visited character list
                visited_characters_list.append(input_string[j])
            else:
                # if we encounter a character for the second time, we stop the loop as we only need the non repeating characters in substring
                break
            # if the string that we have is larger than the biggest substring we'll substitute it with the longer value
            if len(input_string[i:j])> len(max_length_substring):
                # assigning the new longer substring
                max_length_substring = input_string[i:j]
    # if the i and j pointers reach the end the output should be the input string as it has all unique characters
    if len(max_length_substring) == 0:
        return input_string
    else:
        return max_length_substring

#printing the final max substring
print("Input string: "+given_string+"\nThe longest substring is : "+longest_non_repeating_substring(given_string))

# Q2: Given a list of numbers, find the number that repeats the most.

# declaring a list of random numbers
number_list = [0,1,1,1,9,2,3,7,5,0,9,1,8,2,3,0,4,9,8,1,2,3,7,5,0,9,1,2,3,8,4]

# defining a function that counts the frequency of each number from the input list
def count_numbers(input_numbers):
    # declaring a blank dictionary to keep track of frequency of all the numbers
    number_frequency = {}
    # declaring a max count list to keep track of [maximum number, maximum occurrent of that number]
    max_count = [-1,-1]
    # iterating through the list of numbers
    for i in input_numbers:
        # if the number is present in the dictionary just increment the count
        if i in number_frequency:
            # increment the frequency of that number
            number_frequency[i] = number_frequency[i] + 1
        else:
            # defining the frequency if we have seen it for the first time
            number_frequency[i] = 1
        # if the frequency of number is greater than the max we can update the max count variable
        if number_frequency[i] > max_count[1]:
            max_count = [i,number_frequency[i]]
    # returning the max count list
    return max_count
# printing the final value
print("Input list: "+str(number_list)+"\nMaximum occurring number: "+str(count_numbers(number_list)[0]))

# ending the timer
end_time = time.time()
# printing the difference which will print time in milliseconds
print("Time: "+str((end_time-start_time)*1000)+" milliseconds")