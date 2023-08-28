import time

def binary_search_iterate (value, arr):
    for i in range(N):
        if value == arr[i]:
            return i
    return False

start = time.perf_counter()

arr = [2, 3, 7, 10, 12]
target = 2
index_n = len(arr)
index = binary_search_iterate(target, arr)

end = time.perf_counter()

print(f'{end - start} secs')

if index or index == 0:
    print(f'{target} found at index {index}')
else:
    print('Element not found')
    