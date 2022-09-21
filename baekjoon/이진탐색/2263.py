
## 메모리 초과
## python에서 slice는 list를 만들어내기 때문에 계속 list를 만들어내서 메모리 초과됨
## 따라서 2263(2) 에서는 inorder와 postorder의 시작과 끝의 index 번호를 저장해서 문제를 해결함.

import sys
input = sys.stdin.readline

def toPreorder(inorder, postorder):

    if len(inorder) == 0:
        return
    elif len(inorder) == 1:
        print(inorder[0], end = ' ')
        return

    root_idx = inorder.index(postorder[-1])

    print(postorder[-1], end =' ')

    left_in = inorder[:root_idx]
    left_post = postorder[:len(left_in)]
    toPreorder(left_in, left_post)

    right_in = inorder[root_idx + 1:]
    right_post = postorder[len(left_in):len(postorder) - 1]
    toPreorder(right_in, right_post)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

toPreorder(inorder, postorder)