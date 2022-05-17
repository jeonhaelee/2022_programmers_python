def is_dif(sub_d):
    sub_d.sort()
    for i in range(len(sub_d)-1):
        if sub_d[i] == sub_d[i+1]:
            return False
    return True

def solution(relation):
    answer = 0
    d = []
    for i in range(len(relation[0])):
        sub_d = []
        for row in relation:
            sub_d.append(row[i])
        if is_dif(sub_d) == True:
            answer += 1
        d.append(sub_d)
        
    print(d)
    
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],
            ["300","tube","computer","3"],["400","con","computer","4"],
            ["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))