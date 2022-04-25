import hashlib

s = input()
encode_data = s.encode()
res = hashlib.sha256(encode_data).hexdigest()
print(res)