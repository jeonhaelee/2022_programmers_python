
def find_test(result):
    for i in range(len(result)-1):
        if result[i] == result[i+1]:
            return True
    return False

def solution(s):
    answer = -1
    result = []
    for i in range(len(s)):
        result += s[i]
    while find_test(result) :
        for i in range(len(result)-1):
            if i >= len(result):
                break
            if result[i] == result[i+1]:
                del result[i]
                del result[i]
    if len(result) == 0:
        answer = 1
        return answer
    else:
        answer = 0
        return answer

s = "cdcd"
print(solution(s))