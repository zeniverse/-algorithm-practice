
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

myString = "abcdevwxyz"
print(solution(myString))