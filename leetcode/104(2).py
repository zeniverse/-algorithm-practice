
def  maxDepth(self, root):
    if not root:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return 1 + max(left, right)
