#!/bin/python3

MOD = 10**9 + 7

from sys import stdin
readl = stdin.readline

for _ in range(int(readl())):
  n, m = map(int, readl().split())
  r = m
  if n > 1:
    r *= m - 1
    r *= pow(m - 2, n - 2, MOD)
  if r >= MOD:
    r %= MOD
  print (r)
