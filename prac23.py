def solution(priorities, location):
    answer = 0
    
    tasks = []
    for i in range(len(priorities)):
        tasks.append((priorities[i], i))
    print(tasks)
    
    value = tasks[location]
    while value in tasks:
        temp_list = sorted(tasks, key= lambda x : -x[0])
        max_val = temp_list[0][0]
        print(max_val)
        if tasks[0][0] != max_val:
            tasks.append(tasks[0])
            del tasks[0]
        else: del tasks[0]
        print(tasks)
        answer += 1
        
    return answer


# def solution(priorities, location):
#     answer = 0
#     work_idx = 0
#     while work_idx == location:
#         max_idx = list.index(priorities)
#         work_idx = max_idx
#         priorities[work_idx] = 0
#         answer += 1
#     return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))