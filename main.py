import time


def linear_search(value, arr, index):
    for i in range(index + 1):
        if value == arr[i]:
            return {"index": i, "is_found": True}
    return {}


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

    i = 0
    while arr[i] != value:
        i += 1

    arr[last_index] = last_element

    if i < last_index or arr[last_index] == value:
        return {"index": i, "is_found": True}
    else:
        return {"is_found": False}


target = 120000
arr = list(range(target + 1))
index_n = len(arr)
index = index_n if index_n < len(arr) else index_n - 1

# linear search
start = time.perf_counter()

result = linear_search(target, arr, index)

end = time.perf_counter()
print(f"{end - start} secs")

print(
    f"At {result.get('index', None) if result.get('is_found', False) else None} is {target} found"
)

# recursive linear search
start = time.perf_counter()

result_recursive = linear_search_recursive(target, arr, index)

end = time.perf_counter()
print(f"{end - start} secs")

print(
    f" (recursive) At {result_recursive.get('index', None) if result_recursive.get('is_found', False) else None} is {target} found"
)

# sentinel linear search
start = time.perf_counter()

result_sentinel = linear_search_sentinel(target, arr)

end = time.perf_counter()
print(f"{end - start} secs")

print(
    f" (sentinel) At {result_sentinel.get('index', None) if result_sentinel.get('is_found', False) else None} is {target} found"
)
