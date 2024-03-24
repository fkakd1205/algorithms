N = int(input())

a = 1
b = 1
diff = -1
cnt = 1
while(True):
    if a <= N <= b:
        print(cnt)
        break
    diff += 6
    cnt += 1
    a = b + 1
    b = a + diff    
