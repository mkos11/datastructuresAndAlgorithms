# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
# 원래 엄청 간단하게 풀었던거 같은데? 일단 시간내에 풀고 리뷰 하면서 이쁘게 고치기
def padding(x, n):
    return ' ' * (n - len(x)) + x
def solution(n, arr1, arr2):
    convert = {'0': ' ', '1': '#'}
    ans = []
    for i in range(n):
        ans.append('')
        for x in bin(arr1[i] | arr2[i])[2:]:
            ans[i] += convert[x]
        ans[i] = padding(ans[i], n)
    return ans
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
print(	["######", "###  #", "##  ##", " #### ", " #####", "### # "])