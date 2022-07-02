numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

locations = {
    1:(0, 0), 2:(0, 1), 3:(0, 2),
    4:(1, 0), 5:(1, 1), 6:(1, 2),
    7:(2, 0), 8: (2, 1), 9:(2, 2),
    '*':(3, 0), 0:(3, 1), '#':(3, 2)
}


l_num = [1,4,7]
r_num = [3,6,9]

left_location = '*'
right_location = '#'

res = ""

for i in numbers:
    if i in l_num:
        res += 'L'
        left_location = i
    elif i in r_num:
        res += 'R'
        right_location = i
    else:
        current_pos = locations[i]
        left_pos = locations[left_location]
        right_pos = locations[right_location]
        l_distance = abs(current_pos[0] - left_pos[0]) + abs(current_pos[1] - left_pos[1])
        r_distance = abs(current_pos[0] - right_pos[0]) + abs(current_pos[1] - right_pos[1])

        if l_distance < r_distance:
            res += 'L'
            left_location = i
        elif r_distance < l_distance:
            res += 'R'
            right_location = i
        else:
            if hand[:1] == 'r':
                res += 'R'
                right_location = i
            else:
                res += 'L'
                left_location = i

print(res)