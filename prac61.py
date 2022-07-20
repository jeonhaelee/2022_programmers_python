# 문자열 압축

# 내 풀이
def make_short(s, n):
    result = ""
    
    target = s[0:n]
    target_count = 1
    
    for i in range(n, len(s), n):
        if s[i:i+n] == target:
            target_count += 1
        else:
            if target_count == 1:
                pass
            else:
                result += str(target_count)
            result += target
            target = s[i:i+n]
            target_count = 1
            
    if target_count == 1:
        pass
    else:
        result += str(target_count)
    result += target

    
    print(f'n : {n}, result : {result}')
    return result

def solution(s):
    answer = len(s)
    print(f'len(s) : {len(s)}')
    
    for n in range(1, len(s)):
        result = make_short(s, n)
        if len(result) < answer:
            answer = len(result)
        
    return answer

s = "aabbaccc"
print(solution(s)) # 7

s = "ababcdcdababcdcd"
print(solution(s)) # 9

s = "abcabcdede"
print(solution(s)) # 8

s = "abcabcabcabcdededededede"
print(solution(s)) # 14

s = "xababcdcdababcdcd"
print(solution(s)) # 17

# 다른 사람 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))