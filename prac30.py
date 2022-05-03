def solution(n):
    answer = 0
    start_num = 1
    while start_num <= n:
        sub_ans = 0
        for i in range(start_num, n+1):
            sub_ans += i
            if sub_ans == n:
                start_num += 1
                answer += 1
                break
            if sub_ans > n:
                start_num += 1
                break
    return answer