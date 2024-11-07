# top -> down

def uniquePaths(m, n):
    dp = [[-1] * n for _ in range(m)]

    def dfs(r, c):
        if r == 0 and c == 0:
            dp[r][c] = 1
            return dp[r][c]
        
        ans = 0
        if dp[r][c] == -1:
            if r - 1 >= 0:
                ans += dfs(r - 1, c)
            if c - 1 >= 0:
                ans += dfs(r, c - 1)
            
            dp[r][c] = ans

        return dp[r][c]
    return dfs(m - 1, n - 1)


m = 3
n = 7
print(uniquePaths(m, n))