
s = "abcabcdede"

def compress(s, step):
    compressed = ""
    prev = s[:step]
    count = 1

    for i in range(step, len(s), step):
        cur = s[i: i + step]

        if cur == prev:
            count += 1
        else:
            compressed += (str(count) + prev) if count > 1 else prev
            prev = cur
            count = 1

    compressed += (str(count) + prev) if count > 1 else prev
    return len(compressed)

def solution(s):
    answer = len(s)
    # 압축 최대 길이는 문자열의 절반을 넘어가지 않는다!
    # 절반의 길이를 넘어가면 압축이 아니기 때문
    for step in range(1, len(s)//2 + 1):
        compressed_length = compress(s, step)
        answer = min(answer, compressed_length)
    return answer

print(solution(s))