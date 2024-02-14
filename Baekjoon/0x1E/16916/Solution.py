S = input()
P = input()
f = [0] * (len(P)+1)

# KMP 알고리즘 - 접두사, 접미사 비교를 통해 확인할 문자열을 건너뛸 수 있도록 한다
# 1. P에서 패턴을 찾아 f세팅
def failure():
    j = 0
    for i in range(1, len(P)):
        while (j > 0 and P[i] != P[j]): j = f[j-1]
        if P[i] == P[j]:
            j += 1
            f[i] = j

failure()

# 2. S에서 f를 이용해 P를 찾는다
j = 0
included = False
for i in range(len(S)):
    while (j > 0 and S[i] != P[j]): j = f[j-1]
    if S[i] == P[j]: j += 1
    if j == len(P):
        included= True
        break

if included:
    print(1)
else:
    print(0)
