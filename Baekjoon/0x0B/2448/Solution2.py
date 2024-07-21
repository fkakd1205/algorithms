N = int(input())
init_pattern = ['  *  ', ' * * ', '*****']

def pattern(k):
    result = []
    if k == 3:
        return init_pattern
    
    ex_pattern = pattern(k // 2)
    for p in ex_pattern:
        result.append(' ' * (k//2) + p + ' ' * (k//2))
    for p in ex_pattern:
        result.append(p + ' ' + p)
    return result

answer = pattern(N)
print(*answer, sep='\n')
