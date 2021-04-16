#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: choihangyul

백준 14500번 - 테트로미노(삼성코테기출)
"""
"""
입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. 
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 
입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
"""
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
board =  [list(map(int, input().split())) for _ in range(N)]
tetris = [
    [(0, 1), (1, 0), (1, 1)],
    [(0,1), (0,2), (0,3)],
    [(1,0), (2,0), (3,0)],
    [(0,1), (0,2), (1,0)],
    [(0,1), (0,2), (-1,2)],
    [(1,0), (1,1), (1,2)],
    [(0,1), (0,2), (1,2)],
    [(1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1)],
    [(0,1), (1,0), (2,0)],
    [(1,0), (2,0), (2,-1)],
    [(1,0), (1,1), (2,1)],
    [(0,1), (1,0), (-1,1)],
    [(0,1), (1,0), (1,-1)],
    [(0,1), (1,1), (1,2)],
    [(0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,-1)],
    [(1,0), (2,0), (1,-1)],
    [(1,0), (1,1), (2,0)]
]
def tetromino(x, y):
    global ans
    for i in range(19): # 5개 블록들 회전, 대칭해서 나오는 경우의 수가 19개
        s = board[x][y]
        for j in range(3):
            try:
                nx = x + tetris[i][j][0]
                ny = y + tetris[i][j][1]
                s += board[nx][ny]
            except IndexError:
                continue
        ans = max(ans, s)

def solve():
    for i in range(N):
        for j in range(M):
            tetromino(i, j)

ans = 0
solve()
print(ans)
