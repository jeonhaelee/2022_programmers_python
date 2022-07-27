# 캐시
# cache hit : 1, cache miss : 5


def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    pocket = []
    
    for city in cities:
        if city in pocket:
            del pocket[pocket.index(city)]
            pocket.append(city)
            answer += 1
        else:
            if len(pocket) < 3:
                pocket.append(city)
            else:
                del pocket[0]
                pocket.append(city)
            answer += 5
            
    return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities)) # 50