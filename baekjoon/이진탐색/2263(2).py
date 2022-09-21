
import sys
sys.setrecursionlimit(10**9) 
input = sys.stdin.readline

def toPreorder(in_start, in_end, post_start, post_end):
    if(in_start > in_end) or (post_start > post_end):
        return

    parents = postorder[post_end]
    print(parents, end = ' ')

    left = posiion[parents] - in_start
    right = in_end - posiion[parents]

    toPreorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    toPreorder(in_end - right + 1, in_end, post_end - right, post_end - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

posiion = [0] * (n + 1)
for i in range(n):
    posiion[inorder[i]] = i

toPreorder(0, n - 1, 0, n - 1)