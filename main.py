import time
from typing import List
from concurrent.futures import ThreadPoolExecutor

def linear_search(value, arr, index):
    for i in range(index + 1):
        if value == arr[i]:
            return {"index": i, "is_found": True}
    return {"is_found": False}


def linear_search_recursive(value, arr, index):
    if index < 0:
        return {"is_found": False}
    elif arr[index] == value:
        return {"index": index, "is_found": True}
    else:
        return linear_search_recursive(value, arr, index - 1)


def linear_search_sentinel(value, arr):
    last_index = len(arr) - 1
    last_element = arr[last_index]
    arr[last_index] = value

    # Element to be searched is
    # placed at the last index
    i = 0
    while arr[i] != value:
        i += 1

    arr[last_index] = last_element

    if i < last_index or arr[last_index] == value:
        return {"index": i, "is_found": True}
    else:
        return {"is_found": False}


# improve the Linear Search Algorithm
def linear_search_transposition(value, arr, index):
    # improve performance for mulitple search of same value
    # modifying array/list
    for i in range(index + 1):
        if arr[i] == value:
            if i - 1 >= 0:
                arr[i - 1], arr[i] = value, arr[i - 1]
            return {"index": i, "is_found": True}
    return {"is_found": False}


def linear_search_front_head(value, arr, index):
    # swap fist elment with found element
    for i in range(index + 1):
        if arr[i] == value:
            arr[0], arr[i] = value, arr[0]
            return {"index": i, "is_found": True}
    return {"is_found": False}


def linear_search_hash_table(arr: List[int], value: int, index: int) -> dict:
    hash_table = dict()

    for i in range(index + 1):
        hash_table[arr[i]] = i
    if value in hash_table:
        return {"index": hash_table.get(value, None), "is_found": True}
    else:
        return {"is_found": False}


def linear_search_multi_thread( value: int, arr: List[int], index: int, n: int) -> dict:
    for i in range(n * index // thread_max, (n + 1) * (index + 1) // thread_max):
        if value == arr[i]:
            return {"index": i, "is_found": True}
        else:
            return {"is_found": False}


def performance_tester(fn, target, *args):
    start = time.perf_counter()
    result = fn(target, *args)
    end = time.perf_counter()
    print(f"{end - start} secs")

    print(
        f"At {result.get('index', None) if result.get('is_found', False) else None} is {target} found"
    )


target = 10
arr = list(range(target + 1))
index_n = len(arr)
index = index_n if index_n < len(arr) else index_n - 1
thread_max = 10

# linear search
performance_tester(linear_search, target, arr, index)

# recursive linear search
performance_tester(linear_search_recursive, target, arr, index)

# sentinel linear search
performance_tester(linear_search_sentinel, target, arr)

# improvements with transposition

# transposition
# while arr[0] != target:
#     performance_tester(linear_search_transposition, target, arr, index)

# front/head
# while arr[0] != target:
#     performance_tester(linear_search_front_head, target, arr, index)
# print(arr[0])

# hash table
performance_tester(linear_search_hash_table, arr, target, index)

# multithreading
with ThreadPoolExecutor(max_workers=thread_max) as executor:
    for i in range(thread_max + 1):
        executor.submit(performance_tester, linear_search_multi_thread, target, arr, index, i)