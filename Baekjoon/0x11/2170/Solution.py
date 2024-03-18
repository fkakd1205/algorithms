from sys import stdin

N = int(input())
pos = [list(map(int, stdin.readline().split())) for _ in range(N)]
pos.sort()
st = pos[0][0]
en = pos[0][1]
length = 0

for i in range(1, len(pos)):
    if (pos[i][0] <= en):
        en = max(en, pos[i][1])
    else:
        length += (en - st)
        st = pos[i][0]
        en = pos[i][1]

length += (en - st)
print(length)
