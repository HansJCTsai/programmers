def solution(distance, rocks, n):
    rocks.sort()
    left, right = 1, distance
    answer = 0
     
    while left <= right:
        mid = (left + right) //2
        prv = 0
        removed = 0
        
        for rock in rocks:
            if rock - prv < mid:
                removed += 1
            else :
                prv = rock
        if distance - prv < mid:
            removed += 1
        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer
