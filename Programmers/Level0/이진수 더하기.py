
bin1 = "10"
bin2 = "11"

def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

print(solution(bin1, bin2))
