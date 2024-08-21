
k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]

def solution(k, ranges):
    answer = []

    # 콜라츠 추측을 이용해 num배열에 해당 값들을 추가해주고
    # 해당 값들을 이용한 정적분 누적합을 구하면 된다

    # 콜라츠 추측
    arr = [k]
    while k != 1:
        if not k % 2:
            k //= 2
        else:
            k = k * 3 + 1
        arr.append(k)
    n = len(arr) - 1

    prefix = [0] * (len(arr) + 1)

    # 누적합
    for i in range(2, len(arr) + 1):
        prefix[i] = prefix[i - 1] + (arr[i - 2] + arr[i - 1])/2
    for i in ranges:
        a, b = i[0] + 1, len(arr) + i[1]
        if a > b:
            answer.append(-1.0)
        else:
            answer.append(prefix[b] - prefix[a]) 

    return answer

print(solution(k, ranges))