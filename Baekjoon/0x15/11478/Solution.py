S = input()
N = len(S)

store = dict()
en = 0
for i in range(N):
    temp = ''
    for j in range(i, N):
        temp += S[j]
        store[temp] = 1

print(len(store))
