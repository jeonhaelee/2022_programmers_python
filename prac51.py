# 실패율
# 스테이지 개수 : N
# stages 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.

def solution(N, stages):
    answer = []
    sub = []
    
    loss =[]
    remain = len(stages)
    
    for i in range(N):
        loss.append(0)
    
    
    for i in range(1, N+1):
        for p in range(len(stages)):
            if i == 1:
                if stages[p] <= i:
                    loss[i-1] += 1
            else:
                if stages[p] == i:
                    loss[i-1] += 1

    print(f'loss : {loss}')
    
    for i in range(N):
        print(f'{loss[i]}/{remain}')
        ratio = (loss[i]/remain)
        print(f'{i+1}번째 ratio : {ratio}')
        remain -= loss[i]
        sub.append([ratio, i+1])
    
    print(f'정렬 전 sub : {sub}')
    sub.sort(key= lambda x : (-x[0], x[1])) 
    print(f'정렬 후 sub : {sub}')
    
    for i in range(N):
        answer.append(sub[i][1])
        
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))  # [3,4,2,1,5]

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))  # [4,1,2,3]

