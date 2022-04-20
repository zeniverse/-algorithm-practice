n = int(input())
arr = list(map(int, input().split()))
arr_sort = list(sorted(set(arr)))

arr_sort = {arr_sort[i] : i for i in range(len(arr_sort))}
print(*[arr_sort[i] for i in arr])