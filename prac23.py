

from re import S

from numpy import take


def solution(priorities, location):
    answer = 0
    
    tasks = []
    for i in range(len(priorities)):
        tasks.append((priorities[i], i))
    print(tasks)
    
    value = tasks[location]
    print("찾으려는 값 : {}".format(value))
    while value in tasks:
        temp_list = sorted(tasks, key= lambda x : -x[0])
        max_val = temp_list[0][0]
        print(max_val)
        count = 0
        for val in tasks:
            if val[0] == max_val:
                count += 1
        if count == len(tasks):
            answer += (tasks.index(value) + 1)
            break
        if tasks[0][0] != max_val:
            tasks.append(tasks[0])
            del tasks[0]
        else: 
            del tasks[0]
            answer += 1
        print(tasks)
        
    return answer


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))