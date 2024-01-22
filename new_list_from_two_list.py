# Exercise 10: Create a new list from two list using the following condition

# Create a new list from two list using the following condition
# Given two list of numbers, 
# write a program to create a new list such that the new list should contain odd numbers from the first list
# even numbers from the second list.

def merge_list(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)



