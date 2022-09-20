# 땅따먹기

def solution(land):
    answer = []
    
    while len(answer) < 4:
        
        used_idx = [len(answer)]
        result = land[0][len(answer)]
        
        for row in land[1:]:
            li = row[:]
            
            if result == 0:
                result += max(li)
                used_idx.append(li.index(max(li)))
                continue
            
            if li.index(max(li)) == used_idx[-1]:
                del li[li.index(max(li))]
                result += max(li)
                li.index(max(li))
            else:
                result += max(li)
                li.index(max(li))
            
        answer.append(result)

    return max(answer)


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land)) # 16