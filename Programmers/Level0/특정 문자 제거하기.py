my_string = "BCBdbe"
letter = 'B'

def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer

print(solution(my_string, letter))