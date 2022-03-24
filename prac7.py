

def solution(sizes):
    answer = 0
    long = []
    short = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            long.append(sizes[i][0])
            short.append(sizes[i][1])
        else : 
            long.append(sizes[i][1])
            short.append(sizes[i][0])
    answer = max(long) * max(short)
    return answer

