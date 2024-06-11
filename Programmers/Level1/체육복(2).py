
n = 3
lost = [1, 2]
reserve = [2, 3]

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # reserve[:] 는 reserve를 복사한 배열
    # 아래서 같은 요소가 있을 때 reserve에서 지워주므로 복사한 배열로 for문을 돌려야한다
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    return n - len(lost)

print(solution(n, list, reserve))