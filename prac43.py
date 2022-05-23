def count_onezero(n):
    one = 0; zero = 0
    print("n의 2진수 : {}".format(bin(n)))
    for i in range(2, len(bin(n))):
      if bin(n)[i] == '1':
        one += 1
      else : zero += 1
    print("one : {}, zero : {}".format(one, zero))
    return one, zero

count_onezero(15)

def solution(n):
    n_one, n_zero = count_onezero(n)
    print("n_one : {}, n_zero : {}".format(n_one, n_zero))

    i = 1
    while True:
      sol_one, sol_zero = count_onezero(n+i)
      if n_one == sol_one:
        return n + i
      i += 1
  
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

print(solution(15))