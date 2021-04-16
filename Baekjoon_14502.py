#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: choihangyul

백준 14502번 - 연구소 (삼성코테기출)
"""
"""
바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
"""
import sys
sys.setrecursionlimit(10000)
# input = sys.stdin.readline

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
visited, safe, virus = [], -3, 100

def dfs(x, y):
    res = 1
    check[x][y] = True
    for dx, dy  in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny  < 0 or ny  >= m:
            continue
        if not (check[nx][ny] or MAP[nx][ny]):
            res += dfs(nx, ny)
    return res

def solve(wall, x, y):
    global virus, check
    if wall == 3:
        cnt = 0
        for i, j in  visited:
            cnt += dfs(i, j)
        virus = min(virus, cnt)
        return
    for i in range(x, n):
        k = y if i == x else 0
        for j in range(k, m):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                solve(wall+1, i, j+1)
                MAP[i][j] = 0
                
for i in range(n):
    for j in range(m):
        if MAP[i][j] != 1:
            safe += 1
        if MAP[i][j] == 2:
            visited.append((i, j))

solve(0, 0, 0)
print(safe-virus)





