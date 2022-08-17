# 삼각 달팽이

# 내 풀이
def solution(n):
    answer = []
    num = 1
    
    li = [[0] * n for i in range(n)]
    x = -1; y = 0
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            li[x][y] = num
            num += 1
    
    for i in range(n):
        for j in range(n):
            if li[i][j] != 0:
                answer.append(li[i][j])
    
    return answer

n = 4
print(solution(n)) # [1,2,9,3,10,8,4,5,6,7]

n = 5
print(solution(n)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

# 다른 사람 풀이 1
def solution(n):
    dx=[0,1,-1];dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)]
    x,y=0,0;num=1;d=0
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d];nx=x+dx[d];num+=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:y,x=ny,nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    return sum(b,[])

# 다른 사람 풀이 2
from itertools import chain
def solution(n):
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
    return list(chain(*board))

# 다른 사람 풀이 3
import sys
sys.setrecursionlimit(1000000)

class Triangle():
    def __init__(self,n):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.cnt = 1
        self.answer = []
        self.ldown(0,0,n)
        for i in range(n):
            for j in range(i+1):
                self.answer.append(self.board[i][j])

    def ldown(self,x,y,n):
        if n < 1:
            return 0
        for i in range(x,x+n):
            self.board[i][y] = self.cnt
            self.cnt += 1
        self.right(i,y+1,n-1)

    def right(self,x,y,n):
        if n < 1:
            return 0
        for j in range(y,y+n):
            self.board[x][j] = self.cnt
            self.cnt += 1
        self.lup(x-1,j-1,n-1)

    def lup(self,x,y,n):
        if n < 1:
            return 0
        for i in range(x,x-n,-1):
            self.board[i][y] = self.cnt
            y -= 1
            self.cnt += 1
        self.ldown(i+1,y+1,n-1)

def solution(n):
    triangle = Triangle(n)
    return triangle.answer