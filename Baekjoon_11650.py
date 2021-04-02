#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:52:31 2021

@author: choihangyul

백준 11650번 - 좌표 정렬하기
"""

arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[0], x[1]))

for x in arr:
    print(str(x[0]) + " " + str(x[1]))
