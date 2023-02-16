
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    
    res = 0
    word_list = [begin]
    diff_word = list()

    while True:
        for w in word_list:
            diff_word.clear()

            for word in words:
                diff = 0

                for idx in range(0, len(begin)):
                    if w[idx] != word[idx]:
                        diff += 1
                    if diff > 1 : break

                if diff == 1:
                    diff_word.append(word)
                    words.remove(word)

        res += 1
        if target in diff_word:
            return res
        else:
            word_list = diff_word

    

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

