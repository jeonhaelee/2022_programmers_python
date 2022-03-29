

def solution(strings, n):
    d = []
    for i in range(len(strings)):
        d.append(strings[i][n:])
    d.sort()
    answer = []
    for i in range(len(strings)):
        for j in range(len(strings)):
            if d[i] == strings[j][n:]:
                answer.append(strings[j])
    return answer

print(solution(["abce", "abcd", "cdx"], 2))