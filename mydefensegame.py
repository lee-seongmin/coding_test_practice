def solution(n, k, enemy):
    ori = enemy
    cnt = 0
    enemy.sort()
    muj = enemy[:len(enemy)-k]

    for m in muj:
        ori.remove(m)

    for i in range(len(ori)):
        n -= ori[i]
        if n > 0:
            cnt+=1
        else:
            break
        
    return cnt+k