def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0

print(solution(10))