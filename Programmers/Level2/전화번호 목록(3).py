phone_book = ["119", "97674223", "1195524421"]


def solution(phone_book):
    phone_book = set(phone_book)

    for phone in phone_book:
        tmp = ""
        for num in phone:
            tmp += num
            if tmp == phone:
                continue
            if tmp in phone_book:
                return False
    return True

print(solution(phone_book))



