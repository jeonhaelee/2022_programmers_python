# 캐시
# cache hit : 1, cache miss : 5

# 내 풀이
def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    pocket = []
    
    for city in cities:
        if city.lower() in pocket:
            del pocket[pocket.index(city.lower())]
            pocket.append(city.lower())
            answer += 1
        else:
            if len(pocket) < cacheSize:
                pocket.append(city.lower())
            else:
                del pocket[0]
                pocket.append(city.lower())
            answer += 5
            
    return answer

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities)) # 16

# 다른 사람 풀이 1
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

# 다른 사람 풀이 2
def solution(cacheSize, cities):
    answer = 0
    cache = []
    old = 0
    for city in cities:
        if city.lower() in cache:
            cache.remove(city.lower())
            cache.append(city.lower())
            answer += cache_hit
        else:
            answer += cache_miss
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city.lower())
    return answer