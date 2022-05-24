import math

def solution(numbers, target):
    answer = 0
    li = []

    for n in numbers:
      if answer < target:
        answer += n
        li.append(('+', n))
      else :
        answer -= n
        li.append(('-', n))
    
    print(li)
    # 같은 수들 중 +, - 다른 것들 순열

    nums = []
    numbers = []
    for num in li:
      if num[1] in nums:
        numbers[nums.index(num[1])][1] += 1
      else :
        nums.append(num[1])
        numbers.append((num[1], 1))
    print(numbers)

    # math.factorial()
    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

# numbers = [4, 1, 2, 1]
# target = 4