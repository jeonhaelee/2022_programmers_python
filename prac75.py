# 두 큐 합 같게 만들기


# 내 풀이
from collections import deque

def solution(queue1, queue2):
    s = sum(queue1) + sum(queue2)
    
    if s % 2 != 0:
        return -1
    
    std = sum(queue1)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    count = 0
    while len(queue1) != 0 and len(queue2) != 0:
        if std > int(s/2):
            tmp = queue1.popleft()
            std -= tmp
            count += 1
        elif std < int(s/2):
            tmp = queue2.popleft()
            std += tmp
            queue1.append(tmp)
            count += 1
        else:
            return count
    
    return -1

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2)) # 2

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2)) # 7

queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2)) # -1


# 다른 사람 풀이 1
from collections import deque

def solution(queue1, queue2):
    answer = 0
    total = (sum(queue1) + sum(queue2))

    if total % 2 != 0:
        return -1

    total //= 2

    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)

    while answer <= 600000: # 두개의 큐 최대 길이만큼 탐색
        if q1_sum == q2_sum:
            return answer
        elif q1_sum < q2_sum:
            q2_front = q2.popleft()
            q2_sum -= q2_front
            q1_sum += q2_front
            q1.append(q2_front)
        else:
            q1_front = q1.popleft()
            q1_sum -= q1_front
            q2_sum += q1_front
            q2.append(q1_front)

        answer += 1

    return -1