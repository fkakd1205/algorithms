# V1.
# def get_next_pos(cur, d):
#     x = cur[0]
#     y = cur[1]
#     if d == 'L':
#         x -= 1
#     elif d == 'R':
#         x += 1
#     elif d == 'U':
#         y += 1
#     else:
#         y -= 1

#     return x, y

# def solution(dirs):
#     answer = 0
#     store = set()
#     cur = (0, 0)
#     for d in dirs:
#         x, y = get_next_pos(cur, d)
#         if -5 <= x <= 5 and -5 <= y <= 5:
#             if (cur[0], cur[1], x, y) not in store:
#                 answer += 1
#                 store.add((cur[0], cur[1], x, y))
#                 store.add((x, y, cur[0], cur[1]))
#             cur = (x, y)
#     return answer


# V2.
def solution(dirs):
    answer = 0
    store = set()
    x, y = 0, 0
    dir = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for d in dirs:
        cx, cy = x + dir[d][0], y + dir[d][1]
        if -5 <= cx <= 5 and -5 <= cy <= 5:
            store.add((x, y, cx, cy))
            store.add((cx, cy, x, y))
            x, y = cx, cy
    answer = len(store) // 2
    return answer

dirs = input()
print(solution(dirs))
