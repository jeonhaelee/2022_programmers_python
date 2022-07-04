# 구명보트

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    
    while len(people) > 1:
        if people[0] + people[-1] > limit:
            answer += 1
            del people[0]
            
    if len(people) == 1:
        answer += 1
        del people[0]
        
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit)) # 3