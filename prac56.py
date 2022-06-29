# 크레인 인형뽑기 게임
# "N x N" 크기의 정사각 격자. 인형이 없는 칸은 빈칸.

# 첫번째 내 풀이

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

# 첫번째 풀이 정리한 두번째 내 풀이

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

# 다른 사람 풀이 1

def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

# 다른 사람 풀이 2

def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a