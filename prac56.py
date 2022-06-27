# 크레인 인형뽑기 게임
# "N x N" 크기의 정사각 격자. 인형이 없는 칸은 빈칸.


def solution(board, moves):
    answer = 0
    n = len(board)
    get = []
    
    for i in range(len(moves)):
        num = moves[i]
        
        get.append(board[num][-1])
        board[num][-1] = 0
        
        if len(get) >= 2 and get[-2] == get[-1]:
            del get[-1]
            del get[-1]
            answer += 1
            
    print(board) 
    print(get)
    
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves)) # 4