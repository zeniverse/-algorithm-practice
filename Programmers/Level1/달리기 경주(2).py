

def solution(players, callings):
    dic = {player : i for i, player in enumerate(players)}
    
    for p in callings:
        idx = dic[p]
        dic[p] -= 1
        dic[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))

