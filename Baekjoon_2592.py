#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 13:54:58 2021

@author: choihangyul

백준 2592번 - 대표값
"""

"""
열 개의 자연수가 주어질 때 이들의 평균과 최빈값을 구하는 프로그램을 작성하시오.

입력: 첫째 줄부터 열 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 
주어지는 자연수는 1,000 보다 작은 10 의 배수이다.

출력: 첫째 줄에는 평균을 출력하고, 둘째 줄에는 최빈값을 출력한다. 
최빈값이 둘 이상일 경우 그 중 하나만 출력한다. 평균과 최빈값은 모두 자연수이다.

"""

from collections import Counter

arr = [int(input()) for _ in range(10)]
val = Counter(arr).most_common()
print(sum(arr)//10)
print(val[0][0])