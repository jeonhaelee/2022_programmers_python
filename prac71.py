# 행렬 테두리 회전하기
import numpy as np

def solution(rows, columns, queries):
    answer = []
    arr = np.arange(1, rows * columns + 1).reshape(rows, columns)
    
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        temp_list = []
        
        temp = arr[x1+1, y1]
        temp_list.append(temp)

        count = y1
        while count < y2:
            arr[x1, count], temp = temp, arr[x1, count]
            temp_list.append(temp)
            count += 1
        
        count = x1
        while count < x2:
            arr[count, y2], temp = temp, arr[count, y2]
            temp_list.append(temp)
            count += 1
            
        count = y2
        while count > y1:
            arr[x2, count], temp = temp, arr[x2, count]
            temp_list.append(temp)
            count -= 1
            
        count = x2
        while count > x1:
            arr[count, y1], temp = temp, arr[count, y1]
            temp_list.append(temp)
            count -= 1
            
        answer.append(min(temp_list))

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries)) # [8, 10, 25]