
import sys
input = sys.stdin.readline

def toPostOrder(preOrder, inOrder):
    
    if len(preOrder) == 0:
        return
    elif len(preOrder) == 1:
        print(preOrder[0], end = ' ')
        return
    elif len(preOrder) == 2:
        print(preOrder[1], preOrder[0], end=' ')
        return

    root_idx = inOrder.index(preOrder[0])

    left_in = inOrder[:root_idx]
    left_pre = preOrder[1:len(left_in) + 1]
    toPostOrder(left_pre, left_in)

    right_in = inOrder[root_idx + 1:]
    right_pre = preOrder[1 + len(left_pre):]
    toPostOrder(right_pre, right_in)

    print(preOrder[0], end=' ')


for _ in range(int(input())):
    n = int(input())
    preOrder = list(map(int, input().split()))
    inOrder = list(map(int, input().split()))

    toPostOrder(preOrder, inOrder)
    print()