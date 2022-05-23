def count_onezero(n):
    one = 0; zero = 0
    for i in range(2, len(bin(n))):
      if bin(n)[i] == '1':
        one += 1
      else : zero += 1
    return one, zero

def solution(n):
    answer = 0

    n_one, n_zero = count_onezero(n)

    i = 1
    while True:
      sol_one, sol_zero = count_onezero(n+i)
      if n_one == sol_one and n_zero == sol_zero:
        answer = n+i
        return answer
      i += 1
  
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

print(solution(78))