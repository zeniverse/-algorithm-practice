from sys import maxsize
import heapq

def solution(board):
    n = len(board)
    costBoard = [[[maxsize] * n for _ in range(n)] for _ in range(4)]

    for i in range(4):
        costBoard[i][0][0] = 0

    # BFS
    # 방향 : 동 - 0, 서 - 1, 남 - 2, 북 - 3
    # (비용, x, y, 방향)
    heap = [(0, 0, 0, 0), (0, 0, 0, 2)]

    while heap:
        cost, x, y, d = heapq.heappop(heap)

        for dx, dy, dd in ((1, 0, 0), (-1, 0, 1), (0, 1, 2), (0, -1, 3)):
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny]:
                continue    
            
            newCost = cost + (100 if d == dd else 600)

            if costBoard[dd][nx][ny] > newCost:
                costBoard[dd][nx][ny] = newCost
                heapq.heappush(heap, (newCost, nx, ny, dd))

    return min(costBoard[0][n - 1][n - 1], costBoard[1][n - 1][n - 1], costBoard[2][n - 1][n - 1], costBoard[3][n - 1][n - 1]) 

board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(board))