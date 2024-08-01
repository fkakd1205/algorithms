N = int(input())

num = [0] + ([1] * 9)
new_num = [0] * 10

for _ in range(N-1):
    for i in range(10):
        if i == 0:
            new_num[i] = num[i+1]
        elif i == 9:
            new_num[i] = num[i-1]
        else:
            new_num[i] = num[i-1] + num[i+1]
        
    for i in range(10):
        num[i] = new_num[i]

print(sum(num) % 1_000_000_000)
