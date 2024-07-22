from sys import stdin

N = int(input())
card = list(map(int, stdin.readline().split()))

M = int(input())
nums = list(map(int, stdin.readline().split()))
result = []

card.sort()

def binary_search(target):
    left = 0
    right = N-1
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if card[mid] == target:
            answer = 1
            break
        if card[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

for n in nums:
    result.append(binary_search(n))

print(*result)
