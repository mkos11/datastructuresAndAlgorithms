# https://www.acmicpc.net/problem/6568

# 32바이트 메모리, 8비트 가산기, 5비트 pc
# pc => 다음에 실행되어야 하는 명령어의 주소
# 명령어: oooxxxxx, ooo:종류, xxxxx: 피연산자(값)
# 000 x: 메모리 주소 x에 가산기 값 저장
# 001 x: 메모리 주소 x의 값을 가산기로 불러옴
# 010 x: 가산기의 값이 0이면 pc값을 x로 변경
# 011: 아무 연산도 안함
# 100: 가산기 값 1 감소
# 101: 가산기 값 1 증가
# 110: pc값 x로 바꿈
# 111: 프로그램 종료
# pc, 가산기 초기 값 0
# 명령어 실행하기 전 pc 값 1 증가

from sys import*
input = lambda: stdin.readline().rstrip()

class Adder:
    def __init__(self, mem):
        self.pc = 0
        self.val = 0
        self.mem = mem
    def execute(self, command):
        self.pc = (self.pc + 1) % 32
        command_type = command[:3]
        operand = int(command[3:], 2)
        if command_type == '000':
            self.mem[operand] = self.padding(bin(self.val)[2:])
        elif command_type == '001':
            self.val = int(self.mem[operand], 2)
        elif command_type == '010':
            if self.val == 0: self.pc = operand
        elif command_type == '011':
            pass
        elif command_type == '100':
            self.val = (self.val + 255) % 256
        elif command_type == '101':
            self.val = (self.val + 1) % 256
        elif command_type == '110':
            self.pc = operand
        elif command_type == '111':
            return self.padding(bin(self.val)[2:])
        return self.execute(self.mem[self.pc])
    def padding(self, x):
        return ('0'*(8 - len(x))) + x
while True:
    try:
        mem = [input() for _ in range(32)]
        adder = Adder(mem)
        print(adder.execute(adder.mem[adder.pc]))
    except:
        break


