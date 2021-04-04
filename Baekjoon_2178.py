#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:55:34 2021

@author: choihangyul

백준 2178번 - 미로 탐색 (BFS)
"""
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = [(0, 0)]
visited[0][0] = 1
while q:
    # print(q)
    x, y = q.pop(0)
    
    if (x == N-1) and (y == M-1):
        print(visited[x][y])
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<N) and (0<=ny<M):
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
        
