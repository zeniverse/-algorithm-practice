
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
     dp = [[0 for _ in range(4)] for _ in range(len(land))]

     for i in range(len(land)):
          if i == 0:
               dp[0] = land[0]
               continue

          for j in range(4):
               dp[i][j] = land[i][j] + max([dp[i - 1][k] for k in range(4) if k != j])

     return max(dp[-1])

print(solution(land))