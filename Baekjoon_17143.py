"""
@author: choihangyul

백준 17143 - 낚시(삼성코테기출)
"""
"""
낚시왕이 오른쪽으로 한 칸 이동한다.
낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
상어가 이동한다.

입력
첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)
둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 상어의 정보는 다섯 정수 
r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. 
(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.

출력
낚시왕이 잡은 상어 크기의 합을 출력한다.
"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [0, -1, 1, 0, 0] # 좌우
dy = [0, 0, 0, 1, -1] # 상하
r, c, m = map(int, input().split())

di = {}
ans = 0

for i in range(m):
    x, y, s, d, z = map(int, input().split())
    string = "{} {}".format(x, y)
    di[string] = [s, d, z]

def move_shark(di, r, c):
    tmp = {}
    for k, v in di.items(): # (key, value) 받아옴
        # 좌표
        x, y = map(int, k.split())
        # 속력, 방향, 크기
        s, d, z = v

        # s 조절
        base_len = (r-1)*2 if d<3 else (c-1)*2
        s = (s % base_len)

        # move
        nx, ny =  x, y
        for _ in range(s):
            tmp_nx, tmp_ny = nx + dx[d], ny + dy[d]
            if tmp_nx < 1 or tmp_nx > r or tmp_ny < 1 or tmp_ny > c:
                if d % 2 == 0:
                    d -= 1
                else:
                    d += 1
            nx, ny = nx + dx[d], ny + dy[d]

        # check
        string = "{} {}".format(nx, ny)
        if string in tmp:
            if tmp[string][2] > z:
                continue
        tmp[string] = [s, d, z]
    return tmp

def catch_shark(idx, r, di):
    global ans
    for i in range(1, r+1):
        string = "{} {}".format(i, idx)
        if string in di:
            ans += di[string][2]
            del di[string]
            break

for i in range(1, c+1):
    catch_shark(i, r, di)
    di = move_shark(di, r, c)

print(ans)

