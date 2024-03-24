from sys import stdin
from itertools import combinations

t = int(input())

def gcd(a, b):
    while(b != 0):
        temp = a % b
        a = b
        b = temp

    return a

for _ in range(t):
    num = list(map(int, stdin.readline().split()))
    arr = num[1:]
    sum = 0
    for a, b in combinations(arr, 2):
        sum += gcd(a, b)

    print(sum)
