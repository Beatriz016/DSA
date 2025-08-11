# arr = [7, 12, 9, 4, 11, 3]

# global value
# for i in arr:
#     value = i
#     for j in arr:
#         if value < j :
#             print(f"{value} is lower than {j}")
#         else :
#             value = j
#             print(f"{value} is lower than {i}")

# print(f"Lowest value in the array: {value}")



arr = [7, 12, 9, 4, 11, 3]
minVal =  arr[0] 

for i in arr:
    if i < minVal:
        minVal = i
        print(minVal)


print(f"Lowest value in the array: {minVal}")

    


        




