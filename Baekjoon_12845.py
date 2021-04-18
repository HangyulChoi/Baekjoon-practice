"""
@author: choihangyul
백준 12845번 - 모두의 마블
문제
두 카드는 인접한 카드여야 한다.
업그레이드 된 카드 A의 레벨은 변하지 않는다.
카드 합성을 할 때마다 두 카드 레벨의 합만큼 골드를 받는다.

입력
카드의 개수 n(0 < n ≤ 1,000)이 주어진다.
다음 줄에 각각 카드의 레벨 Li가 순서대로 주어진다. (0 < Li ≤ 100,000)

출력
영관이가 받을 수 있는 골드의 최댓값을 출력한다.
"""
import sys
sys.setrecursionlimit(1000)
n = int(input())
level = list(map(int, input().split()))
level.sort(reverse=True)
gold = 0
for i in range(1, n):
    tmp = level[0] + level[i]
    gold += tmp
print(gold)

#%% 
# 다른 방법
## 모든 카드 레벨을 더하고 제일 높은 레벨은 n-2번 더해지는 것 (총 n-1번 이니까)
import sys
sys.setrecursionlimit(1000)
n = int(input())
level = list(map(int, input().split()))
topLevel = max(level)
print(sum(level) + (n-2)*topLevel)