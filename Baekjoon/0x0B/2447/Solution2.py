N = int(input())

def pattern(k):
    result = []
    if k == 1:
        return ['*']
    
    ex_pattern = pattern(k // 3)
    for p in ex_pattern:
        result.append(p * 3)
    for p in ex_pattern:
        result.append(p + ' ' * (k // 3) + p)
    for p in ex_pattern:
        result.append(p * 3)

    return result

answer = pattern(N)
print(*answer, sep='\n')
