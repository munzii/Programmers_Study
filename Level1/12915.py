def solution(strings, n):
    return sorted(sorted(strings), key=lambda strings: strings[n])

print(solution(["sun", "bed", "car"], 1))