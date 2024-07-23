
numbers = [2,7]

def check(x):
    if x % 2 == 0:
        return x + 1
    
    x = '0' + bin(x)[2:]
    idx = x.rfind('0')
    x = x[:idx] + '10' + x[idx+2:]

    return int(x, 2)


def solution(numbers):
    return [check(num) for num in numbers]

print(solution(numbers))