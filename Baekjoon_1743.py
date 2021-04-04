#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:53:50 2021

@author: choihangyul

백준 1743번 - 음식물 피하기  (BFS)
"""
"""
문제
코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 
이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 
선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 

입력: 첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 
그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ 10,000)이 주어진다.  
그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.
좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다.

출력: 첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.
"""
from collections import deque

N, M, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 1

def BFS():
    q.append((i, j))
    t = 1
    visited[i][j] = 1
    while q:
        x, y = q.popleft()                
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0<=nx<N) and (0<=ny<M):
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    t += 1
    return t

q = deque()
ans = 0
for i in range(N):    
    for j in range(M):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            res= BFS()
            if res > ans: ans = res

print(ans)