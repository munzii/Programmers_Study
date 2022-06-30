def solution(arr, divisor):
    s=[]
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            s.append(arr[i])
    if len(s) != 0:
        s.sort()
        return s
    else:
        return [-1]
    
print(solution([5,9,7,10], 5))