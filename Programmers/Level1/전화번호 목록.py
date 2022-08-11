phone_book = ["119", "97674223", "1195524421"]

phone_book = sorted(phone_book)
print(phone_book)

for p1, p2 in zip(phone_book, phone_book[1:]):
    if p2.startswith(p1):
        print(False)
    


