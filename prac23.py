def solution(priorities, location):
    answer = 0
    tasks = []
    for i in range(len(priorities)):
        tasks.append((priorities[i], i))
    while tasks[0][1] != location:
        max_val = max(priorities)
        if tasks[0][0] != max_val:
            tasks.append(tasks[i])
            del tasks[0]
        else: del tasks[0]
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