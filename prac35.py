import numpy as np

def solution(clothes):
    answer = 1

    type = []
    for cloth in clothes:
      if cloth[1] not in type:
        type.append(cloth[1])

    type_num = np.zeros(len(type), dtype = np.int8)
    for cloth in clothes:
      idx = type.index(cloth[1])
      type_num[idx] += 1

    for num in type_num:
      answer *= (int(num)+1)

    return answer-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))