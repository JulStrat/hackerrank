'''
https://www.hackerrank.com/challenges/antipalindromic-strings
'''
from sys import stdin
readl = stdin.readline

MOD = 10**9 + 7

def main():
    for __ in range(int(readl())):
        n, m = map(int, readl().split())
        r = m
        if n > 1:
            r *= m - 1
            r *= pow(m - 2, n - 2, MOD)
        print(r%MOD)

if __name__ == '__main__':
    main()
