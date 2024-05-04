from heapq import heappush, heappop

MX = 2

def solution(genres, plays):
    answer = []
    store = {}
    genre_cnt = {}
    
    # 해시 + 최대힙
    for i in range(len(genres)):
        g = genres[i]
        p = int(plays[i])
        
        if genres[i] in store:
            heappush(store[g], (-p, i))
            genre_cnt[g] += p
        else:
            store[g] = [(-p, i)]
            genre_cnt[g] = p

    # genre_cnt = { A : 1000, ...}에서 key는 장르, value는 장르 스트리밍 횟수 합
    # value 내림차순 정렬
    sorted_genre = sorted(genre_cnt.items(), key= lambda x : -x[1])
    for g, s in sorted_genre:
        cnt = 0
        while (store[g] and cnt < MX):
            c, num = heappop(store[g])
            cnt += 1
            answer.append(num)

    return answer

arr1 = input().split()
arr2 = input().split()
print(solution(arr1, arr2))
