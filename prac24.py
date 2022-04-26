
from unittest import result


def find_test(sub_result):
    for i in range(len(sub_result)-1):
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
            if result[i] == result[i+1]:
                del result[i]
                del result[i+1]
    if len(result) == 0:
        answer = 1
        return answer
    else:
        answer = 0
        return answer



    return answer

s = "baabaa"
print(solution(s))