
# def is_all_finish(progresses):
#     for i in progresses:
#         if i < 100:
#             return False
#     return True

# def solution(progresses, speeds):
#     answer = []
#     finished_number = 0
#     while is_all_finish(progresses) == False:
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]
#         for i in range(finished_number, len(progresses)):
#             working = progresses[i]
#             if working >= 100:
#                 finished_number += 1
#         answer.append(finished_number)
#     return answer

def solution(progresses, speeds):
    answer = []
    finished_number = 0
    while len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            print(progresses)
        for i in range(len(progresses)):
            if progresses[i] < 100:
                continue
            del progresses[i]
            del speeds[i]
            finished_number += 1
        answer.append(finished_number)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)
