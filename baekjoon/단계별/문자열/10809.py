alphabet = [chr(i) for i in range(97,123)]

s = input()

for i in alphabet:
    print(s.find(i), end=" ")