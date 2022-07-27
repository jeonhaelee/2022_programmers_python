# 캐시
# cache hit : 1, cache miss : 5


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