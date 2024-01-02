import time
from typing import List
import math

class Unionfind:
    array = list()
    
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
    
    def is_connect (self, p:int, q:int):
        return self.array[p] == self.array[q]
    
    def union (self, p_id:int, q_id:int):
        p_value = self.array[p_id]
        q_value = self.array[q_id]
        
        for id in range(len(self.array)): 
            if self.array[id] == p_value:
                self.array[id] = q_value
    
new_find = Unionfind(10)
new_find.union(2,3)
print(new_find.is_connect(2,3))
print(new_find.array)