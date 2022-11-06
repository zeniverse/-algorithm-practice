import sys
input = sys.stdin.readline

k, l = map(int, input().split())
dic = dict()

for i in range(l):
    student = input().rstrip()
    dic[student] = i

dic = sorted(dic.items(), key=lambda x:x[1])

if k > len(dic):
    k = len(dic)

for i in range(k):
    print(dic[i][0])