

def solution(num):
    answer = ''
    sub_answer = ''
    
    if num <= 3:
        if num % 3 == 0:
            return 4
        elif num % 3 == 1:
            return 1
        elif num % 3 == 2:
            return 2
    else:
        rest = num % 3
        if rest == 1:
            sub_answer += '1'
        elif rest == 2:
            sub_answer += '2'
        else: sub_answer += '4'
        
        number = (num-3)
        while number > 9:
            number, rest = divmod(number,9)
            if 1 <= rest and rest <= 3:
                sub_answer += '1'
            elif 4 <= rest and rest <= 6:
                sub_answer += '2'
            elif 7 <= rest and rest <= 9:
                sub_answer += '4'
        if 1 <= number and number <= 3:
            sub_answer += '1'
        elif 4 <= number and number <= 6:
            sub_answer += '2'
        elif 7 <= number and number <= 9:
            sub_answer += '4'
        
    for i in range(len(sub_answer)-1,-1,-1):
        answer += sub_answer[i]
        
    return int(answer)
