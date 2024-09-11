import time
from typing import List
import math

class Solution:
    def brute_force(self, arr):
        max_res = arr[0]
        for i in range(len(arr)):
            tmp = 0
            for j in range(i, len(arr)):
                tmp += arr[j]
                max_res = max(tmp, max_res)
        return max_res
         
    def kadane(self, arr):
        # final compare garuantees of max value at that stage
        res = arr[0]
        # check start again garuantees max value of tmp stage
        tmp = arr[0]
        for i in range(1, len(arr)):
            tmp = max(tmp + arr[i], arr[i])
            
            res = max(res, tmp)
        return res   
    

case = [2, 3, -8, 7, -1, 2, 3]

solution = Solution()

print(solution.brute_force(case))
print(solution.kadane(case))