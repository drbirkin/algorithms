import time
from typing import List

def binary_search_recursive(value: int, arr: List[int], end_index: int, start_index: int = 0) -> dict :
    # element search from left and not present
    if end_index: 
        mid_index = (end_index - start_index) // 2 + start_index
        if end_index >= start_index:
            if value == arr[mid_index]:
                return {"found": True, "index": mid_index}
            elif value < arr[mid_index]:
                return binary_search_recursive(value, arr, mid_index, start_index)
            elif value > arr[mid_index]:
                # avoid infinite call
                return binary_search_recursive(value, arr, end_index, mid_index + 1)
    
    return {"found": False}

def binary_search_iternate(value:int, arr: List[int], end_index: int) -> dict:
    r_index = end_index  
    l_index = 0  
    while l_index <= r_index and r_index > 0:
        mid_index = (r_index - l_index) // 2 + l_index
        if value == arr[mid_index]:
            return {"found": True, "index": mid_index} 
        elif value < arr[mid_index]:
            r_index = mid_index
        elif value > arr[mid_index]:
            l_index = mid_index + 1
    
    return {"found": False}
            
start = time.perf_counter()

arr = [2, 3, 7, 10, 12, 18, 21, 35, 36]
target = 38
index_n = len(arr)
# result = binary_search_recursive(target, arr, index_n - 1)
result = binary_search_iternate(target, arr, index_n - 1)

end = time.perf_counter()

print(f"{end - start} secs")

if result['found']:
    print(f"{target} found at index {result['index']}")
else:
    print("Element not found")
