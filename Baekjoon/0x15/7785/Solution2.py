from sys import stdin

n = int(input())
record = dict()

for i in range(n):
    name, log = map(str, stdin.readline().split())
    
    if log == 'enter':
        record[name] = 1
    else:
        del record[name]

result = sorted(record.keys(), reverse=True)
print(*result, sep="\n")

