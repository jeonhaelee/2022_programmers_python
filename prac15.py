

def solution(s):
    answer = ''
    sub_answer = ''
    
    for i in range(len(s)): # 입력 받은 s의 길이만큼 for문 순회
        
        if s[i] != ' ': # s[i]번째 문자가 공백이 아니라면 sub_answer에 더해줍니다.
            sub_answer += s[i]
            
        else: # s[i]번째 문자가 공백이라면 
              # sub_answer에 담아놨던 문자들을 조건에 맞게 대문자, 소문자로 바꾼 후 answer에 더해줍니다.
            for j in range(len(sub_answer)): # sub_answer의 길이만큼 for문 순회
                if j % 2 == 0: # 인덱스가 짝수이면(홀수번째 문자이면) 대문자로,
                    answer += sub_answer[j].upper()
                else :         # 아니라면 소문자로 바꿔 answer에 더해줍니다.
                    answer += sub_answer[j].lower()
            answer += ' ' # 단어 하나를 answer에 넣었다면 다음 단어를 넣기 전 공백을 더해줍니다.
            sub_answer = '' # 다음 단어를 위해 sub_answer는 다시 빈 문자열로 만들어줍니다.
    
    # 맨 끝 단어는 s가 공백으로 끝나지 않아 위 for문을 통해 출력되지 않으므로 ,
    # 맨 끝 단어가 담긴 sub_answer을 조건에 맞게 대소문자를 바꾼 후, answer에 더해주는 과정을 한번 해줍니다.
    for j in range(len(sub_answer)): 
                if j % 2 == 0:
                    answer += sub_answer[j].upper()
                else :
                    answer += sub_answer[j].lower()

    # answer를 리턴해줍니다.
    return answer