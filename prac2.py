

def solution(numbers, hand):
    answer = ''
    
    left = '*'
    right = '#'
    
    for i in range(0,len(numbers)):
        if numbers[i] == 1:
            answer += 'L'
            left = 1
            continue
        if numbers[i] == 4:
            answer += 'L'
            left = 4
            continue
        if numbers[i] == 7:
            answer += 'L'
            left = 7
            continue
            
        if numbers[i] == 3:
            answer += 'R'
            right = 3
            continue
        if numbers[i] == 6:
            answer += 'R'
            right = 6
            continue
        if numbers[i] == 9:
            answer += 'R'
            right = 9
            continue
            
        if numbers[i] == 2:
            if numbers[i-1] == 2:
                answer += answer[-1]
            elif left in (1,5) or right in (3,5):
                if left in (1,5) and right in (3,5):
                    if hand == "right":
                        answer += "R"
                        right = 2
                    else :
                        answer += "L"
                        left = 2
                elif left in (1,5):
                    answer += "L"
                    left = 2
                elif right in (3,5):
                    answer += "R"
                    right = 2
            elif left in (4,8) or right in (6,8):
                if left in (4,8) and right in (6,8):
                    if hand == "right":
                        answer += "R"
                        right = 2
                    else :
                        answer += "L"
                        left = 2
                elif left in (4,8):
                    answer += "L"
                    left = 2
                elif right in (6,8):
                    answer += "R"
                    right = 2
            elif left in (7,0) or right in (9,0):
                if left in (7,0) and right in (9,0):
                    if hand == "right":
                        answer += "R"
                        right = 2
                    else :
                        answer += "L"
                        left = 2
                elif left in (7,0):
                    answer += "L"
                    left = 2
                elif right in (9,0):
                    answer += "R"
                    right = 2
            elif left == '*' or right == '#':
                if left == '*':
                    answer += "L"
                    left = 5
                else :
                    answer += "R"
                    right = 5
            continue
                    
        if numbers[i] == 5:
            if numbers[i-1] == 5:
                answer += answer[-1]
            elif left in (4,2,8) or right in (6,2,8):
                if left in (4,2,8) and right in (6,2,8):
                    if hand == "right":
                        answer += "R"
                        right = 5
                    else :
                        answer += "L"
                        left = 5
                elif left in (4,2,8):
                    answer += "L"
                    left = 5
                elif right in (6,2,8):
                    answer += "R"
                    right = 5
            elif left in (1,7,0) or right in (3,9,0):
                if left in (1,7,0) and right in (3,9,0):
                    if hand == "right":
                        answer += "R"
                        right = 5
                    else :
                        answer += "L"
                        left = 5
                elif left in (1,7,0):
                    answer += "L"
                    left = 5
                elif right in (3,9,0):
                    answer += "R"
                    right = 5
            continue
                    
        if numbers[i] == 8:
            if numbers[i-1] == 8:
                answer += answer[-1]
            elif left in (7,5,0) or right in (9,5,0):
                if left in (7,5,0) and right in (9,5,0):
                    if hand == "right":
                        answer += "R"
                        right = 8
                    else :
                        answer += "L"
                        left = 8
                elif left in (7,5,0):
                    answer += "L"
                    left = 8
                elif right in (9,5,0):
                    answer += "R"
                    right = 8
            elif left in (4,2,'*') or right in (6,2,'#'):
                if left in (4,2,'*') and right in (6,2,'#'):
                    if hand == "right":
                        answer += "R"
                        right = 8
                    else :
                        answer += "L"
                        left = 8
                elif left in (4,2,'*'):
                    answer += "L"
                    left = 8
                elif right in (6,2,'#'):
                    answer += "R"
                    right = 8
            elif left == 1:
                answer += "L"
                left = 8
            elif right == 3:
                answer += "R"
                right = 8
            continue
                    
        if numbers[i] == 0:
            if numbers[i-1] == 0:
                answer += answer[-1]
            elif left in ('*',8) or right in ('#',8):
                if left in ('*',8) and right in ('#',8):
                    if hand == "right":
                        answer += "R"
                        right = 0
                    else :
                        answer += "L"
                        left = 0
                elif left in ('*',8):
                    answer += "L"
                    left = 0
                elif right in ('#',8):
                    answer += "R"
                    right = 0
            elif left in (7,5) or right in (9,5):
                if left in (7,5) and right in (9,5):
                    if hand == "right":
                        answer += "R"
                        right = 0
                    else :
                        answer += "L"
                        left = 0
                elif left in (7,5):
                    answer += "L"
                    left = 0
                elif right in (9,5):
                    answer += "R"
                    right = 0
            elif left in (4,2) or right in (6,2):
                if left in (4,2) and right in (6,2):
                    if hand == "right":
                        answer += "R"
                        right = 0
                    else :
                        answer += "L"
                        left = 0
                elif left in (4,2):
                    answer += "L"
                    left = 0
                elif right in (6,2):
                    answer += "R"
                    right = 0
            elif left == 1:
                answer += "L"
                left = 0
            elif right == 3:
                answer += "R"
                right = 0
            continue
            
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
solution(numbers, hand)