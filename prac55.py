# 키패드 누르기
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작.

left_loc = -1
right_loc = -1


def check_distance_2(hand):
    global left_loc
    global right_loc
    
    left_score = 0; right_score = 0
    if left_loc == 2:
        left_score = 1
    elif left_loc in (1, 5):
        left_score = 2
    elif left_loc in (4, 8):
        left_score = 3
    elif left_loc in (7, 0):
        left_score = 4
    else : left_score = 5
    
    if right_loc == 2:
        right_score = 1
    elif right_loc in (1, 5):
        right_score = 2
    elif right_loc in (4, 8):
        right_score = 3
    elif right_loc in (7, 0):
        right_score = 4
    else : right_score = 5
        
    if left_score < right_score:
        left_loc = 2
        return "L"
    elif left_score > right_score:
        right_loc = 2
        return "R"
    else:
        if hand == "left":
            left_loc = 2
            return "L"
        else:
            right_loc = 2
            return "R"
        
def check_distance_5(hand):
    global left_loc
    global right_loc
    
    left_score = 0; right_score = 0
    if left_loc == 5:
        left_score = 1
    elif left_loc in (2, 4, 8):
        left_score = 2
    elif left_loc in (1, 7, 0):
        left_score = 3
    else : left_score = 4
    
    if right_loc == 5:
        right_score = 1
    elif right_loc in (2, 6, 8):
        right_score = 2
    elif right_loc in (3, 9, 0):
        right_score = 3
    else : right_score = 4
        
    if left_score < right_score:
        left_loc = 5
        return "L"
    elif left_score > right_score:
        right_loc = 5
        return "R"
    else:
        if hand == "left":
            left_loc = 5
            return "L"
        else:
            right_loc = 5
            return "R"
        
def check_distance_8(hand):
    global left_loc
    global right_loc
    
    left_score = 0; right_score = 0
    if left_loc == 8:
        left_score = 1
    elif left_loc in (5, 7, 0):
        left_score = 2
    elif left_loc in (2, 4, -1):
        left_score = 3
    else : left_score = 4
    
    if right_loc == 8:
        right_score = 1
    elif right_loc in (5, 9, 0):
        right_score = 2
    elif right_loc in (2, 6, -1):
        right_score = 3
    else : right_score = 4
        
    if left_score < right_score:
        left_loc = 8
        return "L"
    elif left_score > right_score:
        right_loc = 8
        return "R"
    else:
        if hand == "left":
            left_loc = 8
            return "L"
        else:
            right_loc = 8
            return "R"

def check_distance_0(hand):
    global left_loc
    global right_loc
    
    left_score = 0; right_score = 0
    if left_loc == 0:
        left_score = 1
    elif left_loc in (8, -1):
        left_score = 2
    elif left_loc in (5, 7):
        left_score = 3
    elif left_loc in (2, 4):
        left_score = 4
    else : left_score = 5
    
    if right_loc == 0:
        right_score = 1
    elif right_loc in (8, -1):
        right_score = 2
    elif right_loc in (5, 9):
        right_score = 3
    elif right_loc in (2, 6):
        right_score = 4
    else : right_score = 5
        
    if left_score < right_score:
        left_loc = 0
        return "L"
    elif left_score > right_score:
        right_loc = 0
        return "R"
    else:
        if hand == "left":
            left_loc = 0
            return "L"
        else:
            right_loc = 0
            return "R"
        
def solution(numbers, hand):
    answer = ''
    
    for num in numbers:
        if num in (1, 4, 7):
            answer += "L"
            left_loc = num
            
        elif num in (3, 6, 9):
            answer += "R"
            right_loc = num
            
        else:
            if num == 2:
                answer += check_distance_2(hand)
            elif num == 5:
                answer += check_distance_5(hand)
            elif num == 8:
                answer += check_distance_8(hand)
            elif num == 0:
                answer += check_distance_0(hand)
                
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))