
n = 15

def solution(n):
    return len([i for i in range(1, n + 1, 2) if n % i == 0])

print(solution(n))

# n 이하인 숫자 a부터 k개의 연속된 숫자의 합이 n이라면,
# k(2a + k -1)/2 = n 공식이 성립한다
# 따라서 a = n/k + (1-k)/2 가 되는데, a가 자연수라는 조건이 성립하기 위해서는
# k는 n의 약수여야하고, 1-k는 짝수여야 하므로 k는 홀수여야한다.