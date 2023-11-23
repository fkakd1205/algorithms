import sys

n = int(input())
stack = []
count = 1
result = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    
    while(count <= num):
        stack.append(count)
        count += 1
        result.append("+")

    if(stack[-1] == num):
        stack.pop()
        result.append("-")
    else:
        break

if(stack):
    print("NO")
else:
    print('\n'.join(result))
