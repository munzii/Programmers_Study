import sys

x, n = map(int, sys.stdin.readline().split())

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i*x)
    return answer

print(solution(x, n))