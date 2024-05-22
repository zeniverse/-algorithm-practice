
spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]

def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2

print(solution(spell, dic))
