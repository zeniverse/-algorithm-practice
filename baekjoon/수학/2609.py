arr = list(map(int, input().split()))

# 유클리드 호제법을 사용하려면 a > b 여야 하기 때문에 list로 받아 sort 해준다.
arr.sort()

# 유클리드 호제법
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

res1 = gcd(arr[-1], arr[0])

print(res1, (arr[-1] * arr[0]) // res1)