#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: choihangyul

백쥰  7575번 - 바이러스
"""
"""
입력
첫 번째 줄에는 감염된 프로그램의 개수 N 과 바이러스 코드 추정을 위한 최소 길이를 나타내는 정수 K 가 주어진다. 
단, 2 ≤ N ≤ 100이고, 4 ≤ K ≤ 1,000이다. 두 번째 줄부터 각 프로그램에 대한 정보가 주어지는데, 
먼저 i 번째 프로그램의 길이를 나타내는 정수 Mi가 주어지고, 
다음 줄에 프로그램 코드를 나타내는 Mi개의 양의 정수가 공백을 사이에 두고 주어진다. 
단, 10 ≤ Mi ≤ 1,000이고, 프로그램 코드를 나타내는 각 정수의 범위는 1이상 10,000 이하이다.

출력
바이러스 코드로 추정되는 부분이 있으면 YES를 출력하고, 없으면 NO를 출력해야 한다.
"""
# find()
import sys
# input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
for _ in range(n):
    m = int(input())
    arr.append(list(input().split()))
    
for j in range(len(arr[0]) - k + 1):
    tmp = arr[0][j:j+k]
    for x in range(1, n):
        y = ''.join(arr[x]).find(''.join(tmp))
        if y == -1:
            y = ''.join(arr[x][::-1]).find(''.join(tmp))
        if y == -1:
            break
        if x == n-1:
            print('YES')
            sys.exit()
print('NO')

#%%
# KMP 알고리즘
import sys
# input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
for _ in range(n):
    m = int(input())
    arr.append(list(input().split()))
    
def makeTable(tmp):
    table = [0] * k
    i = 0
    for j in range(1, k):
        while i > 0 and tmp[i] != tmp[j]:
            i = table[i-1]
        if tmp[i] == tmp[j]:
            i += 1
            table[j] = i
    return table

def KMP(string, find, tmp):
    i = 0
    for j in range(len(string)):
        while i>0 and string[j] != find[i]:
            i = tmp[i-1]
        if string[j] == find[i]:
            if i == k-1:
                return 1
            else:
                i += 1
    return 0

for j in range(len(arr[0]) - k + 1):
    table = makeTable(arr[0][j:j+k])
    for x in range(1, n):
        y = KMP(arr[x], arr[0][j:j+k], table)
        if not y:
            y = KMP(arr[x][::-1], arr[0][j:j+k], table)
        if not y:
            break
        if x == n-1:
            print('YES')
            sys.exit()
print('NO')
    