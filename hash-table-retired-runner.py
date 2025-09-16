#版本 1
def solution(participant, completion):
    count ={}
    for name in participant:
        count[name] = count.get(name, 0) + 1
        
    for name in completion:
        count[name] -= 1
        
    for name, c in count.items():
        if c != 0:
            return name

#版本 2
from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return next(iter(diff))
