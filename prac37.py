import sys
sys.setrecursionlimit(10**7)

def solution(n):
    arr = [-1]*(n+1)
    arr[0] = 0
    arr[1] = 1
    return find(arr, n) % 1234567

def find(arr, n):   # 이미 구했었던 피보나치수라면, 찾아서 꺼내주는 식으로 시간 단축
    if arr[n] != -1:
      return arr[n]
    else:
      arr[n] =  find(arr, n-1) + find(arr, n-2)
      return arr[n]



# 다른 사람 풀이
# 재귀 함수를 이용하지 않은 풀이

def f(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a

