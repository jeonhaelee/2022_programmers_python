# 큰 수 만들기
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
# 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 탐욕법 - 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법.

# 문제 파악 실수 -> 다시 해보자!
# 시간 초과 나옴. 조합이 문제? 그리디 알고리즘 이용해서 다시.


def solution(number, k):
    answer = ''
    
    numbers = list(number)
    
    i = 1
    out_idx = []
    set_idx = 0
    while i < len(numbers)-1:
        
        if numbers[i] < numbers[set_idx]:
            out_idx.append(i)
            i += 1
        else :
            out_idx.append(set_idx)
            set_idx = i
            i += 1
            
        if len(out_idx) == k:
            break

        
    for n in range(len(numbers)):
        if n in out_idx:
            continue
        else:
            answer += numbers[n]
            
    return answer


number = "1924"
k = 2
print(solution(number, k)) # "94"

number = "1231234"
k = 3
print(solution(number, k)) # "3234"

number = "4177252841"
k = 4
print(solution(number, k)) # "775841"
