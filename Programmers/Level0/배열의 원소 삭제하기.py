
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]

arr = [293, 1000, 395, 678, 94]
delete_list = [94, 777, 104, 1000, 1, 12]
print(solution(arr, delete_list))