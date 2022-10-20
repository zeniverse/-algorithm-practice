n = 144

def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

print(solution(n))


# isinstance() 를 사용해서 어떤 타입인지 알 수 있다.
# isinstance(144, int) -> True or False

# float.is_integer() 를 사용해서 정수인지 판별 할 수 있다.
# float형에서만 사용할 수 있다.

