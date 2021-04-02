#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:29:44 2021

@author: choihangyul

백준 2588번 - 곱셈
"""

a = int(input())
b = int(input())
arr_b = [int(i) for i in str(b)]
arr_b.reverse()

for i in range(len(arr_b)):
    print(a * arr_b[i])
print(a*b)


#%%
# arr = list(map(int, list(String)))
# arr = [int(i) for i in String]
