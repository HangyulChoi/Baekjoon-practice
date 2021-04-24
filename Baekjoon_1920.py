"""
백준 1920번 - 수 찾기
@author: choihangyul

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""
# 시간 너무 오래 걸림
import sys
sys.setrecursionlimit(100000)
n = int(input())
target = list(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))
ans = []
for num in a:
    if num in target:
        ans.append(1)
    else:
        ans.append(0)
for k in range(m):
    print(ans[k])

#%% 
## set 
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n = input()
target = set(input().split())
m = input()
a = list(input().split())
for num in a:
    if num in target:
        print('1\n')
    else:
        print('0\n')