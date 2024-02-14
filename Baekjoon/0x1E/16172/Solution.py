S = input()
K = input()
f = [0] * (len(K)+1)

# V1. 시간초과
# S2 = ''
# for chr in S:
#     if(chr.isalpha()): S2 += chr

# # 1. K의 패턴 설정
# j = 0
# for i in range(1, len(K)):
#     while (j > 0 and K[i] != K[j]):  j = f[j-1]
#     if K[i] == K[j]:
#         j += 1
#         f[i] = j

# # 2. K의 패턴을 이용해 S에서 키워드 포함여부 확인
# j = 0
# included = False
# for i in range(len(S2)):
#     while (j > 0 and S2[i] != K[j]): j = f[j-1]
#     if S2[i] == K[j]: j += 1
#     if j == len(K):
#         included = True
#         break

# V2.
# 1. K의 패턴 설정
j = 0
for i in range(1, len(K)):
    while (j > 0 and K[i] != K[j]):  j = f[j-1]
    if K[i] == K[j]:
        j += 1
        f[i] = j

# 2. K의 패턴을 이용해 S에서 키워드 포함여부 확인
j = 0
included = False
for i in range(len(S)):
    if S[i].isdigit(): continue
    while (j > 0 and S[i] != K[j]): j = f[j-1]
    if S[i] == K[j]: j += 1
    if j == len(K):
        included = True
        break

if (included):
    print(1)
else:
    print(0)
