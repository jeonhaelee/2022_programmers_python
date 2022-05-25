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
      if n[1] in nums:
        nums_set[nums.index(n[1])][1] += 1
      else:
        nums.append(n[1])
        nums_set.append([n[1],1])
        
    print(nums)
    print(nums_set)

    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

# numbers = [4, 1, 2, 1]
# target = 4