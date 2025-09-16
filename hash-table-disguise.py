def solution(clothes):
    clothes_map = {}
    
    for item, kind in clothes:
        clothes_map[kind] = clothes_map.get(kind, 0) +1
    
    answer = 1
    for count in clothes_map.values():
        answer *= (count + 1)
    
    return answer -1
