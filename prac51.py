# 실패율
# 스테이지 개수 : N
# stages 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.

# 내 풀이

def solution(N, stages):
    answer = []
    sub = []
    
    loss =[]
    remain = len(stages)
    
    for i in range(N):
        loss.append(0)
    
    i = 1
    while True:
        for p in range(len(stages)):
            if i == 1:
                if stages[p] <= i:
                    loss[i-1] += 1
            else:
                if stages[p] == i:
                    loss[i-1] += 1
        i += 1
        if i == N + 1:
            break
    
    for i in range(N):
        if remain == 0:
            ratio = 0
        else:
            ratio = (loss[i]/remain)
        remain -= loss[i]
        sub.append([ratio, i+1])
    
    sub.sort(key= lambda x : (-x[0], x[1])) 
    
    for i in range(N):
        answer.append(sub[i][1])
        
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))  # [3,4,2,1,5]

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))  # [4,1,2,3]

N = 5
stages = [3, 3, 3, 3]
print(solution(N, stages))  


# 다른 사람 풀이1

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

# 다른 사람 풀이2

def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer