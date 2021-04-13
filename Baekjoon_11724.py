#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:48:37 2021

@author: choihangyul

백준 11724번 - 연결 요소의 개수
"""
"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
"""
# DFS
import sys
sys.setrecursionlimit(10000) 

N, M = map(int, input().split())
matrix = [[] for _ in  range(N+1)]
visited = [False] * (N+1)
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

def DFS(v):
    visited[v] = True
    for e in matrix[v]:
        if not visited[e]:
            DFS(e)
 
for i in range(1, N+1):
    if not visited[i]:
        DFS(i)
        ans += 1

print(ans)        