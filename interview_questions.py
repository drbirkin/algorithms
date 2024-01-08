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
        self.array = [{"name": f"name{i}"} for i in range(self.__length + 1)]
    # O(n) 
    def is_connect(self, p_name:str, q_name:str):
        p1, p2 = ''
        for profile in self.array:
            if profile.get('name') == p_name:
                p1 = profile
            elif profile.get('name') == q_name:
                p2 = profile
                
        return p1.get["name"] == p2.get["name"]
    
