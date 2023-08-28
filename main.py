import time

def linear_search (value, arr, N):
    for i in range(N):
        if value == arr[i]:
            return i
    return False

start = time.perf_counter()

arr = [2, 3, 7, 10, 12]
target = 2
index_n = len(arr)
index = linear_search(target, arr, index_n)

end = time.perf_counter()

print(f'{end - start} secs')

if index or index == 0:
    print(f'{target} found at index {index}')
else:
    print('Element not found')
    