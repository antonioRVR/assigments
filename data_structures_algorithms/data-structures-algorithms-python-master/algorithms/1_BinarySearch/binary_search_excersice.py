# ### Binary Search Exercise
# 1. When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

#     ```numbers = [1,4,6,9,10,5,7]```
    
# 2. Find index of all the occurances of a number from sorted list

#     ```
#     numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
#     number_to_find = 15  
#     ```
#    This should return 5,6,7 as indices containing number 15 in the array
    

from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)



  # 1


numbers = [1,4,6,9,10,5,7]
number_to_find = 5

index = binary_search_recursive(numbers, number_to_find, 0, len(numbers))
print(f"Number found at index {index} using binary search")

# returns -1 because the list is not sorted and the algortihm expects a sorted list

# 2

#  Find index of all the occurances of a number from sorted list

#     ```
#     numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
#     number_to_find = 15  
#     ```
#    This should return 5,6,7 as indices containing number 15 in the array


#  for this we make a few changes to the binary search algorithm

    
def find_all(numbers,number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    i = index - 1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return indices



numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  

index = find_all(numbers, number_to_find)
print(f"Number found at index {index} using binary search")