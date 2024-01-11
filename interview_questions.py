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
    maximum = 0
    # O(n)
    def __init__(self, N:int):
        self.__length = N
        self.array = list(range(self.__length + 1))
        self.size = [1] * (N + 1)
    # O(logn)
    def find(self, value:int):
        if value < self.array[value]: self.maximum = self.array[value]
        else: self.maximum = value
        if value != self.array[value]:
            value = self.find(self.array[value])
        value = self.maximum
        return value
    # O(logn)
    def is_connect(self, p:int, q:int):
        return self.find(p) == self.find(q)
    # O(log(n)) TODO larger number as root
    def union (self, p:int, q:int):
        p_value = self.find(p)
        q_value = self.find(q)

        if p_value != q_value:

            if self.size[p_value] <= self.size[q_value]:
                self.array[p_value] = q_value
                self.size[q_value] += self.size[p_value]
            else:
                self.array[q_value] = p_value
                self.size[p_value] += self.size[q_value]

social_media = Socialmedia(10)
find_largest = Findlargest(10)
find_largest.union(8, 10)
find_largest.union(2, 8)
find_largest.union(2, 3)
find_largest.union(1, 3)
print(find_largest.is_connect(6,2))
print(find_largest.array)
print(find_largest.find(2))