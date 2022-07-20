# 오픈채팅방

# 내 풀이
def solution(record):
    answer = []
    user_info = {}
    
    for re in record:
        action, info = re.split(maxsplit=1)
        
        if action == 'Enter':
            id, name = info.split()
            user_info[id] = name
        
        if action == 'Change':
            id, name = info.split()
            user_info[id] = name
        
    for re in record:
        action, info = re.split(maxsplit=1)
    
        if action == 'Enter':
            id, name = info.split()
            sentence = user_info[id] + "님이 들어왔습니다."
            answer.append(sentence)
            
        if action == 'Leave':
            id = info
            sentence = user_info[id] + "님이 나갔습니다."
            answer.append(sentence)
            
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# 다른 사람 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer