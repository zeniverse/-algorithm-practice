
babbling = ["wooyemawooye", "mayaa", "ymaeaya"]

def solution(babbling):
    res = 0

    for word in babbling:
        stack = ''
        prev = ''

        for i in word:
            stack += i

            if prev != stack and stack in ["aya", "ye", "woo", "ma"]:
                prev = stack
                stack = ''

        if len(stack) == 0:
            res += 1

    return res

print(solution(babbling))