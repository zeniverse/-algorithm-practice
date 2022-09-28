

from collections import defaultdict
from copy import deepcopy


res = 1
children = defaultdict(list)

def visited_sheep(info, candidates):
    tmp = deepcopy(candidates)
    count = 0

    for node in candidates:
        if info[node] == 0:
            count += 1
            tmp.remove(node)

            if children.__contains__(node):
                for child in children[node]:
                    tmp.add(child)

    if tmp != candidates:
        candidates.clear()

        for node in tmp:
            candidates.add(node)
        
        count += visited_sheep(info, candidates)

    return count




def dfs(info, candidates, sheep, wolf):
    global res
    sheep += visited_sheep(info, candidates)

    for next_node in candidates:
        if sheep - wolf > 1:
            tmp = deepcopy(candidates)
            tmp.remove(next_node)

            if children.__contains__(next_node):
                for child in children[next_node]:
                    tmp.add(child)

            dfs(info, tmp, sheep, wolf + 1)

    res = max(res, sheep)


def solution(info, edges):
    global res, children

    for parent, child in edges:
        children[parent].append(child)

    dfs(info, set(children[0]), 1, 0)


    return res

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))