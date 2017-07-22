#!/bin/python

MOD = 10**9 + 7

def towerColoring(n):
    return pow(3, pow(3, n, MOD - 1), MOD)

n = int(raw_input().strip())
result = towerColoring(n)
print (result)
