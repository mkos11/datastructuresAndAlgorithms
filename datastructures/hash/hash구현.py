# hash를 구현해보자
# 근데 파이썬은 dict() 제공해줘서 평소엔 이거 쓰면 됨

# 인덱스로 찾아갔을때 그 안에 원소들 순서가 의미가 있나? 그냥 집합 연산으로 처리해도 될듯?
# 충돌 발생하면 set()으로 처리해주자

# 이렇게 Global class 만들어놓고 상속해서 사용도 가능(클래스에서 전역변수 쓰고 싶을 때)
class Global:
    SIZE = 100
    PRIME_NUMBER = 2833

class Hash(Global):
    def __init__(self):
        self.table = [set() for _ in range(Global.SIZE)]

    def hash_func(self, key):
        # 파이썬 hash(key) 이런식으로 내장 함수 써줘도 되는데, 여기선 그냥 큰 소수 곱해서 직접 만들어보기
        return (sum(list(map(ord, key))) * Global.PRIME_NUMBER) % Global.SIZE

    # 집합으로 처리 하니까 뭔가 날로먹는 기분이지만... 동작 과정을 이해하는게 중요한거니까..
    def add(self, key, value):
        keyIdx = self.hash_func(key)
        self.table[keyIdx].add((key, value))

    def remove(self, key):
        keyIdx = self.hash_func(key)
        for k, v in sorted(self.table[keyIdx]):
            if key == k:
                self.table[keyIdx].remove((k, v))
                return

    def get(self, key):
        keyIdx = self.hash_func(key)
        for k, v in sorted(self.table[keyIdx]):
            if key == k: return v
        return None

if __name__ == "__main__":
    hash = Hash()
    hash.add('김', 113)
    hash.add('이', '113')
    hash.add('박', '123')
    print(hash.get('김'))
    hash.remove('김')
    hash.remove('김')
    print(hash.get('김'))
    print(hash.get('박'))
