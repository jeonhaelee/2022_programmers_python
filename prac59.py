# 큰 수 만들기
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
# 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 탐욕법 - 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법.

def solution(number, k):
    answer = []
    for num in number:
        while answer and answer[-1] < num and k > 0:
            k -= 1
            answer.pop()
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)


number = "1924"
k = 2
print(solution(number, k)) # "94"

number = "1231234"
k = 3
print(solution(number, k)) # "3234"

number = "4177252841"
k = 4
print(solution(number, k)) # "775841"

