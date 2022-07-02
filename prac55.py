# 키패드 누르기
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작.

def solution(numbers, hand):
    answer = ''
    
    for num in numbers:
        if num in (1, 4, 7):
            answer += "L"
        elif num in (3, 6, 9):
            answer += "R"
    return answer