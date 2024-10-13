N = int(input())
arr = list(map(int, input().split()))
sum = [0] * N
sum[0] = arr[0]

for i in range(1, N):
    sum[i] += arr[i] + sum[i-1]

def right_bucket():
    honey = 0
    for right_bee in range(1, N-1):
        honey = max(honey, sum[N-1] - sum[0] - arr[right_bee] + sum[N-1] - sum[right_bee])
    return honey

def left_bucket():
    honey = 0
    for left_bee in range(1, N-1):
        honey = max(honey, sum[N-2] - arr[left_bee] + sum[left_bee-1])
    return honey

def middle_bucket():
    honey = 0
    for bucket in range(1, N-1):
        honey = max(honey, sum[bucket] - arr[0] + sum[N-2] - sum[bucket-1])
    return honey

print(max(right_bucket(), left_bucket(), middle_bucket()))
