def solution(cacheSize, cities):
    answer = 0
    cache = []
    for c in cities:
        city = c.lower()
        # cache miss
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            elif cache:
                cache.pop(0)
                cache.append(city)
            answer += 5
        # cache hit
        else:
            idx = cache.index(city)
            cache.pop(idx)
            cache.append(city)
            answer += 1
    return answer

cacheSize = int(input())
cities = input().split()
print(solution(cacheSize, cities))
