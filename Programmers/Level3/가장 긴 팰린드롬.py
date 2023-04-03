def isPalindrome(x):
    if x == x[::-1]:
        return True

def solution(s):
    res = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]):
                if res < len(s[i:j]):
                    res = len(s[i:j])
    return res

s = "abcdcba"
print(solution(s))