

def is_all_finish(progresses): # 모든 기능이 완료되었는지 확인하는 함수
    for i in progresses:
        if i < 100:
            return False
    return True

def solution(progresses, speeds):
    answer = []
    finished_number = 0 # 어떤 기능이 완료되었을 때 함께 배포 가능한 총 기능 수를 담을 변수
    stack = 0
    while is_all_finish(progresses) == False: # 모든 기능이 완료될 때까지 while문 반복
        for i in range(len(progresses)): # while문을 돌 때마다 각 기능에 해당 개발 속도를 더해준다
            progresses[i] += speeds[i]
        for i in range(stack, len(progresses)):
            working = progresses[i]
            stack = i
            if working < 100: # i 번째의 기능이 완료되지 않았을 경우 for문 탈출
                break
            else : finished_number += 1 # 기능이 완료되었을 경우 +1씩 해주기
        if finished_number > 0: # finished_number가 1 이상인 경우에만 answer에 넣어주는 조건
            answer.append(finished_number)
            finished_number = 0 # 다음 기능부터 배포가능한 수를 다시 세기 위해 0으로 다시 만들어준다
    return answer

