N, r, c = map(int, input().split())

def recur(size, x, y, num):
    if size == 1:
        print(num)
        return

    size = size // 2

    if 0 <= x < size and 0 <= y < size:
        recur(size, x, y, num)
    elif 0 <= x < size and size <= y < (size * 2):
        recur(size, x, y - size, (size**2) * 1 + num)
    elif size <= x < (size * 2) and 0 <= y < size:
        recur(size, x - size, y, (size**2) * 2 + num)
    else:
        recur(size, x - size, y - size, (size**2) * 3 + num)

recur(2**N, r, c, 0)
