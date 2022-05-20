

new_id = "abcdefghijklmn.p"

# 1단계
new_id = new_id.lower()

# 2단계
for i in range(len(new_id)):
    if not new_id[i].isalnum():
        if new_id[i] not in ["-", '_', '.']:
            new_id = new_id.replace(new_id[i], ' ')

new_id = new_id.replace(' ', '')

# 3단계
while '..' in new_id:
    new_id = new_id.replace('..', '.')

# 4단계
if new_id:
    if new_id[0] == '.':
        new_id = new_id[1:]

if new_id:
    if new_id[-1] == '.':
        new_id = new_id[:-1]

# 5단계
if len(new_id) == 0:
    new_id = 'a'

# 6단계
if len(new_id) >= 16:
    new_id = new_id[:15]

if new_id[-1] == '.':
    new_id = new_id[:-1]

# 7단계
if len(new_id) <= 2:
    while len(new_id) < 3:
        new_id += new_id[-1]


print(new_id)
