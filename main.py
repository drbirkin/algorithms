import time
from typing import List
import math

class Solution:
    # def brute_force(self, arr):
    #     max_res = arr[0]
    #     for i in range(len(arr)):
    #         tmp = 0
    #         for j in range(i, len(arr)):
    #             tmp += arr[j]
    #             max_res = max(tmp, max_res)
    #     return max_res
         
    def kadane(self, arr):
        # final compare garuantees of max value at that stage
        res = arr[0][0]
        # check start again garuantees max value of tmp stage
        for j in range(len(arr)):
            tmp = arr[j][0]
            for i in range(1, len(arr[j])):
                tmp = max(tmp + arr[j][i], arr[j][i])
                
                res = max(res, tmp)
        return res   
    

case =  [[ 1,  2, -1, -4, -20],
          [-8, -3,  4,  2,   1],
          [ 3,  8, 10,  1,   3],
          [-4, -1,  1,  7,  -6]]

solution = Solution()

# print(solution.brute_force(case))
print(solution.kadane(case))