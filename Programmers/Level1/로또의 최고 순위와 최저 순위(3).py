lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    answer = [0, 0]
    score = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    compare = set(lottos) & set(win_nums)
    answer[0] = score[len(compare) + lottos.count(0)]
    answer[1] = score[len(compare)]
    
    return answer

print(solution(lottos, win_nums))