import time
from typing import List
import math


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
        # l_index = 0
        # r_index = 1

        # while r_index < end_index and arr[r_index] < value:
        #     l_index = r_index
        #     r_index *= 2
        # ensure that r_index not go out of the range if search last value
        # r_index = min(r_index, end_index)
        # binary search
        # while l_index <= r_index and r_index > 0:
        #     mid_index = (r_index - l_index) // 2 + l_index
        #     if value == arr[mid_index]:
        #         return {"found": True, "index": mid_index}
        #     elif value < arr[mid_index]:
        #         r_index = mid_index - 1
        #     elif value > arr[mid_index]:
        #         l_index = mid_index + 1
        # return {"found": False}

        # Bit method
        # Set number of bits to represent
        lg = int(math.log2(end_index))

        # largest array index
        # while ((1 << lg) < n - 1):
        # lg += 1

        pos = 0
        for i in range(lg, -1, -1):
            if arr[pos] == value:
                return {"index": pos, "found": True}

            # Incrementally construct the
            # index of the target value
            #  => int + int  8 | 4 = 12 1000 | 0100 = 1100
            new_pos = pos | (1 << i)
            print(i, pos, 1 << i, pos | (1 << i))

            # find the element in one
            # direction and update position
            if (new_pos <= end_index) and (arr[new_pos] <= value):
                pos = new_pos

        # if element found return
        # pos otherwise -1
        return (
            {"index": pos, "found": True} if (arr[pos] == value) else {"found": False}
        )


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

def binary_uniform_lookup (value: int, arr: List[int], max_size: int, end_index: int) -> dict:
    table = uniform_table(max_size, end_index)
    
    index = table[0] - 1
    co = 0
    
    while table[co] != 0:
        if arr[index] == value: return {"found": True, "index": index}
        elif arr[index] < value:
            co += 1 
            index += table[co]
        else: 
            co += 1
            index -= table[co]
    
    return {"found": False}
        
def uniform_table (max_size: int, end_index: int) -> list :
    lookup_table = [0] * max_size
    pow = 1
    co = 0
    # print text part
    interval_textformat = {
        "interval_text": "",
        "start_interval": 0,
        "end_interval": 0
    }
    
    while True:
        pow <<= 1
        mid_interval = (end_index + (pow >> 1)) // pow
        lookup_table[co] = mid_interval
        
        # text part
        uniform_table_text(interval_textformat, lookup_table = lookup_table, co = co, end_index = end_index, pow = pow)
        
        if lookup_table[co] == 0: break
        co += 1
    
    print(interval_textformat["interval_text"])
    
    return lookup_table

# print seperated intervals
def uniform_table_text (interval_textformat, **args):
    lookup_table, co, pow, end_index = args.values()
    print(co)
    interval_textformat["end_interval"] = (interval_textformat["end_interval"] + lookup_table[co]) if( interval_textformat["end_interval"] + lookup_table[co] ) - 1> interval_textformat["end_interval"]  else 0
    print(f"( {end_index} + {pow >> 1} ) / {pow} = {lookup_table[co]}")
    print(co, pow, lookup_table[co])
    interval_textformat["interval_text"] += f'[{interval_textformat["start_interval"]}{(" - " + str(interval_textformat["end_interval"] - 1) + "], ") if interval_textformat["end_interval"] else "], "}' if lookup_table[co] > 0 else ''
    interval_textformat["start_interval"] += lookup_table[co]
    

start = time.perf_counter()

arr = range(0, 100001)
target = 12343
index_n = len(arr)
MAX_SIZE = 1000
# result = binary_search_recursive(target, arr, index_n - 1)
# result = binary_search_iternate(target, arr, index_n - 1)
# result = binary_search_first(target, arr, index_n - 1)
# result = binary_search_last(target, arr, index_n - 1)
# result = binary_search_meta(target, arr, index_n - 1)
result = binary_uniform_lookup(target, arr, MAX_SIZE, index_n)

end = time.perf_counter()

print(f"{end - start} secs")

if result["found"]:
    print(f"{target} found at index {result['index']}")
else:
    print("Element not found")
