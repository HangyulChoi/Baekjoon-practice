#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 23:07:12 2021

@author: choihangyul

백준 2667번 - 단지번호붙이기
"""
"""
입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""
# DFS
import sys
sys.setrecursionlimit(10000) 

# 단지 만들기 
N = int(input())
matrix = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        matrix[i][j] = int(matrix[i][j])

# read = lambda : sys.stdin.readline().strip()
# matrix = [list(map(int, list(read()))) for _ in range(N)]

def DFS(matrix, cnt, x, y):
    matrix[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if matrix[nx][ny] == 1:
            cnt = DFS(matrix, cnt + 1, nx, ny)
    return cnt

ans = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            ans.append(DFS(matrix, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)