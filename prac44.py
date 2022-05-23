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

    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

# numbers = [4, 1, 2, 1]
# target = 4