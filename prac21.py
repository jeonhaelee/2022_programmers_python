

def solution(num):
    answer = ''
    d = []

    while num > 0:
        num, rest = divmod(num, 3)
        d.append(rest)
        print("num : {}, rest : {}".format(num,rest))
    print("d : {}".format(d))
    for i in range(len(d)-1,-1,-1):
        n = int(d[i])
        if n == 1:
            answer += '1'
        elif n == 2:
            answer += '2'
        else: answer += '4'
    print("answer : {}".format(answer))
    return int(answer)


n = 6
print(solution(n))