#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:51:40 2021

@author: choihangyul

백준 1260번 - DFS와 BFS
"""
"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력: 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.
"""

from sys import stdin

input = stdin.readline
N, M, V = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    matrix[start][end] = 1
    matrix[end][start] = 1

def BFS(v):
    visited = [v]
    queue = [v]
    
    while queue:
        num = queue.pop(0)
        for c in range(len(matrix[v])):
            if (matrix[num][c] == 1) and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

def DFS(v, visited):
    visited += [v]
    for c in range(len(matrix[v])):
        if (matrix[v][c] == 1) and (c not in visited):
            DFS(c, visited)
    return visited

print(*DFS(V, []))
print(*BFS(V))


#%%
from collections import deque
import sys

sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

def DFS(v):
    print(str(v), end=" ")
    if v == M:
        return
    else:
        for i in range(1, N+1):
            if MAP[v][i] == 1 and check[i] is False:
                check[i] = True
                DFS(i)

def BFS(v):
    Q = deque([])
    Q.append(v)    
    while Q:
        x = Q.popleft()
        if check_BFS[x] is False:
            check_BFS[x] = True
            print(x, end=" ")
            for i in range(1, N+1):
                if MAP[x][i] == 1 and check_BFS[i] is False:
                    Q.append(i)

N, M, V = map(int, input().split())
MAP = [[0] * (N+1) for _ in range(N+1)]
check = [False] * (N+1)
check_BFS = [False] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    MAP[start][end] = 1
    MAP[end][start] = 1

check[V] = True
DFS(V)
print()
BFS(V)
#%%

from queue import PriorityQueue

que = PriorityQueue()

que.put(1)
que.put(2)
que.put(3)
que.put(4)
que.put(5)


for i in range(len(que.queue)):
    print(que.queue[i], end=" ")
    
que.get()
que.queue