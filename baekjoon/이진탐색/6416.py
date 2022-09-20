
from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(list)
nodes = set()
root = []
arr = []
caseCount = 0
edgeCount = 0


def find_root(trees):
    val = []
    
    for v in trees.values():
        val.extend(v)

    for k in trees.keys():
        if k not in val:
            root.append(k)

    if root:
        if len(root) >= 2:
            return False
    else:
        return False

    return True

def dfs(root, visited):

    for e in trees[root]:
        if not visited[e]:
            visited[e] = True
            dfs(e, visited)


while True:
    input_ = input().rstrip()

    if input_ == '-1 -1':
        break
    if input_ == '':
        continue

    arr += list(map(int, input_.split()))

    for i in range(0, len(arr), 2):
        if arr[i] == 0 and arr[i + 1] == 0:
            edgeCount = (len(arr) - 2) // 2

            caseCount += 1
            isTree = True

            if edgeCount == 0:
                isTree = True
            else:
                if not find_root(trees):
                    isTree = False

                if edgeCount + 1 != len(nodes):
                    isTree = False

                if isTree:
                    visited = [False] * (max(nodes) + 1)
                    visited[root[0]] = True
                    dfs(root[0], visited)

                    for i in nodes:
                        if not visited[i]:
                            isTree = False

            if isTree:
                print('Case', caseCount, 'is a tree.')
            else:
                print('Case', caseCount, 'is not a tree.')

            trees = defaultdict(list)
            nodes = set()
            root = []
            arr = []
            edgeCount = 0


            break
        
        trees[arr[i]].append(arr[i + 1])
        nodes.add(arr[i])
        nodes.add(arr[i + 1])
        
    
        
    



