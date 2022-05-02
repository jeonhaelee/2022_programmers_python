def solution(s):
    answer = ''
    d = list(map(int, s.split(" ")))
    min = d[0]; max = d[0]
    for num in d:
        if num < min :
            min = num
        if num > max :
            max = num
    answer += str(min)
    answer += " "
    answer += str(max)
    return answer

s = "-1 -2 -3 -4"
print(solution(s))