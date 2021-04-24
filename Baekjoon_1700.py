"""
@author: choihangyul
백준 1700번 - 멀티탭 스케줄링
예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면, 

키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기
키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 
디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다.

입력
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 
두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다. 

출력
하나씩 플러그를 빼는 최소의 횟수를 출력하시오. 
"""
import heapq
n, k = map(int, input().split())
use = list(map(int, input().split()))
q = []
cnt = 0
for i in range(k):
    if use[i] in q:
        continue
    if len(q) < n:
        heapq.heappush(q, use[i])
        continue
    
    idx_list = []
    for j in range(n):
        try:
            idx = use[i:].index(q[j])
        except:
            idx = 101
        idx_list.append(idx)
    del q[idx_list.index(max(idx_list))]
    heapq.heappush(q, use[i])
    cnt += 1
print(cnt)
