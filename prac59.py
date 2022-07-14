# 큰 수 만들기
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
# 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 탐욕법 - 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법.

# 문제 파악 실수 -> 다시 해보자!
# 시간 초과 나옴. 이중 for문 없애보자.


from itertools import combinations

def get_make(set, numbers):
    get = ""
    for i in range(len(numbers)):
        if i in set:   
            pass
        else:
            get += numbers[i]
    return get

def solution(number, k):
    answer = ''
    numbers = list(number)
    
    idx = []
    for i in range(len(number)):
        idx.append(i)
        
    sets = list(combinations(idx, k))
    
    result = []
        
    while len(sets) != 0:
        get = get_make(sets[0], numbers)
        result.append(get)
        del sets[0]
    
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
