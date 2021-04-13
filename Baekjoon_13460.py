#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 23:53:19 2021

@author: choihangyul

백준 13460번 - 구술 탈출2 (삼성코테기출)
"""
"""
입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. 
'.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 
'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
"""
# BFS
import sys
from collections import deque
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[[[False]*M for _ in range(N)]for _ in range(M)]for _ in range(N)]
dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
q = deque()

def init():
    rx, ry, bx, by = [0] * 4
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'R':
                rx, ry = i, j
            elif matrix[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    c = 0
    while matrix[x+dx][y+dy] != '#' and matrix[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c

def BFS():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d> 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if matrix[nbx][nby] == 'O': # 실패조건(Blue가 구멍에 들어감)
                continue
            if matrix[nrx][nry] == 'O': # 성공
                print(d)
                return
            if nrx == nbx and nry == nby: # Red, Blue 겹쳤을 때
                if rc > bc : # 이동거리가 많은 걸 한 칸 뒤로
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1) # 실패
init()
BFS()



