# Author Name : Vinit Kirit Jain
# Creation Date : 2023-09-06

# Question 1 : Reversing the string

# declaring the function to reverse string by taking the input string
def reverse_string(input_string):
    # declaring an empty list
    reversed_list = []
    # iterating through each string character in a reverse order
    for i in range(len(input_string) - 1, -1, -1):
        # appending each element in the new list
        reversed_list.append(input_string[i])
    # converting the list into string by using in built function join
    reversed_string = "".join(reversed_list)
    # returning the reversed string
    return reversed_string

# printing the reversed string into the console
print(reverse_string("Vinit Jain"))

# Question 2 : Merging and sorting two lists

# declaring the function to merge and sort lists by taking two lists
def merge_and_sort(first_list, second_list):
    # declaring an empty list
    merged_and_sorted_list = []
    # initializing the two pointers i and j
    i = 0
    j = 0
    # iterating only till the length of the lists
    while i < len(first_list) and j < len(second_list):
        # comparing the two elements from the lists and adding the lower character to the final list
        if first_list[i] < second_list[j]:
            merged_and_sorted_list.append(first_list[i])
            # iterating i once it has been added to the final list
            i += 1
        # comparing the two elements from the lists and adding the lower character to the final list
        elif second_list[j] < first_list[i]:
            merged_and_sorted_list.append(second_list[j])
            # iterating j once it has been added to the final list
            j += 1
        # comparing the two elements from the lists and adding the equal characters to the final list
        else:
            merged_and_sorted_list.append(first_list[i])
            merged_and_sorted_list.append(second_list[j])
            # iterating i & j once it has been added to the final list
            i += 1
            j += 1
    # the above loop will reach the end of one of the lists so adding all the elements till the end of the list
    while i < len(first_list):
        merged_and_sorted_list.append(first_list[i])
        i += 1
    while j < len(second_list):
        merged_and_sorted_list.append(second_list[j])
        j += 1
    # returning the final list
    return merged_and_sorted_list

# printing the merged and sorted list into the console
print(merge_and_sort(["a", "c", "d","t","x"], ["b", "e", "f","g","z"]))
