
numbers = [2,7]

def solution(numbers):
    res = []

    for num in numbers:
        num_list = list('0' + bin(num)[2:])
        idx = ''.join(num_list).rfind('0')

        num_list[idx] = '1'

        if num % 2 == 1:
            num_list[idx + 1] = '0'

        res.append(int(''.join(num_list), 2))

    return res

print(solution(numbers))