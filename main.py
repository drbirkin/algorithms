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
class Quickunion:
    array = list()
    
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
        
    def root(self, value:int):
        while value != self.array[value]:
            value = self.array[value]
        return value
    
    def is_connect (self, p:int, q:int):
        return self.root(p) == self.root(q)
    
    def union (self, p:int, q:int):
        p_value = self.root(p)
        q_value = self.root(q)
        
        for id in range(len(self.array)): 
            if self.array[id] == p_value:
                self.array[id] = q_value

# Union find 
# time complexity n^2
union_find = Unionfind(10)
union_find.union(2,3)
print(union_find.is_connect(2,3))
print(union_find.array)

# Quick union
# time complexity n
quick_union = Quickunion(10)
quick_union.union(2,4)
print(quick_union.is_connect(2,4))
print(quick_union.array)

# TODO improvements with weigthed QU and path comparision also both