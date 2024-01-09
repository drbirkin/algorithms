import time
from typing import List
import math

class Unionfind:
    array = list()
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
    # O(1)
    def is_connect (self, p:int, q:int):
        return self.array[p] == self.array[q]
    
    # O(n)
    def union (self, p_id:int, q_id:int):
        p_value = self.array[p_id]
        q_value = self.array[q_id]
        # Change all entries with p to q
        for id in range(len(self.array)): 
            if self.array[id] == p_value:
                self.array[id] = q_value
                
class Quickunion:
    array = list()
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
    # O(n)   
    def root(self, value:int):
        while value != self.array[value]:
            value = self.array[value]
        return value
    # O(n)
    def is_connect (self, p:int, q:int):
        return self.root(p) == self.root(q)
    # O(n)
    def union (self, p:int, q:int):
        p_value = self.root(p)
        q_value = self.root(q)
        # Change root value
        self.array[p_value] = self.array[q_value]
                
class Weight_QU:
    array = list()
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
        self.size = [1] * N
    # O(log(n)) in amortized time analysis, but not witth n-1 deep tree (O(n))
    def root(self, value:int):
        while value != self.array[value]:
            value = self.array[value]
        return value
    # O(log(n))
    def is_connect (self, p:int, q:int):
        return self.root(p) == self.root(q)
    # O(log(n))
    def union (self, p:int, q:int):
        p_value = self.root(p)
        q_value = self.root(q)
        
        if p_value != q_value:
        
            if self.size[p_value] <= self.size[q_value]:
                self.array[p_value] = q_value
                self.size[q_value] += self.size[p_value]
            else:
                self.array[q_value] = p_value
                self.size[p_value] += self.size[q_value]       

class Weight_Path_QU:
    array = list()
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
        self.size = [1] * N
    # O(log(n)) in amortized time analysis, but not witth n-1 deep tree (O(n))
    def root(self, value:int):
        # Path compression
        value = self.root(self.array[value])
        return value
    # O(log(n))
    def is_connect (self, p:int, q:int):
        return self.root(p) == self.root(q)
    # O(log(n))
    def union (self, p:int, q:int):
        p_value = self.root(p)
        q_value = self.root(q)
        
        if p_value != q_value:
        
            if self.size[p_value] <= self.size[q_value]:
                self.array[p_value] = q_value
                self.size[q_value] += self.size[p_value]
            else:
                self.array[q_value] = p_value
                self.size[p_value] += self.size[q_value]      
# Union find 
# time complexity n^2 on n operations (n * union operations)
union_find = Unionfind(10)
union_find.union(2,3)
print(union_find.array)
print(union_find.is_connect(2,3))

# Quick union
# time complexity n^2 on n operations but should be slightly performant
quick_union = Quickunion(10)
quick_union.union(2,4)
print(quick_union.array)
print(quick_union.is_connect(2,4))

# Weighted Quick union
# time complexity n*log(n) on n operations
weight_qu = Weight_QU(10)
weight_qu.union(2,4)
print(weight_qu.array)
weight_qu.union(1,6)
print(weight_qu.array)
weight_qu.union(6,8)
print(weight_qu.array)
print(weight_qu.is_connect(1,8))

# TODO improvements with weigthed QU and path comparision also both