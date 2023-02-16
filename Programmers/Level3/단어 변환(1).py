
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        x, cnt = queue.popleft()

        if x == target:
            return cnt
        
        for i in range(0, len(words)):
            diff = 0
            word = words[i]

            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                queue.append([word, cnt + 1])
    return 0
    

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

