from sys import stdin

K, L = map(int, stdin.readline().split())
temp = dict()

for idx in range(L):
    number = stdin.readline().rstrip()
    temp[number] = idx

result = sorted(temp.items(), key = lambda x: x[1])

# 대기 리스트 학생 수 보다 수강신청 인원(K)이 더 큰 경우
if (K > len(result)):
    K = len(result)

for i in range(K):
    print(result[i][0])
