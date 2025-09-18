def solution(n, times):
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) //2
        total =0 
        
        for t in times:
            total += mid // t
            if total >= n :
                break
        if total >= n:
            answer = mid
            right = mid -1
        else:
            left = mid +1
    return answer
