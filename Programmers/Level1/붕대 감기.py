def solution(bandage, health, attacks):
    max_health = health
    attack = {i[0]:i[1] for i in attacks}
    last_attack_time = attacks[-1][0]
    bandage_count = 1
    
    for time in range(1, last_attack_time + 1):
        if time in attack:
            health -= attack[time]
            bandage_count = 1
            
            if health <= 0:
                return -1
            
        else:
            health = min(max_health, health + bandage[1])
            if bandage_count == bandage[0]:
                health = min(max_health, health + bandage[2])
                bandage_count = 1
            else:
                bandage_count += 1
    
    return health