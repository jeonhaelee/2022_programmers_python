

def solution(n):
    d = []
    for i in range(len(str(n))):
        d.append(str(n)[i])
    answer = 0
    for i in d:
        answer += int(i)
    return answer



