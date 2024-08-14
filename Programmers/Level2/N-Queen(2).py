
# 퀸은 가로 세로 대각선 아무 방향으로 한쪽으로 쭉 이동할 수 있다
# 즉, 퀸이 있는 자리를 기준으로 가로 세로 대각선 방향에 다른 퀸이 존재하면 안된다

def nqueen(queens, next_queen, n):
    global answer

    if next_queen in queens:
        return
    
    for row, col in enumerate(queens):
        next_queen_row = len(queens)
        if abs(next_queen - col) == next_queen_row - row:
            return
        
    queens.append(next_queen)

    if len(queens) == n:
        answer += 1
        return
    
    for next_queen in range(n):
        nqueen(queens[:], next_queen, n)

def solution(n):
    global answer
    answer = 0

    for next_queen in range(n):
        queens = []
        nqueen(queens, next_queen, n)

    return answer

print(solution(4))