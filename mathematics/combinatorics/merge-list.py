#!/bin/python3
MOD = 10**9 + 7

from functools import reduce
from operator import mul
from sys import stdin
readl = stdin.readline

def ncr(n, r):
  r = min(r, n - r)
  nom = reduce(mul, range(n, n - r, -1), 1)
  denom = reduce(mul, range(1, r + 1), 1)
  return (nom//denom)

for _ in range(int(readl())):
  n, m = map(int, readl().split())
  print (ncr(n + m, n)%mod)
