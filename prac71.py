# 행렬 테두리 회전하기
import numpy as np

def solution(rows, columns, queries):
    answer = []
    arr = np.arange(1, rows * columns + 1).reshape(rows, columns)
    print(arr)
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries)) # [8, 10, 25]