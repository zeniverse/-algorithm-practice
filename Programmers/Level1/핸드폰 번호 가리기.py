phone_number = "027778888"

res = ("*" * (len(phone_number) - 4)) + phone_number[-4:]
print(res)