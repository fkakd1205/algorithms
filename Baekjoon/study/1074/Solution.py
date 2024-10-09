N, r, c = map(int, input().split())

answer = 0

def search_position(x, y, size):
    global answer
    if size == 1: return

    new_size = size // 2

    if 0 <= x < new_size and 0 <= y < new_size:
        search_position(x, y, new_size)
    elif 0 <= x < new_size and new_size <= y < size:
        answer += (new_size * new_size)
        y -= new_size
        search_position(x, y, new_size)
    elif new_size <= x < size and 0 <= y < new_size:
        answer += (new_size * new_size) * 2
        x -= new_size
        search_position(x, y, new_size)
    else:
        answer += (new_size * new_size) * 3
        x -= new_size
        y -= new_size
        search_position(x, y, new_size)

search_position(r, c, 2 ** N)
print(answer)
