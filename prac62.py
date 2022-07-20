# 오픈채팅방

def solution(record):
    answer = []
    user_id = []
    user_name = []
    
    for re in record:
        action, info = re.split(maxsplit=1)
        print(f'action : {action}, info : {info}')
        
        if action == 'Enter':
            id, name = info.split()
            if id not in user_id:
                user_id.append(id)
                user_name.append(name)
            else:
                idx = user_id.index(id)
                user_name[idx] = name
        
        if action == 'Change':
            id, name = info.split()
            idx = user_id.index(id)
            user_name[idx] = name
        
        
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]