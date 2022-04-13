

def solution(number):
    result = ''
    while number > 0:
        number, rest = divmod(number,3)
        if rest == 1:
            result += '1'
        elif rest == 2:
            result += '2'
        else : result += '4'
        if rest == 0:
            number -= 1
    answer = ""
    for i in range(len(result)-1,-1,-1):
        answer += result[i]
    return int(answer)