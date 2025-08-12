# Leetcode 4
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = nums1 + nums2
        print("Array", arr)
        # arr.sort()
        # print("sort: ",arr)

        n = len(arr)

        # Bubble Sort (Slow but accepted)
        for i in range(n -1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        
        print("Bubble Sorted Array: ", arr)

        if (n % 2 == 0): # even 

            # n // 2 gives the middle index for even-length arrays
            # Adding +1 means the slice will go up to but not including that index + 1
            # arr[start:end] -  Get the two middle elements when length is even

            middle = arr[(n // 2) - 1 : (n // 2) + 1] 
            print("middle: ", middle)

            median = (middle[0] + middle[1]) / 2
            print(f"Median: {median:.5f}")
            print(" ")

        else:
             # The middle element index is (n - 1) = 3 - 1 =  2,  2 // 2 = 1
             median = float(arr[(n - 1) // 2] )
             print("Median: ", median)

        return 0.0  

# Local test
sol = Solution()
sol.findMedianSortedArrays([1, 2], [3, 4])
sol.findMedianSortedArrays([1, 3], [2])