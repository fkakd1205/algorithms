from sys import stdin

N = int(input())
arr = [int(stdin.readline()) for _ in range(N)]

arr.sort()

print('\n'.join(map(str, arr)))
