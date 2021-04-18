"""
@author: choihangyul
백준 11000번 - 강의실 배정 (Greedy algorithm)
"""
"""
Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
이후 N개의 줄에 Si, Ti가 주어진다. (1 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.
"""
import heapq
# import sys
# input = sys.stdin.readline
n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n)]
timetable.sort(key=lambda x:x[0])
q = []
for i in range(n):
    if len(q) != 0 and q[0] <= timetable[i][0]:
            heapq.heappop(q)
    heapq.heappush(q, timetable[i][1])
print(len(q))

#%%
# 시간 초과 (해결과정 흐름만 확인하기)
import sys
input = sys.stdin.readline
n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n)]
timetable.sort()
end = [0]
for i in range(n):
    if timetable[i][0] >= min(end):
        end.remove(min(end))
        end.append(timetable[i][1])
    else:
        end.append(timetable[i][1])
print(len(end))