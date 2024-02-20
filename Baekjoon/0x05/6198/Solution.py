from sys import stdin

N = int(input())
building = []
stack = []
result = 0

for _ in range(N):
    t = int(stdin.readline().rstrip())
    building.append(t)

for b in reversed(building):
    count = 0
    if not stack:
        stack.append((b, count))
    else:
        # 자신의 빌딩(A)보다 작은 빌딩(B)이라면
        # B에서 볼 수 있는 옥상의 개수는 A에서도 볼 수 있으므로, B의 count로 A에서 볼 수 있는 옥상 개수를 알 수 있음
        # 그 후 B를 스택에서 제거. 이제 A보다 큰 빌딩(C)이 온다면 A의 count로 C에서 볼 수 있는 옥상 개수를 알 수 있음
        while(stack and stack[-1][0] < b):
            count += stack.pop()[1] + 1
        
        stack.append((b, count))
    
    if count > 0:
        result += count

print(result)
