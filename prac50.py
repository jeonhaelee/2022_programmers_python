# 신고 결과 받기


def solution(id_list, report, k):
    answer = []
    count = []
    result = []
    for i in range(len(id_list)):
        result.append([])
        answer.append(0)
        count.append(0)

    for id in report:
        id1, id2 = id.split(" ")
        result[id_list.index(id1)].append(id2)
        count[id_list.index(id2)] += 1
    
    print(result)
    print(count)
    
    target = []
    for i in range(len(id_list)):
        if count[i] >= k:
            target.append(id_list[i])
    
    for i in range(len(result)):
        for j in result[i]:
            if j in target:
                answer[i] += 1
    print('answer :', answer)
    
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))    # [2,1,1,0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))    # [0,0]