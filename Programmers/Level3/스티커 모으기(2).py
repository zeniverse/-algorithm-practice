

def solution(sticker):
    n = len(sticker)

    if n <= 3:
        return max(sticker)
        
    dp1 = [0] * n
    dp2 = [0] * n

    # dp1 -> 첫번째 스티커를 뗀 경우
    # dp2 -> 첫번째 스티커를 떼지 않은 경우

    dp1[0], dp1[1] = sticker[0], dp1[0]
    dp2[0], dp2[1] = 0, sticker[1]

    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1] ,dp1[i - 2] + sticker[i])

        
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1] ,dp2[i - 2] + sticker[i])


    return max(dp1[-2], dp2[-1])

sticker = [1, 3, 2, 5, 4]
print(solution(sticker))