# 타겟 넘버
# 다시 스스로 해보자.

def solution(numbers, target):
    answer = 0
    return answer

###

import math

def solution(numbers, target):
    true_answer = 0
    li_answer = []

    count = 0
    while count < len(numbers):
      answer = numbers[count]
      li = []
      for i in range(len(numbers)):
        if i == count:
          li.append(['+', numbers[count]])
          continue
        if answer < target:
          answer += numbers[i]
          li.append(['+', numbers[i]])
        else :
          answer -= numbers[i]
          li.append(['-', numbers[i]])
      
      if li not in li_answer:
        li_answer.append(li)
        if answer == target:
          true_answer += 1


      answer = -numbers[count]
      li = []
      for i in range(len(numbers)):
        if i == count:
          li.append(['-', numbers[count]])
          continue
        if answer < target:
          answer += numbers[i]
          li.append(['+', numbers[i]])
        else :
          answer -= numbers[i]
          li.append(['-', numbers[i]])

      if li not in li_answer:
        li_answer.append(li)
        if answer == target:
          true_answer += 1

      count += 1


    return true_answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5

