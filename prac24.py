
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
    print("초기 result 값 : {}".format(result))
    while find_test(result) :
        for i in range(len(result)-1):
            if i >= len(result):
                break
            print("i 값 : {}".format(i))
            print("현재 result : {}".format(result))
            if result[i] == result[i+1]:
                print("result 제거 전 : {}".format(result))
                del result[i]
                del result[i]
                print("result 제거 후 : {}".format(result))
    print("최종 result 값 : {}".format(result))
    if len(result) == 0:
        answer = 1
        return answer
    else:
        answer = 0
        return answer



    return answer

s = "baabaa"
print(solution(s))