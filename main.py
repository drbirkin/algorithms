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
    
    def sliding_window(self, arr, K):
        window_sum = sum(arr[:K])
        max_val = window_sum
        
        for i in range(len(arr) - K):
            window_sum = window_sum - arr[i] + arr[K + i]
            max_val = max(window_sum, max_val)
            
        return max_val
    

case = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

solution = Solution()

# print(solution.brute_force(case))
print(solution.brute_force(case, 3))
print(solution.sliding_window(case, 3))