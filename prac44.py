# 다시 새롭게 만들어보자.

import math

def solution(numbers, target):
    true_answer = 0

    answer = numbers[0]

    li = [['+', numbers[0]]]
    for i in range(1, len(numbers)):
      if answer < target:
        answer += numbers[i]
        li.append(['+', numbers[i]])
      else :
        answer -= numbers[i]
        li.append(['-', numbers[i]])
    
    print(li)
    print(answer)
    if answer == target:
      true_answer += 1


    answer = -numbers[0]
    li = [['-', numbers[0]]]
    for i in range(1, len(numbers)):
      if answer < target:
        answer += numbers[i]
        li.append(['+', numbers[i]])
      else :
        answer -= numbers[i]
        li.append(['-', numbers[i]])

    print(li)
    print(answer)
    if answer == target:
      true_answer += 1

    return true_answer

# numbers = [1, 1, 1, 1, 1]
# target = 3
# print(solution(numbers, target)) # 5

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target)) # 2