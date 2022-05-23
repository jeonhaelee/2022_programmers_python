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
    
    sub = []
    for i in range(len(li)):
      sub_sub = [li[i]]
      for j in range(i+1, len(li)):
        if li[i][1] == li[j][1]:
          sub_sub.append(li[j])
      sub.append(sub_sub)
    
    for i in sub:
      print(i)

    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

# numbers = [4, 1, 2, 1]
# target = 4