#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:44:36 2021

@author: choihangyul

백준 2490번 - 윷놀이
"""

"""
1 1 1 1 E
0 0 0 0 D
0 0 0 1 C
0 0 1 1 B
0 1 1 1 A
"""


def yut(arr):
    num_of_zero = arr.count(0)
    if num_of_zero  == 0:
        print('E')
    elif num_of_zero == 1:
        print('A')
    elif num_of_zero == 2:
        print('B')
    elif num_of_zero == 3:
        print('C')
    else:
        print('D')
    
for _  in range(3):
    arr = list(map(int, input().split()))
    yut(arr)


#%%
lst = [[1,2], [1,2], [1], [1], [2,1]]
print(list(set(map(tuple, lst))))

#%%

