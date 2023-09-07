import time
from typing import List


def binary_search_recursive(
    value: int, arr: List[int], end_index: int, start_index: int = 0
) -> dict:
    # element search from left and not present
    if end_index:
        mid_index = (end_index - start_index) // 2 + start_index
        if end_index >= start_index:
            if value == arr[mid_index]:
                return {"found": True, "index": mid_index}
            elif value < arr[mid_index]:
                return binary_search_recursive(value, arr, mid_index - 1, start_index)
            elif value > arr[mid_index]:
                # avoid infinite call
                return binary_search_recursive(value, arr, end_index, mid_index + 1)

    return {"found": False}


def binary_search_iternate(value: int, arr: List[int], end_index: int) -> dict:
    r_index = end_index
    l_index = 0
    while l_index <= r_index and r_index > 0:
        mid_index = (r_index - l_index) // 2 + l_index
        if value == arr[mid_index]:
            return {"found": True, "index": mid_index}
        elif value < arr[mid_index]:
            r_index = mid_index - 1
        elif value > arr[mid_index]:
            l_index = mid_index + 1

    return {"found": False}


def binary_search_meta(value: int, arr: List[int], end_index: int) -> dict:
    if end_index: 
        l_index = 0
        r_index = 1

        while r_index < end_index and arr[r_index] < value:
            l_index = r_index
            r_index *= 2
        # ensure that r_index not go out of the range if search last value
        r_index = min(r_index, end_index)
        # binary search
        while l_index <= r_index and r_index > 0:
            mid_index = (r_index - l_index) // 2 + l_index
            if value == arr[mid_index]:
                return {"found": True, "index": mid_index}
            elif value < arr[mid_index]:
                r_index = mid_index - 1
            elif value > arr[mid_index]:
                l_index = mid_index + 1

    return {"found": False}


# Duplicate elements: search variants
def binary_search_first(value: int, arr: List[int], end_index: int) -> dict:
    r_index = end_index
    l_index = 0
    result = {"found": False}

    while l_index <= r_index and r_index > 0:
        mid_index = (r_index - l_index) // 2 + l_index
        if value == arr[mid_index]:
            result = {"found": True, "index": mid_index}
            # search in left
            r_index = mid_index - 1
        elif value < arr[mid_index]:
            r_index = mid_index - 1
        elif value > arr[mid_index]:
            l_index = mid_index + 1

    return result


def binary_search_last(value: int, arr: List[int], end_index: int) -> dict:
    r_index = end_index
    l_index = 0
    result = {"found": False}

    while l_index <= r_index and r_index > 0:
        mid_index = (r_index - l_index) // 2 + l_index
        if value == arr[mid_index]:
            result = {"found": True, "index": mid_index}
            # search in right
            l_index = mid_index + 1
        elif value < arr[mid_index]:
            r_index = mid_index - 1
        elif value > arr[mid_index]:
            l_index = mid_index + 1

    return result


start = time.perf_counter()

arr = [2, 3, 7, 10, 12, 18, 18, 21, 35, 36]
target = 36
index_n = len(arr)
# result = binary_search_recursive(target, arr, index_n - 1)
# result = binary_search_iternate(target, arr, index_n - 1)
# result = binary_search_first(target, arr, index_n - 1)
# result = binary_search_last(target, arr, index_n - 1)
result = binary_search_meta(target, arr, index_n - 1)

end = time.perf_counter()

print(f"{end - start} secs")

if result["found"]:
    print(f"{target} found at index {result['index']}")
else:
    print("Element not found")
