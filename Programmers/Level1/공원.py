def solution(mats, park):
    answer = -1
    n = len(park)
    m = len(park[0])
    size = set()
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if park[i][j] == "-1":
                dp[i][j] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == 0:
                continue

            dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1
            size.add(dp[i][j])

    for i in mats:
        if i in size:
            answer = max(answer, i)
    return answer

wallet, bill = [5,3,2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]

print(solution(wallet, bill))

