phone_book = ["119", "97674223", "1195524421"]


def solution(phone_book):
    res = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                res = False
                break
    return res

print(solution(phone_book))



