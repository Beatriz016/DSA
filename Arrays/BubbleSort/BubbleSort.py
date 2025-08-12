# How it works:

# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last.
# Go through the array as many times as there are values in the array.

# Bubble Sort Implementation
# To implement the Bubble Sort algorithm in a programming language, we need:

# An array with values to sort.
# An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

#arr = [64, 34, 25, 12, 22, 11, 90, 5]
arr = [7,12,9,11,3]
n = len(arr) # n = 5
for i in range(n - 1): # range(4)...
    for j in range(n-i-1): # range(4); range(3)...range(0)
        if arr[j] > arr[j+1] :
            #swap 
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            # arr[j], arr[j+1] = arr[j+1], arr[j]

print(f"Sorted Array: {arr}")



arr = [64, 34, 25, 12, 22, 11, 90, 5]
arr = [7,12,9,11,3]
n = len(arr) # n = 5
for i in range(n - 1): # range(4)...
    for j in range(n-i-1): # range(4); range(3)...range(0)
        if arr[j] > arr[j+1] :
            #swap 
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            # arr[j], arr[j+1] = arr[j+1], arr[j]

print(f"Sorted Array: {arr}")

        