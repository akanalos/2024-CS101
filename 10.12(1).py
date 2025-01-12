    p=int(input())
    weapon=list(map(int,input().split()))
    weapon_remake = sorted(weapon, reverse=False)
    l = len(weapon_remake)
    ally, enemy = 0, 0
    adv = 0
    while True:
        if weapon_remake[ally] <= p:
            p -= weapon_remake[ally]
            ally += 1
            adv = max(ally - enemy, adv)
        else:
            if ally - enemy > 0:
                enemy += 1
                p += weapon_remake[-enemy]
            else:
                break
        if ally + enemy == l:
            break
    print(adv)