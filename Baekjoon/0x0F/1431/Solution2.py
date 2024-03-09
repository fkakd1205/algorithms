from sys import stdin

N = int(input())
arr = [stdin.readline().rstrip() for _ in range(N)]

def digit_sum(num):
    sum = 0
    for n in num:
        if(n.isdigit()):
            sum += int(n)
    return sum

arr.sort(key = lambda x : (len(x), digit_sum(x), x))

print(*arr, sep="\n")
