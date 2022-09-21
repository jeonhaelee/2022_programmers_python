# 땅따먹기
# product를 이용해 모든 경우의 수를 고려해보자.
# 시간 초과 다시


from itertools import product

def solution(land):
    answer = []

    lands = []
    for l in land:
        sub_lands = []
        for i, v in enumerate(l):
            sub_lands.append((i, v))
        lands.append(sub_lands)
            
            
    lands = list(product(*lands))

    for l in lands:
        result = l[0][1]
        for i in range(1, len(l)):
            if l[i-1][0] == l[i][0]:
                result = 0
                break
            result += l[i][1]
        answer.append(result)
        
    return max(answer)
    


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land)) # 16