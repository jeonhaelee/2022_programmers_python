# 구명보트


def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    
    l_idx = 0
    r_idx = len(people)-1
    
    while r_idx - l_idx >= 0:
        if r_idx == l_idx :
            answer += 1
            break
        
        if people[l_idx] + people[r_idx] > limit:
            answer += 1
            l_idx += 1
        else:
            answer += 1
            l_idx += 1
            r_idx -= 1
            
    return answer


# people = [70, 50, 80, 50]
# limit = 100
# print(solution(people, limit)) # 3

people = [70, 80, 50]
limit = 100
print(solution(people, limit)) # 3