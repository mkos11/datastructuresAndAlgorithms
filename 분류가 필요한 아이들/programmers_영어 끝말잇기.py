# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3

def solution(n, words):
    used = set()
    prev = ''
    for i, word in enumerate(words):
        if word in used: return [(i%n)+1, (i//n)+1]
        if prev == '' or prev == word[0]:
            prev = word[-1]
            used.add(word)
        else:
            return [(i%n)+1, (i//n)+1]
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(	5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))