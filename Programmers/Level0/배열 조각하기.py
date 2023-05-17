
def solution(arr, query):
    for i in range(len(query)):
        if i % 2:
            arr = arr[query[i]:]
        else:
            arr = arr[:query[i] + 1]
    return arr
        
arr =[0, 1, 2, 3, 4, 5]
query = [4, 1, 2]
print(solution(arr, query))