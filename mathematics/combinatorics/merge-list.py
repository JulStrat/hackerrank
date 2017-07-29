'''
https://www.hackerrank.com/challenges/merge-list
'''

from functools import reduce
from operator import mul
from sys import stdin
readl = stdin.readline

MOD = 10**9 + 7

def ncr(n, r):
  r = min(r, n - r)
  nom = reduce(mul, range(n, n - r, -1), 1)
  den = reduce(mul, range(1, r + 1), 1)
  return(nom//den)

def main():
    for __ in range(int(readl())):
        n, m = map(int, readl().split())
        print(ncr(n + m, n)%MOD)

if __name__ == '__main__':
    main()        
