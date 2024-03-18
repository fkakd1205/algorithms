S = list(map(int, input().rstrip()))

# 000110 => 010으로 봐도 된다
# 0 => 1
# 01 => 1
# 010 => 1
# 0101 => 2
# 01010 => 2
# 010101 => 3
cnt = 1
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        cnt += 1

print(cnt // 2)
