
spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]

def solution(spell, dic):
    spell = set(spell)

    for word in dic:
        if not spell - set(word):
            return 1
    return 2

print(solution(spell, dic))
