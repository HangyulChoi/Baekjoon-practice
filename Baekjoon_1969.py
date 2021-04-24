"""
@author: choihangyul
백분 1969번 - DNA
입력
첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다. 
N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력하고, 둘째 줄에는 그 Hamming Distance의 합을 출력하시오. 
그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다.
"""
import sys
sys.setrecursionlimit(1000)
n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]
dna_to_num = {'A':0, 'C':1, 'G':2, 'T':3}
num_to_dna = {0:'A', 1:'C', 2:'G', 3:'T'}
cnt = 0
res = ''
for i in range(m):
    check = [0, 0, 0, 0]
    for j in range(n):
        check[dna_to_num[dna[j][i]]] += 1
    idx = check.index(max(check))
    res += num_to_dna[idx]
    check[idx] = 0
    cnt += sum(check)
print(res)
print(cnt)   