# 큰 수 만들기
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
# 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 탐욕법 - 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법.

# 문제 파악 실수 -> 다시 해보자!

from itertools import combinations

def solution(number, k):
    answer = ''
    # numbers = list(number)
    
    idx = []
    for i in range(len(number)):
        idx.append(i)
        
    sets = list(combinations(idx, k))
    
    result = []
    for set in sets:
        a, b = set[0], set[1]
        if a > b:
            a, b = b, a-1
        get1 = number[-a]
        print(f'get1 : {get1}')
        get2 = get1[-b]
        print(f'get2 : {get2}')
        result.append(''.join(get2))

    result.sort(reverse=True)
    
    answer = result[0]
    
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
