def solution(people, limit):
    lst = []
    cnt = 0
    
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            if (people[i]+people[j]) <= limit:
                cnt+=1
    
    return len(people)-cnt