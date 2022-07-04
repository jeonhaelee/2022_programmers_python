# 구명보트

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    print(people)
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit)) # 3