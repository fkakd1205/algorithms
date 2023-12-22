from sys import stdin

N = int(stdin.readline())
temp = dict()

for _ in range(N):
    key, value = list(stdin.readline().split())

    if value == "enter":
        temp[key] = value
    else:
        del temp[key]

result = sorted(temp.keys(), reverse=True)

print("\n".join(result))
