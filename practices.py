from typing import List
import math
# Number of comparisons in each direction for m queries in linear search

# Given an array containing N distinct elements. There are M queries, each containing an integer X and asking for the index of X in the array. For each query, the task is to perform linear search X from left to right and count the number of comparisons it took to find X and do the same thing right to left. In the end, print the total number of comparisons in both directions among all the queries.
def bi_directional_query_comparision (arr: List[int], query: List[int]) -> int:
    right_compare_amount = 0
    left_compare_amount = 0
    amount_list = []
    for q in query:
        # left to right
        for element in arr:
            right_compare_amount += 1
            if element == q:
                amount_list.append(right_compare_amount)
                break
        # right to left 
        for i in range(len(arr), 0, -1):
            left_compare_amount += 1
            if arr[i - 1] == q:
                amount_list.append(left_compare_amount)
                break
    # print(amount_list)
    return sum(amount_list)

arr = [2, 4, 7, -9, 10, 8, 12]
query = [1, 3, 7, 10, -9]

sum_comparison = bi_directional_query_comparision(arr, query)

print(sum_comparison)

# Search an element in an unsorted array using minimum number of comparisons

# Given an array of n distinct integers and an element x. Search the element x in the array using minimum number of comparisons. Any sort of comparison will contribute 1 to the count of comparisons. For example, the condition used to terminate a loop, will also contribute 1 to the count of comparisons each time it gets executed. Expressions like while (n) {n–;} also contribute to the count of comparisons as value of n is being compared internally so as to decide whether or not to terminate the loop. 
def less_comparision (arr: List[int], n: int, target: int) -> dict:
    count = 0
    backup = 0
    for i in range(0, n):
        count += 1
        if arr[i] == target: 
            return {
                'comparision_count': count,
                'found': True
            }
        count += 1
        if arr[n // 2] == target: 
            return {
                'comparision_count': count,
                'found': True
            }
        count += 1
        if arr[-(i + 1)] == target: 
            return {
                'comparision_count': count,
                'found': True
            }
    return {
        'comparision_count': count,
        'found': False
    }
    
    # if arr[-1] == target: 
    #     count += 1
    #     return {
    #             'comparision_count': count,
    #             'found': True
    #         }
    
    # backup = arr[-1]
    # arr[-1] = target
    
    # for i in range(0, n):
    #     count += 1
    #     if arr[i] == target: 
    #         arr[n - 1] = backup
    #         if i < (n - 1):
    #             return {
    #                 'comparision_count': count,
    #                 'found': True
    #             }
        
        # case of not present in list is excluded
        # arr[-(i + 1)] = backup
        # backup = arr[n-(i + 2)] S
        # arr[n-(i + 2)] = target
        
    # return {
    #     'comparision_count': count,
    #     'found': False
    # }
    
        
less_compare = less_comparision(arr, len(arr), -9)
print(less_compare, arr)
