from sys import stdin

N, K = map(int, input().split())
arr = list(map(int, stdin.readline().split()))
arr2 = [[] for _ in range(101)]
plug = [0] * N

cnt = 0

# [전기용품 번호].append(순서)
for i in range(K):
    arr2[arr[i]].append(i+1)

for i in range(K):
    if arr[i] not in plug:
        # plug가 비어있는 경우
        if 0 in plug:
            for idx in range(len(plug)):
                if plug[idx] == 0:
                    plug[idx] = arr[i]
                    break
        else:
            # plug가 꽉차있는 경우
            mx_idx = -1
            mx = -1
            for j in range(len(plug)):
                # 더이상 사용할 전기용품이 아니라면 바로 선택
                if not arr2[plug[j]]:
                    mx_idx = j
                    break
                elif mx < arr2[plug[j]][0]:     # 조만간 사용하지 않을 전기용품 선택
                    mx = arr2[plug[j]][0]
                    mx_idx = j
            plug[mx_idx] = arr[i]
            cnt += 1

    arr2[arr[i]].remove(arr2[arr[i]][0])

print(cnt)
