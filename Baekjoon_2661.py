"""
@author: choihangyul
백준 2661번 - 좋은수열 (백트래킹)
문제
숫자 1, 2, 3으로만 이루어지는 수열이 있다. 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면, 그 수열을 나쁜 수열이라고 부른다. 
그렇지 않은 수열은 좋은 수열이다.


입력
입력은 숫자 N하나로 이루어진다. N은 1 이상 80 이하이다.

출력
첫 번째 줄에 1, 2, 3으로만 이루어져 있는 길이가 N인 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력한다. 
수열을 이루는 1, 2, 3들 사이에는 빈칸을 두지 않는다.
"""
n = int(input())
ans = []
def back_tracking(idx):
    global ans
    for i in range(1, (idx//2) + 1):
        if ans[idx-2*i:idx-i] == ans[idx-i:]:
            return
    if idx == n:
        print(*ans, sep='')
        exit(0)
    for i in range(1, 4):
        if ans and ans[-1] == i:
            continue
        ans = ans + [i]
        back_tracking(idx+1)

back_tracking(0)