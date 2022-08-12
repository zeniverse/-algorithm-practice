from itertools import permutations

numbers = [3, 30, 34, 5, 9]
numbers = list(map(str, numbers))

# numbers의 원소가 1000이하이므로 3자리수를 만들어서 값을 비교해주기 위해 *3을 해준다
# (numers를 정렬 했을 때, 30보다 3이 더 먼저 나오기 위함)
numbers = sorted(numbers, key=lambda x:x*3, reverse=True)

# numbers = [0, 0, 0, 0] 일 때, 결과값이 0000이 아닌 0이 나올 수 있도록
# int로 한번 변경한 후에 str로 다시 변경해준다.
print(str(int(''.join(numbers))))





