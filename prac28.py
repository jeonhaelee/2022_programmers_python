import math

def solution(brown, yellow):
    answer = []
    x = 0; y = 0
    value = (brown - 4)/2
    x = (value + math.sqrt(pow(value,2)-4*yellow))/2
    y = 3 - x
    answer.append(int(x)+2)
    answer.append(int(y)+2)
    return answer

brown = 10
yellow = 2
print(solution(brown, yellow))