# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    return int(s.replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace('zero', '0'))

# print(solution(	"one4seveneight"))