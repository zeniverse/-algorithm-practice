from itertools import permutations


def compare(user, role):
    if len(user) != len(role):
        return False
    
    for a, b in zip(user, role):
        if b != '*' and a != b:
            return False
    return True


def solution(user_id, banned_id):
    res = 0
    res = []

    for per in permutations(user_id, len(banned_id)):
        flag = True
        for i in range(len(banned_id)):
            if not compare(per[i], banned_id[i]):
                flag = False

        if flag:
            if set(per) not in res:
                res.append(set(per))

    
    return len(res)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
