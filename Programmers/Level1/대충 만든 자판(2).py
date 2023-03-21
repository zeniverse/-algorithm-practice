

def solution(keymap, targets):
    res = []
    dic = {}

    for k in keymap:
        for i , ch in enumerate(k):
            dic[ch] = min(i + 1, dic[ch]) if ch in dic else i + 1

    for t in targets:
        ans = 0
        for word in t:
            if word not in dic:
                ans = -1
                break
            ans += dic[word]
        res.append(ans)
    
    return res

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]

print(solution(keymap, targets))
