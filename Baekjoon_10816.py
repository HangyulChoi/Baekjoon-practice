"""
@author: choihangyul
백준 10816번 - 숫자카드2
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
"""
# from sys import stdin, stdout
## 시간초과
n = int(input())
target = list(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))
ans = [0] * m
for i in range(m):
    for j in range(n):
        if a[i] == target[j]:
            ans[i] += 1
print(*ans)      

#%%
## dic 사용
from sys import stdin
n = int(input())
target = list(map(int, stdin.readline().split()))
m = int(input())
a = list(map(int, stdin.readline().split()))
ans = []
dic = dict()
for num in target:
    try: dic[num] += 1
    except: dic[num] = 1
for i in a:
    try: ans.append(dic[i])
    except: ans.append(0)
    
print(*ans)    

#%%
## 위와 같은 논리 (짧은 코드)
n = int(input())
target = [int(i) for i in input().split()]
m = int(input())
a = [int(i) for i in input().split()]
hashmap = {}
for i in target:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
print(' '.join(str(hashmap[i]) if i in hashmap else '0' for i in a))


