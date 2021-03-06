#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:46:58 2021

@author: choihangyul

백준 1012번 - 유기농 배추 
"""
"""
배추밭에 해충 박멸을 위해 필요한 지렁이 개수 구하기

입력: 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.

출력: 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.
"""
# DFS
import sys 
sys.setrecursionlimit(10000) 
def dfs(x, y): 
    dx = [1, -1, 0, 0]; dy = [0, 0, 1, -1]
    for i in range(4): 
        nx = x + dx[i]; ny = y + dy[i] 
        if (0 <= nx < N) and (0 <= ny < M): 
            if matrix[nx][ny] == 1: 
                matrix[nx][ny] = -1 
                dfs(nx, ny) 

T = int(input()) 
for _ in range(T):
    M, N, K = map(int, input().split()) 
    matrix = [[0]*M for _ in range(N)] 
    cnt = 0 
    for _ in range(K): 
        m, n = map(int, input().split()) 
        matrix[n][m] = 1 
    for i in range(N):
        for j in range(M): 
            if matrix[i][j] > 0: 
                dfs(i, j) 
                cnt += 1 
    print(cnt)

#%%
# BFS
from collections import deque 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j, visited):
    cnt = 0
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))

    return cnt
                                
t = int(input())
for _ in range(t):
    m, n, k = list(map(int, input().split(' ')))
    arr = [[[0] for _ in range(m)] for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split(' '))
        arr[y][x] = 1

    sol = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                  sol += bfs(i, j, visited)      
    print(sol)

