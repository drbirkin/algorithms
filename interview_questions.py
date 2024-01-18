import time
from typing import List
import math

# Question 1
# Social network connectivity. Given a social network containing
# n members and a log file containing
# m timestamps at which times pairs of members formed friendships, TODO: design an algorithm to determine the earliest time
# at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend).
# Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be
# mlogn or better and use extra space proportional to
# n.

class Socialmedia:
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
        self.size = [1] * N
    # O(logn)
    def root(self, id:int):
        profile = self.root(self.array[id])
        return profile
    # O(logn)
    def is_connect(self, p_id:int, q_id:int):
        p_friend = self.root[p_id]
        q_friend = self.root[q_id]

        return p_friend == q_friend
    # O(logn)
    def union(self, p:int, q:int):
        p_friend = self.root(p)
        q_friend = self.root(q)

        if p_friend != q_friend:

            if self.size[p_friend] < self.size[q_friend]:
                p_friend, q_friend = q_friend, p_friend
            self.array[q_friend] = p_friend
            if self.size[p_friend] == self.size[q_friend]:
                self.size[p_friend] += 1

# Question 2
# Union-find with specific canonical element. Add a method
# find() to the union-find data type so that
# find(i) returns the largest element in the connected component containing i.
# The operations,
# union(),
# connected(), and
# find() should all take logarithmic time or better.

# For example, if one of the connected components is
# {1,2,6,9}, then the find() method should return
# 9 for each of the four elements in the connected components.

class Findlargest:
    array = list()
    maximum_values = list()
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
        self.maximum_values = list(range(self.__length + 1))
        self.size = [1] * (N + 1)
    # O(logn)
    def find(self, value:int):
        if value != self.array[value]:
            value = self.find(self.array[value]).get("root")
        return {
            "root": value,
            "maximum": self.maximum_values[value]}
    # O(logn)
    def is_connect(self, p:int, q:int):
        return self.find(p).get("root") == self.find(q).get("root")
    # O(log(n)) TODO larger number as root
    def union (self, p:int, q:int):
        p_obj = self.find(p)
        q_obj = self.find(q)
        p_max, p_root = p_obj.get("maximum"), p_obj.get("root")
        q_max, q_root = q_obj.get("maximum"), q_obj.get("root")

        if p_obj != q_obj:

            if self.size[p_root] <= self.size[q_root]:
                # path q tree
                if p_max >= q_max : self.maximum_values[q_root] = p_max
                # elif not self.maximum_values[q_obj]: self.maximum_values[q_obj] = q_obj
                self.array[p_root] = q_root
                self.size[q_root] += self.size[p_root]
            else:
                # path p tree
                if q_max >= p_max: self.maximum_values[p_root] = q_max
                # elif not self.maximum_values[p_obj]: self.maximum_values[p_obj] = p_obj
                self.array[q_root] = p_root
                self.size[p_root] += self.size[q_root]

# Question 3
# Successor with delete. Given a set of
# n integers
# S={0,1,...,n−1} and a sequence of requests of the following form:

# Remove
# x from
# S

# Find the successor of
# x: the smallest
# y in
# S such that
# y≥x.

# design a data type so that all operations (except construction)  take logarithmic time or better in the worst case.

class Delete_successor:
    array= list()
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
        self.size = [1] * (N + 1)
    # O(1)
    def find(self, value:int):
        # O(1)
        if value != self.array[value]:
            # find smallest successor >= delete
            value = self.find(self.array[value])

        return value
    # O(logn)
    def is_connect(self, p:int, q:int):
        return self.find(p) == self.find(q)
    # O(logn)
    def delete(self, p:int):
        self.tmp_successor_root = self.find(p)
        if p + 1 <= self.__length:
            self.array[p] = p + 1


social_media = Socialmedia(10)
find_largest = Findlargest(10)
delete_successor = Delete_successor(100)
# find_largest.union(10, 8)
# print(find_largest.array)
# print(find_largest.find(10))
# find_largest.union(2, 8)
# print(find_largest.array)
# print(find_largest.find(10))
# find_largest.union(4, 3)
# print(find_largest.array)
# find_largest.union(1, 3)
# print(find_largest.array)
# find_largest.union(9, 6)
# print(find_largest.array)
# find_largest.union(3, 7)
# print(find_largest.array)
# find_largest.union(1, 2)
# print(find_largest.find(10))

# print(find_largest.array)
# print(find_largest.is_connect(1,2))
# print(find_largest.find(9))


delete_successor.delete(4)
delete_successor.delete(3)
delete_successor.delete(1)
delete_successor.delete(100)
print(delete_successor.is_connect(2, 5))
print(delete_successor.find(3))
print(delete_successor.find(1))