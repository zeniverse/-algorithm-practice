
k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]

def solution(k, ranges):
    answer = []

    # 콜라츠 추측
    arr = [k]
    while k != 1:
        if not k % 2:
            k //= 2
        else:
            k = k * 3 + 1
        arr.append(k)
    n = len(arr) - 1

    # 이전 인덱스에서 해당 인덱스까지의 넓이 저장(x의 길이는 항상 1)
    # i 에서 i + 1 까지의 넓이를 area라는 배열에 저장
    # 정적분의 결과는 사다리꼴의 넓이와 같고 높이(x의 좌표차)는 항상1
    # 사다리꼴 넓이는 (윗변 길이 + 아랫변 길이) * 높이 // 2 인데 높이는 항상 1로 고정
    # 따라서 i번째 y값과 i + 1번째 y값을 더한 뒤 2를 나눠준다
    area = [0]
    for i in range(1, len(arr)):
        area.append((arr[i - 1] + arr[i]) / 2)

    # ranges를 순회하며 유효하지 않은 구간은 -1을 더하고,
    # area[i] 는 i - 1부터 i까지의 넓이이므로 a + 1부터 n + b번째 까지의 넓이를 더한다
    for a, b in ranges:
        if a > n + b:
            answer.append(-1.0)
            continue
        answer.append(sum(area[a + 1: n + b + 1]))
    return answer

print(solution(k, ranges))