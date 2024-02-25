N = int(input())

def make_pattern(k):
    result = []
    if k == 1:
        return ['*']

    # (k // 3)의 패턴이 k의 패턴에 사용
    pattern = make_pattern(k // 3)

    for i in pattern:
        result.append(i*3)
    for i in pattern:
        result.append(i + (' '*(k // 3)) + i)
    for i in pattern:
        result.append(i*3)
    return result

print(*make_pattern(N), sep="\n")
