#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:26:52 2021

@author: choihangyul

백준 2606번 - 바이러스 
"""
"""
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 
그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

입력: 첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력: 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
"""
# BFS 1
from collections import deque
N = int(input())
matrix = [0] * (N+1)
computer = [[] for _ in range(N+1)]

for i in range(int(input())):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

matrix[1] = 1
q = deque([1])
while q:
    x = q.popleft()
    for i in range(len(computer[x])):
        if matrix[computer[x][i]] == 0:
            q.append(computer[x][i])
            matrix[computer[x][i]] = 1

print(sum(matrix) - 1)            

#%%
# BFS 2
from sys import stdin
# input = stdin.readline
computer = {}
for i in range(int(input())):
    computer[i+1] = set()
for j in range(int(input())):
    a, b = map(int, input().split())
    computer[a].add(b)
    computer[b].add(a)

def BFS(start, computer):
    q = [start]
    while q:
        for i in computer[q.pop()]:
            if i not in visited:
                visited.append(i)
                q.append(i)

visited = []    
BFS(1, computer)
print(len(visited) - 1) 

#%%
# DFS
from sys import stdin
# input = stdin.readline
computer = {}
for i in range(int(input())):
    computer[i+1] = set()    
for j in range(int(input())):
    a, b = map(int, input().split())
    computer[a].add(b)
    computer[b].add(a)

def DFS(start, computer):
    for i in computer[start]:
        if i not in visited:
            visited.append(i)
            DFS(i, computer)

visited = []
DFS(1, computer)
print(len(visited) - 1)