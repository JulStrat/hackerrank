#!/bin/python3

POSINF = float('inf')

n = int(input())
arr = list(map(int, input().split()))
mind = POSINF
lposd = [0]*(10**5 + 1)

for p in range(n):
  x = arr[p]
  lp = lposd[x]
  if lp: 
    d = p + 1 - lp
    if d < mind:
      mind = d
  lposd[x] = p + 1

print (mind if mind < POSINF else -1)
