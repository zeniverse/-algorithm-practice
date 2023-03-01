

def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
        
    # 1. 맨 앞 스티커를 떼는 경우
    dp = [0] * len(sticker)
    dp[0] = sticker[0]
    dp[1] = sticker[0]

    for i in range(2, len(sticker)-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
        
    res = max(dp)

    # 2. 맨 앞 스티커를 떼지 않는 경우
    dp = [0] * len(sticker)
    dp[0] = 0
    dp[1] = sticker[1]

    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])

    return max(res, max(dp))

sticker = [1, 3, 2, 5, 4]
print(solution(sticker))