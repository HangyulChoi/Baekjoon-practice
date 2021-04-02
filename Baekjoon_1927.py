#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:39:12 2021

@author: choihangyul

백준 1927번 - 최소 힙
"""

"""
입력: 
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
입력되는 자연수는 231보다 작다.

출력: 입력에서 0이 주어진 회수만큼 답을 출력한다. 
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
"""

import heapq
import sys

arr = []

# input = sys.stdin.readline
# print = sys.stdout.write

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, num)
    