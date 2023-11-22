# v1
# arr = [int(input()) for _ in range(9)]

# arr.sort()
# sum = sum(arr)

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if(sum - arr[i] - arr[j] == 100):
#             for k in range(len(arr)):
#                 if (k != i and k != j):
#                     print(arr[k])

# v2
import itertools

arr = [int(input()) for _ in range(9)]
arr.sort()

for comb in itertools.combinations(arr, 7):
    if(sum(comb) == 100):
        for j in comb:
            print(j)
        break
