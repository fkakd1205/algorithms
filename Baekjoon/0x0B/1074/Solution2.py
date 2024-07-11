N, r, c = map(int, input().split())
cnt = 0

def recur_paper(size, x, y):
    global cnt

    size //= 2
    if size == 0:
        return cnt

    if x < size and y >= size:      # 1사분면
        cnt += size * size
        y -= size
    elif x >= size and y < size:     # 3사분면
        cnt += size * size * 2
        x -= size
    elif x >= size and y >= size:     # 4사분면
        cnt += size * size * 3
        x -= size
        y -= size

    recur_paper(size, x, y)

recur_paper(2 ** N, r, c)
print(cnt)
