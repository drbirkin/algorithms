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