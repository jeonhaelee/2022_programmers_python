# 행렬 테두리 회전하기
import numpy as np

def solution(rows, columns, queries):
    answer = []
    arr = np.arange(1, rows * columns + 1).reshape(rows, columns)
    print(arr)
    
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        
        temp = arr[x1, y1-1]
        count = y1
        while count < y2:
            arr[x1, y1] = temp
            temp = arr[x1, y1 + 1]
            count += 1
        
        count = x1
        while count < x2:
            arr[x1, y2] = temp
            temp = arr[x1+1, y2]
            count += 1
            
        count = y2
        while count > y1:
            arr[x1, y1] = temp
            temp = arr[x1, y1-1]
            count -= 1
            
        count = x2
        while count > x1:
            arr[x1, y1] = temp
            temp = arr[x1-1, y1]
            count -= 1

        
        
        
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries)) # [8, 10, 25]