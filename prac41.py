def solution(relation):
    answer = 0
    d = []
    for i in range(len(relation[0])):
        sub_d = []
        for row in relation:
            sub_d.append(row[i])
        d.append(sub_d)
        
    print(d)
    
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],
            ["300","tube","computer","3"],["400","con","computer","4"],
            ["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))