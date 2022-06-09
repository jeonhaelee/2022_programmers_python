# 신고 결과 받기


def solution(id_list, report, k):
    answer = []
    
    result = []
    for i in range(len(id_list)):
        result.append([])

    for id in report:
        id1, id2 = id.split(" ")
        result[id_list.index(id1)].append(id2)
    
    
       
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))    # [2,1,1,0]