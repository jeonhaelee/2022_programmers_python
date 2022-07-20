# 오픈채팅방
# 시간초과 해결 요함. 딕셔너리 이용해보자.


# def solution(record):
#     answer = []
#     user_id = []
#     user_name = []
    
#     for re in record:
#         action, info = re.split(maxsplit=1)
        
#         if action == 'Enter':
#             id, name = info.split()
#             if id not in user_id:
#                 user_id.append(id)
#                 user_name.append(name)
#             else:
#                 idx = user_id.index(id)
#                 user_name[idx] = name
        
#         if action == 'Change':
#             id, name = info.split()
#             idx = user_id.index(id)
#             user_name[idx] = name
        
#     for re in record:
#         action, info = re.split(maxsplit=1)
    
#         if action == 'Enter':
#             id, name = info.split()
#             idx = user_id.index(id)
#             sentence = user_name[idx] + "님이 들어왔습니다."
#             answer.append(sentence)
            
#         if action == 'Leave':
#             id = info
#             idx = user_id.index(id)
#             sentence = user_name[idx] + "님이 나갔습니다."
#             answer.append(sentence)
            
#     return answer

def solution(record):
    answer = []
    user_id = []
    user_info = {}
    
    for re in record:
        action, info = re.split(maxsplit=1)
        
        if action == 'Enter':
            id, name = info.split()
            if id not in user_id:
                user_id.append(id)
                user_info[id] = name
            else:
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