
spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]

def solution(spell, dic):
    spell.sort()

    for word in dic:
        arr = sorted(list(word))
        if arr == spell:
            return 1
    return 2

print(solution(spell, dic))
