# 행렬 테두리 회전하기
# 테스트는 통과. but 제출시 int64 불가? ==> int자료형으로 바꾸어서 append 해주면 해결 완료!

# 내 풀이
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
            
        answer.append(int(min(temp_list)))

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries)) # [8, 10, 25]


# 다른 사람 풀이 1
def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer


# 다른 사람 풀이 2
# deque의 rotate를 이용한 풀이
from collections import deque
def solution(rows, columns, queries):
    arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
    answer, result = deque(), []
    for i in queries:
        a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
        for x in range(d-b):
            answer.append(arr[a][b+x])
        for y in range(c-a):
            answer.append(arr[a+y][d])
        for z in range(d-b):
            answer.append(arr[c][d-z])
        for k in range(c-a):
            answer.append(arr[c-k][b])
        answer.rotate(1)
        result.append(min(answer))
        for x in range(d-b):
            arr[a][b+x] = answer[0]
            answer.popleft()
        for y in range(c-a):
            arr[a+y][d] = answer[0]
            answer.popleft()
        for z in range(d-b):
            arr[c][d-z] = answer[0]
            answer.popleft()
        for k in range(c-a):
            arr[c-k][b] = answer[0]
            answer.popleft()
    return result