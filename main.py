import time
from typing import List
import math

class Solution:
    def sort(self, arr, n):
        low = 0
        high = n -1
        mid = 0
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr   
    

case = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

solution = Solution()

# print(solution.brute_force(case))
print(solution.sort(case, len(case)))