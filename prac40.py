def solution(number, k):
    answer = ''
    numbers = list(map(int, [x for x in number]))
    numbers_s = sorted(numbers)

    for i in range(k):
      del numbers[numbers.index(numbers_s[0])]
      del numbers_s[0]

    for x in numbers:
      answer += str(x)
    return answer

number = "4177252841"
k = 4
print(solution(number, k)) #"775841"