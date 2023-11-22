a = input()
b = input()
arr = [0 for _ in range(26)]

for i in a:
    arr[ord(i) - 97] += 1

for i in b:
    arr[ord(i) - 97] -= 1

print(sum(map(abs, arr)))
