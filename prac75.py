# 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    answer = -2
    s = sum(queue1) + sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    count = 0
    while sum(queue1) != sum(queue2):
        if sum(queue1) > int(s/2):
            tmp = queue1.popleft()
            queue2.append(tmp)
            count += 1
        if sum(queue2) > int(s/2):
            tmp = queue2.popleft()
            queue1.append(tmp)
            count += 1
        if count > 300000:
            break
    
    if count <= 300000:
        answer = count
    else:
        answer = -1
    
    return answer

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2)) # 2

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2)) # 7

queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2)) # -1