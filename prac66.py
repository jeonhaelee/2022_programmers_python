# 순위 검색

def solution(info, query):
    answer = []
    people = []
    
    for i in info:
        a, b, c, d, e = i.split(" ")
        person = {
            'language' : a,
            'type' : b,
            'technic' : c,
            'food' : d,
            'score' : e
        }
        people.append(person)
        
    for q in query:
        
        q = q.replace('and ', '')
        print(q)
        
        a, b, c, d, e = q.split(" ")
        
        if a == '-':
            a = ['cpp' , 'java' , 'python']
        else:
            a = list(a)
            
        if b == '-':
            b = ['backend' , 'frontend']
        else:
            b = list(b)
            
        if c == '-':
            c = ['junior , senior']
        else:
            c = list(c)
            
        if d == '-':
            d = ['chicken , pizza']
        else:
            d = list(d)
            
        count = 0
        for p in people:
            print(p)
            if p['language'] in a and p['type'] in b and p['technic'] in c and p['food'] in d and p['score'] >= e:
                count += 1
        
        # if '-' not in (a, b, c, d, e):
        #     count = 0
        #     for p in people:
        #         print(p)
        #         if p['language'] == a and p['type'] == b and p['technic'] == c and p['food'] == d and p['score'] >= e:
        #             count += 1
        
        answer.append(count)
        
        
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150",
        "cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query)) # [1,1,1,1,2,4]