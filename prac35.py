import numpy as np

def solution(clothes):
    answer = 1
    type = {}
    for name, cloth_type in clothes:
      if cloth_type not in type:
        type[cloth_type] = 2
      else :
        type[cloth_type] += 1
    print(type)
    for num in type.values() :
      answer *= num

    return answer - 1
