# How it works:

# Go through the array to find the lowest value.
# Move the lowest value to the front of the unsorted part of the array.
# Go through the array again as many times as there are values in the array.

# [ 7, 12, 9, 11, 3]
# [ 3, 7, 12, 9, 11]
# [ 3, 7, 9, 12, 11]
# [ 3, 7, 9, 11, 12]

# Selection Sort Implementation
# To implement the Selection Sort algorithm in a programming language, we need:

# An array with values to sort.
# An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n−1 times.


my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n-1): # 0, 8
    min_index = i # min = i = 0, 1, 2...
    for j in range(i+1, n): # 0 + 1 = (1, 8) 
        if my_array[j] < my_array[min_index]: # j = 1[34] < (min[0] = min[64])
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)

# Selection Sort Shifting Problem

# In the code above each time the next lowest value array element is rmeoved, all the following elements must be shifted one place down to make up for the removal. These shifting operaton takes a lot of time.



# Here is an implementation of the improved Selection Sort, using swapping:

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j 
    
    # swap
    temp = my_array[i]
    my_array[i] = my_array[min_index]
    my_array[min_index] = temp

    # tuple swap 
    # my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array using swapping:", my_array)

