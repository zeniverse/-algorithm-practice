
new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    
    res = ''

    #1
    new_id = new_id.lower()

    #2
    for i in new_id:
        if i.isalpha() or i.isdecimal() or i in ['-', '_', '.']:
            res += i

    #3
    while '..' in res:
        res = res.replace('..', '.')

    #4
    if res[0] == '.':
        if len(res) > 1:
            res = res[1:]
    if res[-1] == '.':
        res = res[:-1]
    #5
    if res == '':
        res = 'a'

    #6
    if len(res) > 15:
        res = res[:15]
        if res[-1] == '.':
            res = res[:-1]

    #7
    while len(res) < 3:
        res += res[-1]
        
    return res