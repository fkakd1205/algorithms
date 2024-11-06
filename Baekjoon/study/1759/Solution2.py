N, C = map(int, input().split())
arr = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']

arr.sort()
result = [''] * N

def recur(st, cur):
    if cur == N:
        vowel_cnt = 0
        cons_cnt = 0
        for alpha in result:
            if alpha in vowels:
                vowel_cnt += 1
            else:
                cons_cnt += 1
        
        if vowel_cnt >= 1 and cons_cnt >= 2:
            print(*result, sep="")
        return
    
    for i in range(st, C):
        result[cur] = arr[i]
        recur(i+1, cur+1)

recur(0, 0)
