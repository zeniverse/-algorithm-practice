
common = [2, 4, 8]

def check(arr):
    diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        if diff != arr[i] - arr[i - 1]:
            return False
    return True


def solution(common):

    if check(common):
        diff = common[-1] - common[-2]
        return common[-1] + diff
    else:
        diff = common[-1] // common[-2]
        return common[-1] * diff


print(solution(common))
