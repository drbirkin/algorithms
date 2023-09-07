import time
from typing import List

def binary_search_recursive(value: int, arr: List[int], end_index: int, start_index: int = 0) -> dict :
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


start = time.perf_counter()

arr = [2, 3, 7, 10, 12, 18, 21, 35, 36]
target = 2
index_n = len(arr)
result = binary_search_recursive(target, arr, index_n - 1)

end = time.perf_counter()

print(f"{end - start} secs")

if result['found']:
    print(f"{target} found at index {result['index']}")
else:
    print("Element not found")
