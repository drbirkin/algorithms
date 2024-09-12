import time
from typing import List
import math

class Solution:
    def brute_force(self, arr, K):
        max_val = 0
        
        for i in range(len(arr) - K + 1):
            tmp = 0
            for j in range(K):
                tmp += arr[i + j]
                
            if tmp > max_val:
                max_val = tmp

        return max_val
    

case = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

solution = Solution()

# print(solution.brute_force(case))
print(solution.brute_force(case, 3))