#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:38:58 2021

@author: choihangyul

백준 10825번 - 국영수
"""
"""
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 
(단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

"""
arr = []
for _ in range(int(input())):
    arr.append(list(map(str, input().split())))

arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in arr:
    print(x[0])

#%%
a, b = map(int, input().split())
print(a+b)
