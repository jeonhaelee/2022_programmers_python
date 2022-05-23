def count_onezero(n):
    one = 0; zero = 0
    for i in range(2, len(bin(n))):
      if bin(n)[i] == '1':
        one += 1
      else : zero += 1
    return one, zero

def solution(n):
    n_one, n_zero = count_onezero(n)

    i = 1
    while True:
      sol_one, sol_zero = count_onezero(n+i)
      if n_one == sol_one:
        return n + i
      i += 1