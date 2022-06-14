# 실패율
# 스테이지 개수 : N
# stages 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.

def solution(N, stages):
    answer = []
    sub_answer = []
    
    sub = []
    for i in range(N):
        sub.append(0)
        
    for i in range(len(stages)):
        for j in range(stages[i]):
            sub[j-1] += 1
    
    print(sub)
    for i in range(N):
        sub_answer.append([(len(stages)-sub[i])/len(stages), i])
    
    sub_answer.sort(reverse=True)
    print(sub_answer)
    
    for n in sub_answer:
        answer.append(n[1] + 1)
        
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))  # [3,4,2,1,5]