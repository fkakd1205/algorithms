from sys import stdin

VOWELS = ('a', 'e', 'i', 'o', 'u')
CONSONANT = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

L, C = map(int, input().split())
alphabet = list(map(str, stdin.readline().split()))
arr = [0] * L

alphabet.sort()

def func(cur):
    if cur == L:
        result = []
        # 모음, 자음 count
        vowel_cnt = 0
        consonant_cnt = 0
        for i in range(L):
            if alphabet[arr[i]] in VOWELS:
                vowel_cnt += 1
            elif alphabet[arr[i]] in CONSONANT:
                consonant_cnt += 1
            result.append(alphabet[arr[i]])
        # 모음 1개 이상, 자음 2개 이상인 경우에만 출력
        if(vowel_cnt > 0 and consonant_cnt > 1):
            print(*result, sep="")
        return
    
    start_idx = 0 if cur == 0 else arr[cur - 1] + 1
    for i in range(start_idx, C):
        arr[cur] = i
        func(cur + 1)

func(0)
