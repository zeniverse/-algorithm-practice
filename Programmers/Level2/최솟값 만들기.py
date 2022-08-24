
A = [1, 4, 2]
B = [5, 4, 4]

res = []

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(len(A)):
    res.append(A[i] * B[i])

print(sum(res))
