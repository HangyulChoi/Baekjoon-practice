#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:01:27 2021

@author: choihangyul

백준 9613번 - GCD 합
"""

"""
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있다. 
각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 
입력으로 주어지는 수는 1,000,000을 넘지 않는다.

출력: 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
"""
import itertools
import sys

input = sys.stdin.readline

def gcd(x, y):
    return gcd(y, x%y) if y else x

for _ in range(int(input())):
    N, *arr = map(int, input().split())
    val = 0
    for a, b in itertools.combinations(arr, 2):
        val += gcd(a, b)
    print(val)

#%%
from itertools import combinations
list(combinations([1,2,3,4,5], 2))