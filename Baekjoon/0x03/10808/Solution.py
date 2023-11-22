S = input()
arr = [0 for _ in range(26)]

for i in S:
    arr[ord(i) - 97] += 1

print(*arr)