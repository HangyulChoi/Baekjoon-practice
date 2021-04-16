#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: choihangyul

백준 6603번 - 로또 
"""
"""
입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 
첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.
입력의 마지막 줄에는 0이 하나 주어진다. 

출력
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.
각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.
"""
# combinations 사용
from itertools import combinations

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    c = list(combinations(s, 6))
    for ans in c:
        for value in list(ans):
            print(value, end=' ')
        print()
    print()

#%%
# 위 코드 짧게 정리
from itertools import combinations
while True:
    arr =  list(input().split())
    if arr[0] == '0':
        break
    for i in combinations(arr[1:], 6):
        print(" ".join(i))
    print()