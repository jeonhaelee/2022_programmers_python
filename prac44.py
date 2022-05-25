import math

def solution(numbers, target):
    answer = 0
    li = []

    for n in numbers:
      if answer < target:
        answer += n
        li.append(['+', n])
      else :
        answer -= n
        li.append(['-', n])
    
    print(li)
    # 같은 수들 중 +, - 다른 것들 순열

    nums = []
    nums_set = []
    for n in li:
      if n in nums:
        nums_set[nums.index(n)][1] += 1
      else:
        nums.append(n)
        nums_set.append([n,1])
      
    print("nums : ",end = "")
    print(nums)
    print("nums_set : ",end = "")
    print(nums_set)

    
    sub_ans = 1
    sub_over_one = 0
    for set in nums_set:
      if set[1] > 1:
        sub_over_one += 1
        sub_ans *= math.factorial(set[1])



    print("len(li)-sub_over_one : ", end = "")
    print(len(li)-sub_over_one)
    print("sub_ans : ",end = "")
    print(sub_ans)

    answer = sub_ans

    return int(answer)

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target)) # 2