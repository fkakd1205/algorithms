from sys import stdin

T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, stdin.readline().split()))
    stock.reverse()
    answer = 0

    mx_price = stock[0]
    for i in range(1, N):
        if stock[i] > mx_price:
            mx_price = stock[i]
        else:
            answer += mx_price - stock[i]

    print(answer)
