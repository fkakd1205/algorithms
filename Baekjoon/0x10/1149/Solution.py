from sys import stdin

N = int(input())
price = [0] * N

for i in range(N):
    price[i] = list(map(int, stdin.readline().split()))

# i번째 까지의 총 비용은 i-1번째 까지의 비용의 최솟값과 현재 비용을 더해서 구한다
for i in range(1, N):
    price[i][0] = min(price[i-1][1], price[i-1][2]) + price[i][0]
    price[i][1] = min(price[i-1][0], price[i-1][2]) + price[i][1]
    price[i][2] = min(price[i-1][0], price[i-1][1]) + price[i][2]

print(min(price[N-1][0], price[N-1][1], price[N-1][2]))
