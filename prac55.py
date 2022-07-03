# 키패드 누르기
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작.

# 내 풀이

left_loc = -1; right_loc = -1

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
    elif right_loc in (3, 5):
        right_score = 2
    elif right_loc in (6, 8):
        right_score = 3
    elif right_loc in (9, 0):
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
    global left_loc
    global right_loc
    
    for num in numbers:
        
        if num in (1, 4, 7):
            answer += "L"
            left_loc = num
            
        elif num in (3, 6, 9):
            answer += "R"
            right_loc = num
            
        elif num == 2:
            answer += check_distance_2(hand)
            
        elif num == 5:
            answer += check_distance_5(hand)

        elif num == 8:
            answer += check_distance_8(hand)
            
        elif num == 0:
            answer += check_distance_0(hand)
            
                
    return answer


# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
# print(solution(numbers, hand)) # "LRLLLRLLRRL"


# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"
# print(solution(numbers, hand)) # "LRLLRRLLLRR"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand)) # "LLRLLRLLRL"


# 다른 사람 풀이

def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer