N = int(input())

isused1 = [False] * N
isused2 = [False] * (N*2)
isused3 = [False] * (N*2)
count = 0

def queen(x):
    global count

    if x == N:
        count += 1
        return
    
    for y in range(N):
        if (isused1[y] or isused2[x+y] or isused3[x-y+(N-1)]):
            continue
        isused1[y] = True
        isused2[x+y] = True
        isused3[x-y+(N-1)] = True
        queen(x+1)
        isused1[y] = False
        isused2[x+y] = False
        isused3[x-y+(N-1)] = False

queen(0)
print(count)