# 순위 검색
# 효율성 테스트 다시.

def solution(info, query):
    answer = []
    people = []
    
    for i in info:
        
        a, b, c, d, e = i.split(" ")
        person = a + b + c + d
        p_score = int(e)
        people.append([person, p_score])
        
    print(people)
    
    for q in query:
        
        q = q.replace('and ', '')
        q = q.replace('-', '')
        a, b, c, d, e = q.split(" ")
        qu = a + b + c + d
        score = int(e)
        print(f'qu : {qu}'), print(f'score : {score}')
        
        count = 0
        for p in people:
            if a in p[0] and b in p[0] and c in p[0] and d in p[0] and score <= p[1]:
                count += 1
        
        answer.append(count)

        
        
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150",
        "cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query)) # [1,1,1,1,2,4]