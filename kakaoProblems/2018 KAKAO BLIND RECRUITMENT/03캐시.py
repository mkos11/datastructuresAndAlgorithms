# https://programmers.co.kr/learn/courses/30/lessons/17680
# python 3.6~ dictionary 순서 입력순으로
# linked list + set() 으로 푸는게 처음 떠오르긴 하는데 linked list 구현하기 귀찮아서 생각해본게 dict()
CACHE_HIT, CACHE_MISS = 1, 5
def solution(cacheSize, cities):
    cache = {}
    ans = 0
    for city in cities:
        city = city.lower()
        if city in cache and cacheSize:
            ans += CACHE_HIT
            cache.pop(city)
        else:
            ans += CACHE_MISS
            if cacheSize == len(cache):
                print(cache.keys())
                for k in cache.keys():
                    cache.pop(k)
                    break
        cache[city] = True
    return ans

print(solution(	3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))