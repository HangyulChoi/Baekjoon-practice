"""
@author: choihangyul
백준 2805번 - 나무 자르기
입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. 
(1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 
상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
"""
from sys import stdin
input = stdin.readline
n, l = map(int, input().split()) # n=나무 수, l=가져가려는 길이
tree = list(map(int, input().split()))
left = 1; right = max(tree)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in tree:
        if i > mid:
            cnt += (i - mid)
    if cnt >= l:
        left = mid + 1
    else:
        right = mid - 1
print(right)