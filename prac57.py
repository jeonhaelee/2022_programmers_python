# 구명보트

# 내 풀이

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

# 다른 사람 풀이 1

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

# 다른 사람 풀이 2
# deque(데크)란? 양방향 큐라고 생각하면 된다.

from collections import deque

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        result += 1
    return result