from itertools import permutations

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_count(sub_nums, i):
    count = 0
    for n in sub_nums:
        word = ""
        for i in range(i):
            word += n[i]
        n = int(word)
        if is_prime(n):
            count += 1
    return count
    
def solution(numbers):
    answer = 0
    nums = []
    for i in range(len(numbers)):
        nums[i] = numbers[i]
    for i in range(2, len(numbers)):
        sub_nums = permutations(nums, i)
        answer += prime_count(sub_nums, i)
    
    return answer