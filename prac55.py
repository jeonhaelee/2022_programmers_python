# 키패드 누르기
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작.

left_loc = 0
right_loc = 0
h = ""

def check_distance(num):
    global left_loc
    global right_loc
    global h
    
    if left_loc == num or right_loc == num:

def solution(numbers, hand):
    answer = ''
    global left_loc
    global right_loc
    global h
    h = hand
    
    for num in numbers:
        if num in (1, 4, 7):
            answer += "L"
            left_loc = num
            
        elif num in (3, 6, 9):
            answer += "R"
            right_loc = num
            
        else:
            if num == 2:
                
            elif num == 5:
                
            elif num == 8:
                
            elif num == 0:
                
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))