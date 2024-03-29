# Exercise 10: Create a new list from two list using the following condition

# Create a new list from two list using the following condition
# Given two list of numbers, 
# write a program to create a new list such that the new list should contain odd numbers from the first list
# even numbers from the second list.

def merge_list(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        #Verify whether the present value is odd.
        if num % 2 != 0:
            result_list.append(num)

    # iterate second list
    for num in list2:
        # Verify whether the present value is even.
        if num % 2 == 0:
            result_list.append(num)
    return result_list

list1 = [5, 10, 35, 50, 63, 71]
list2 = [20, 55, 40, 80, 92, 110]
print("result list:", merge_list(list1, list2))

