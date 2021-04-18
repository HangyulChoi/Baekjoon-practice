#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: choihangyul
백준 2583번 - 영역 구하기
"""
"""입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. 
M, N, K는 모두 100 이하의 자연수이다. 
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 
오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 
모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 
입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 
둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
"""
import sys
sys.setrecursionlimit(10000)
m, n, k = map(int, input().split())
s = [[0]*n for _ in range(m)]
dy = [-1, 1, 0, 0]; dx  =  [0, 0, -1, 1]
cnt = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            s[j][k] = 1
for i in range(m):
    for j in range(n):
        if s[i][j] == 0:
            count = 1
            s[i][j] = 1
            q = [[i, j]]
            while q:
                x, y = q[0][0], q[0][1]
                del q[0]
                for k in range(4):
                    x1 = x + dx[k]
                    y1 = y + dy[k]
                    if 0 <= x1 < m and 0 <= y1 < n and s[x1][y1] == 0:
                        s[x1][y1] = 1
                        count += 1
                        q.append([x1, y1])
            cnt.append(count)
print(len(cnt))
cnt.sort()
print(*cnt)

#%%
# dfs
import sys
sys.setrecursionlimit(10000)
m, n, k = map(int, input().split())
s = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
ans = []
count = 0
def dfs(q, p):
    global count
    s[q][p] = 1
    count += 1
    for t in range(4):
        nx = p + dx[t]; ny = q + dy[t]
        if (0<=nx<m and 0<=ny<n and s[ny][nx]==0):
            dfs(ny, nx)

for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            s[j][k] = -1
            
for i in range(n):
    for j in range(m):
        if s[i][j] == 0:
            count = 0
            dfs(i, j)
            ans.append(count)
print(len(ans))
ans.sort()
print(*ans)
