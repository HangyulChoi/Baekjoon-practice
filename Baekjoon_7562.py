#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: choihangyul

백준 7562번 - 나이트의 이동
"""
"""
입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
"""
import sys
from collections import deque
# input = sys.stdin.readline
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y, x_, y_):
    q = deque()
    q.append([x, y])
    a[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == x_ and y==y_:
            return a[x][y] - 1
        for i in range(8):
            nx = x + dx[i]; ny = y + dy[i]
            if nx < 0  or nx >= l or ny < 0 or ny >= l:
                continue
            if a[nx][ny] ==  0:
                q.append([nx, ny])
                a[nx][ny] = a[x][y] + 1

t = int(input())    
for _ in range(t):
    l = int(input())
    a = [[0]*l for _ in range(l)]
    x, y = map(int, input().split())
    x_, y_ = map(int, input().split())
    if x==x_ and y==y_:
        print(0)
        continue
    print(bfs(x, y, x_, y_))