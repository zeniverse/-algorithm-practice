n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

for i in range(1, len(words)):
    if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
        print([(i % n)+1, (i // n)+1])
        break
else:
    print([0, 0])

