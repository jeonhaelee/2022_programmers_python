def solution(number, k):
    answer = ''
    numbers = list(map(int, [x for x in number]))
    numbers_s = sorted(numbers)

    for i in range(k):
      answer1 = ''
      answer2 = ''
      for x in numbers[1:]:
        answer1 += str(x)
      for i in range(len(numbers)):
        if i == numbers.index(numbers_s[0]):
          continue
        else:
          answer2 += str(numbers[i])

      if answer1 > answer2:
        del numbers[0]
      else:
        del numbers[numbers.index(numbers_s[0])]
        del numbers_s[0]

    for x in numbers:
      answer += str(x)
    return answer