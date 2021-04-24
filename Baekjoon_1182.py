"""
@author: choihangyul
백준 1182번 - 부분수열의 합

문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
"""
from sys import stdin
input = stdin.readline
from itertools import combinations
n, s = map(int, input().split())
num = list(map(int, input().split()))
count = 0
for i in range(1, n+1):
    subset = list(combinations(num, i))
    for c in subset:
        if sum(c) == s:
            count += 1
print(count)

#%%
## dfs
## 위의 풀이보다 시간, 메모리 둘다 절반
# from sys import stdin
# input = stdin.readline
n, s = map(int, input().split())
num = list(map(int, input().split()))
count = 0
def dfs(idx, sumcheck):
    if idx >= n:
        return
    if sumcheck + num[idx] == s:
        global count
        count += 1
    dfs(idx+1, sumcheck)
    dfs(idx+1, sumcheck + num[idx])
dfs(0, 0)
print(count)