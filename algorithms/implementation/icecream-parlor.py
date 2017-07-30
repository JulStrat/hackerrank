'''
https://www.hackerrank.com/challenges/icecream-parlor
'''

from sys import stdin
readl = stdin.readline

UB = 10**4

def main():
    for __ in xrange(int(readl())):
        m = int(readl())
        sz = int(readl())
        c = map(int, readl().split())
        dct = [0]*(UB + 1)
        mdl = 0
  
        for i in xrange(sz):
            cost = c[i]
            if not dct[cost]:
                dct[cost] = i + 1
            elif cost + cost == m and not mdl:
                mdl = i + 1
        
        for i in xrange(sz):
            cost = c[i]
            if dct[m - cost]:
                if cost + cost == m:
                    if mdl:
                        print i + 1, mdl
                        break
                else:
                    print i + 1, dct[m - cost]
                    break

if __name__ == '__main__':
    main()
