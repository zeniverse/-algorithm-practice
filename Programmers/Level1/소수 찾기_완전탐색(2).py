from itertools import permutations

numbers = "011"

primeNum = set()

def isPrime(number):
    if number in (0, 1):
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def makeNumbers(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeNum.add(int(str1))
    
    for i in range(len(str2)):
        makeNumbers(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeNumbers("", numbers)

    res = len(primeNum)

    return res


print(solution(numbers))