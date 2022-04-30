import math

def solution(brown, yellow):
    answer = []
    value = (brown - 4)/2
    x = (value + math.sqrt(pow(value,2)-4*yellow))/2
    y = value - x
    answer.append(int(x)+2)
    answer.append(int(y)+2)
    return answer
