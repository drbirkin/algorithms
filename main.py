import time


def linear_search(value, arr, index):
    for i in range(index):
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



arr = [2, 3, 7, 10, 12]
target = 2
index_n = len(arr)
index = index_n if index_n < len(arr) else index_n - 1

start = time.perf_counter()

result = linear_search(target, arr, index)

end = time.perf_counter()
print(f"{end - start} secs")

start = time.perf_counter()

result_recursive = linear_search_recursive(target, arr, index)

end = time.perf_counter()
print(f"{end - start} secs")

if result.get('is_found', False):
    print(f"{target} found at index {result.get('index', None)}")
else:
    print("Element not found")

print(
    f"At {result_recursive.get('index', None) if result_recursive.get('is_found', False) else None} is {target} found"
)
