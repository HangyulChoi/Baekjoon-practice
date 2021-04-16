#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: choihangyul

백준 12100번 - 2048(Easy) (삼성코테기출)
"""
"""
이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 
최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
"""
# 브루트포스, 시뮬레이션
from collections import deque
import sys
sys.setrecursionlimit(10000)
N = int(input())
board = [list(map(int, input().split()))for _ in range(N)]
ans = 0
q = deque()

def get(i, j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        if not board[i][j]:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x*2
            i, j = i + di, j + dj
        else:
            i, j = i + di, j + dj
            board[i][j] = x

def move(k):
    if k == 0:
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i, j)
            merge(N-1, j, -1, 0)
    elif k == 2:
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i, j)
            merge(i, N-1, 0, -1)
 
def solve(cnt):
    global board, ans
    if cnt == 5:
        for i in range(N):
            ans = max(ans, max(board[i]))
        return
    b = [x[:] for x in board]
    for k in range(4):
        move(k)
        solve(cnt+1)
        board = [x[:] for x in b]
 
solve(0)
print(ans)
    
    
    