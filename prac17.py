 
def solution(n):
    answer = ""
    d = []
    a, b = divmod(n,3)
    count = 0
    for i in range(int(a/3)):
        if a >= pow(3,i) and a <= pow(3,i) * 2:
            count = i
    for i in range(count, -1, -1):
        if a - pow(3,i) * 2 >= 0:
            a -= pow(3,i) * 2
            d.append(2)
        elif a - pow(3,i) >= 0:
            a -= pow(3,i)
            d.append(1)
        else : d.append(0)
    d.append(b)
    for i in range(len(d)-1,-1,-1):
        answer += str(d[i])
    return int(answer,3)

print(solution(125))