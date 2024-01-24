from sys import stdin

N = int(input())
user = [list(map(str, stdin.readline().split())) for _ in range(N)]

# stable sort
# 나이를 int로 변환 후 정렬
user.sort(key= lambda x : int(x[0]))

for age, name in user:
    print(age, name, sep=" ")
