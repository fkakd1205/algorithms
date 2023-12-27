N = int(input())

def hanoi(n, start, other, end):
    if n == 1 :
        print(start, end)
        return
    
    hanoi(n-1, start, end, other)
    print(start, end)
    hanoi(n-1, other, start, end)

sum = (2 ** N) - 1
print(sum)

hanoi(N, 1, 2, 3)
