from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([0 for _ in range(cacheSize)])
    if cache : 
        for city in cities : 
            if city.lower() not in cache : 
                cache.pop()
                cache.appendleft(city.lower())
                answer+=5
            else : 
                cache.remove(city.lower())
                cache.appendleft(city.lower())
                answer+=1
    
    else : 
        answer = 5*len(cities)
            
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
