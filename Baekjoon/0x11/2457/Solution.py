from sys import stdin
from collections import deque

N = int(input())
arr = []

for _ in range(N):
    s_m, s_d, e_m, e_d = map(int, stdin.readline().split())
    arr.append([s_m * 100 + s_d, e_m * 100 + e_d])      # month에는 100을 곱해준다

# 피는 날짜, 지는 날짜 순으로 오름차순 정렬
arr.sort()
q = deque(arr)
end_date = 301
count = 0

while (True):
    # 꽃이 지는 날짜가 남아있는 꽃의 피는 날짜보다 빠른 경우. 지는 날짜가 11/30을 넘어간 경우.
    if (not q or q[0][0] > end_date or end_date >= 1201):
        break

    temp_end_date = 0
    while q:
        # 꽃이 피는 날짜가 end_date보다 작으면서 end_date와 차이가 적은 것을 고른다
        if (q[0][0] <= end_date):
            if temp_end_date <= q[0][1]:
                temp_end_date = q[0][1]
            q.popleft()
        else:
            break

    end_date = temp_end_date
    count += 1

# end_date 가 1130 이라면 1129까지만 꽃이 피는 것임
if end_date < 1201:
    print(0)
else:
    print(count)
