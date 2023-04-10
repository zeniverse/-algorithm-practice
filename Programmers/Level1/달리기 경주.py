

def solution(players, callings):
    players_dic = {n : i for i, n in enumerate(players)}
    index_dic = {i : n for i, n in enumerate(players)}

    for call in callings:
        cur_idx = players_dic[call]
        front_idx = cur_idx - 1

        cur_player = call
        front_player = index_dic[front_idx]

        players_dic[cur_player], players_dic[front_player] = front_idx, cur_idx
        index_dic[cur_idx], index_dic[front_idx] = front_player, cur_player


    return list(index_dic.values())

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))

