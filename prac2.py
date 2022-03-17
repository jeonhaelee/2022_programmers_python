

def solution(numbers, hand):
    answer = ''
    
    left = 0
    right = 0
    
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
            elif left == 1 or left == 5 or right == 5 or right == 3:
                if hand == "right":
                    answer += "R"
                    right = 2
                else :
                    answer += "L"
                    left = 2
            elif left == 4 or left == 8 or right == 8 or right == 6:
                if hand == "right":
                    answer += "R"
                    right = 2
                else :
                    answer += "L"
                    left = 2
            elif left == 7 or left == 0 or right == 0 or right == 9:
                if hand == "right":
                    answer += "R"
                    right = 2
                else :
                    answer += "L"
                    left = 2
            continue
                    
        if numbers[i] == 5:
            if numbers[i-1] == 5:
                answer += answer[-1]
            elif left == 4 or left == 2 or left == 8 or right == 2 or right == 8 or right == 6:
                if left == 4 and right == 6:
                    if hand == "right":
                        answer += "R"
                        right = 5
                    else :
                        answer += "L"
                        left = 5
                elif left == 4:
                    answer += "L"
                    left = 5
                elif right == 6:
                    answer += "R"
                    left = 5
                else:
                    if hand == "right":
                        answer += "R"
                        right = 5
                    else :
                        answer += "L"
                        left = 5
            elif left == 1 or left == 7 or right == 3 or right == 9:
                if hand == "right":
                    answer += "R"
                    right = 5
                else :
                    answer += "L"
                    left = 5
            elif left == 0 or right == 0:
                if hand == "right":
                    answer += "R"
                    right = 5
                else :
                    answer += "L"
                    left = 5
            continue
                    
        if numbers[i] == 8:
            if numbers[i-1] == 8:
                answer += answer[-1]
            elif left == 7 or left == 5 or left == 0 or right == 5 or right == 0 or right == 9:
                if hand == "right":
                    answer += "R"
                    right = 8
                else :
                    answer += "L"
                    left = 8
            elif left == 4 or left == 2 or right == 2 or right == 6:
                if hand == "right":
                    answer += "R"
                    right = 8
                else :
                    answer += "L"
                    left = 8
            elif left == 1 or right == 3:
                if hand == "right":
                    answer += "R"
                    right = 8
                else :
                    answer += "L"
                    left = 8
            continue
                    
        if numbers[i] == 0:
            if numbers[i-1] == 0:
                answer += answer[-1]
            elif left == 8 or right == 8:
                if hand == "right":
                    answer += "R"
                    right = 0
                else :
                    answer += "L"
                    left = 0
            elif left == 7 or left == 5 or right == 5 or right == 9:
                if hand == "right":
                    answer += "R"
                    right = 0
                else :
                    answer += "L"
                    left = 0
            elif left == 4 or left == 2 or right == 2 or right == 6:
                if hand == "right":
                    answer += "R"
                    right = 0
                else :
                    answer += "L"
                    left = 0
            elif left == 1 or right == 3:
                if hand == "right":
                    answer += "R"
                    right = 0
                else :
                    answer += "L"
                    left = 0
            continue
            
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
solution(numbers, hand)