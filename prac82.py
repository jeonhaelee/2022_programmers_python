# 땅따먹기
# product를 이용해 모든 경우의 수를 고려해보자.

from itertools import product

def solution(land):
    answer = []

    lands = []
    for l in land:
        sub_lands = []
        for i, v in enumerate(l):
            sub_lands.append((i, v))
        lands.append(sub_lands)
            
            
    print(list(product(*lands)))

    # for l in lands:
    #     result = 0
    #     for i in range(len(l)-1):
    #         if l[i] == l[i+1]:
    #             continue
    #         result += l[i]
    #     answer.append(result)
        
    return max(answer)


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land)) # 16