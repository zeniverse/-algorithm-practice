import math

n = int(input())
s = input()

count = s.count('C')

print(math.ceil((n - (n - count)) / (((n - count) + 1))))