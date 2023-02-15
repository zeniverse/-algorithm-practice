

def solution(n, s):
    if n > s:
        return [-1]
    
    # 곱이 가장 큰 합을 만드려면,
    # 공평하게 모두 나눈 후에 나머지를 각각 1씩 더해주면 된다.
    # (n개의 자연수간의 차이가 적어야한다)
    # ex) n = 3, s = 8 일때, 8을 3으로 나누면 몫은 2 나머지도 2 가된다 
    # res = [2, 2, 2] 를 만들어주고 나머지 2를 각 하나씩 1을 더해
    # res = [2, 3, 3] 으로 만들어주면 된다.
    num, rest = divmod(s, n)
    res = [num] * n

    for i in range(rest):
        res[i] += 1

    res.sort()

    return res
    

n, s = 2, 9
print(solution(n, s))

