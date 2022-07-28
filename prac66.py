# 순위 검색

# 파악 했어야 하는 정보!!!
# 효율성테스트 위해 이진탐색 이용.
# 여기서 infos는 고정, queries의 query만 변함.
# 해시테이블 -> 딕셔너리를 이용.

# 내 풀이 <- 효율성 부족. 더 배우자!!!
def solution(info, query):
    answer = []
    people = []
    
    for i in info:
        
        a, b, c, d, e = i.split(" ")
        person = a + b + c + d
        p_score = int(e)
        people.append([person, p_score])
    
    for q in query:
        
        q = q.replace('and ', '')
        q = q.replace('-', '')
        a, b, c, d, e = q.split(" ")
        score = int(e)
        
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

# 다른 사람 풀이 1
def solution(infos, queries):
    answer = []

    info_dict = {}

    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    info_dict[lang + job + career + food] = []

    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        info_dict[lang + job + career + food].append(int(info[4]))

    
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()

        query_score = int(query[1])
        query = query[0]

        print(f'query : {query}')
        
        info_score = info_dict[query]  
        l = len(info_score)
        tmp = l

        print(f'info_score : {info_score}')
        
        low, high = 0, l - 1

        while low <= high:
            mid = (low + high) // 2

            if query_score <= info_score[mid]:
                tmp = mid
                high = mid - 1

            else:
                low = mid + 1

        answer.append(l - tmp)
    return answer

# 다른 사람 풀이 2
from functools import reduce
from collections import defaultdict
from bisect import insort, bisect_left

def solution(info, query):
    table = {"c": 3, "j": 5, "p": 6, "b": 6, "f": 5, "s": 6, "-": 0}
    conv = lambda l, t: (reduce(lambda a, k: (a << 3) + t(table[k[0]]), l[:-1], 0), int(l[-1]))
    info = list(map(lambda s: conv(s.split(" "), lambda x: 7 - x), info))
    query = list(map(lambda s: conv([c for c in s.split(" ") if c != "and"], lambda x: x), query))
    d = defaultdict(list)
    for k, v in info:
        insort(d[k], v)
    return [sum([len(l) - bisect_left(l, v) for k, l in d.items() if not k & q]) for q, v in query]