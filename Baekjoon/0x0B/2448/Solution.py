N = int(input())
stars = [[' '] * N * 2 for _ in range(N)]

# n=6은 n=3의 star 3개로 만든다. n=12는 n=6의 star 3개로 만든다. ...
def recur(x, y, size):
    if size == 3:
        # 첫번째 줄
        stars[x][y] = '*'
        # 두번째 줄
        stars[x+1][y-1] = '*'
        stars[x+1][y+1] = '*'
        # 세번째 줄
        for k in range(-2, 3):
            stars[x+2][y+k] = '*'
    else:
        size //= 2
        recur(x, y, size)   # 가운데 위 star
        recur(x + size, y - size, size)     # 왼쪽 아래 star
        recur(x + size, y + size, size)     # 오른쪽 아래 star

recur(0, N-1, N)

for star in stars:
    print("".join(star))
