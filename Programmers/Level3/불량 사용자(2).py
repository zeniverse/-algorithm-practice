from itertools import product

def compare(user, role):
    if len(user) != len(role):
        return False
    
    for a, b in zip(user, role):
        if b != '*' and a != b:
            return False
    return True


def solution(user_id, banned_id):
    answer = []
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if compare(u, banned_id[i]):
                result[i].append(u)

    for r in product(*result):
        if len(set(r)) == len(banned_id):
            if set(r) not in answer:
                answer.append(set(r))

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))