# 폰켓몬
# nums는 폰켓몬의 종류 번호가 담긴 1차원 배열이며 개수는 항상 짝수.

# 내 풀이

def solution(nums):
    answer = 0
    
    num_list = []
    for n in nums:      # 이 부분을 set()을 이용해서 중복제거를 한번에 할 수 있음.
        if n in num_list:
            continue
        else:
            num_list.append(n)
            
    if int(len(nums)/2) <= len(num_list):
        answer = int(len(nums)/2)
    else:
        answer = len(num_list)
        
    return answer

nums = [3,1,2,3]
print(solution(nums)) # 2

nums = [3,3,3,2,2,4]
print(solution(nums)) # 3

# 다른 사람 풀이 1

def solution(ls):
    return min(len(ls)/2, len(set(ls)))