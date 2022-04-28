import sys

n, m = map(int, sys.stdin.readline().split())
arr = dict()


for i in range(n):
    data = sys.stdin.readline().strip()
    arr[data] = i + 1

reverse_arr = dict(map(reversed, arr.items()))


for i in range(m):
    quiz = sys.stdin.readline().strip()

    if quiz.isalpha():
        print(arr[quiz])
    else:
        print(reverse_arr[int(quiz)])