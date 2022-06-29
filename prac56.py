# 크레인 인형뽑기 게임
# "N x N" 크기의 정사각 격자. 인형이 없는 칸은 빈칸.


get = []

def get_item(board, check_n):
    global get
    get_num = None
    
    for i in range(len(board)):
        if board[i][check_n-1] != 0:
            get_num = board[i][check_n-1]
            board[i][check_n-1] = 0
            break
    if get_num == None:
        pass
    else:
        get.append(get_num)

def if_same_remove(get, answer):
    
    if len(get) >= 2 and get[-2] == get[-1]:
        del get[-1]
        del get[-1]
        answer += 1
    
    return answer

def check_same():
    result = False
    global get
    
    if len(get) >= 2:
        for i in range(len(get)-1):
           if get[i] == get[i+1]:
                result = True
                return result
                
    return result

def solution(board, moves):
    answer = 0
    global get
    
    for n in moves:
        get_item(board, n)
        print(f'{n} 넣은 후 get : {get}')
        answer = if_same_remove(get, answer)
    
    while check_same() :
        for i in range(len(get)-1):
            if get[i] == get[i+1]:
                    answer += 1
                    del get[i]
                    del get[i]
    
    print(f'최종 board : {board}')
    print(f'최종 get : {get}')
    return answer*2

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves)) # 4