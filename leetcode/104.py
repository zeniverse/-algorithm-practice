from collections import deque

def  maxDepth(self, root):
    res = 0

    if root == None:
        return res

    queue = deque()
    queue.append((root, 1))

    while queue:
        cur_node, cur_depth = queue.popleft()
        res = max(res, cur_depth)
        if cur_node.left:
            queue.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            queue.append((cur_node.right, cur_depth + 1))

    return res
