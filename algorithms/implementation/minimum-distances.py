'''
https://www.hackerrank.com/challenges/minimum-distances
'''

from sys import stdin
readl = stdin.readline

POS_INF = float('inf')

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    mind = POS_INF
    lposd = [0]*(max(arr) + 1)
    d = POS_INF
    for p in range(n):
        x = arr[p]
        lp = lposd[x]
        if lp: 
            d = p + 1 - lp
        if d < mind:
            mind = d
        lposd[x] = p + 1
    
    print(mind if mind < POS_INF else -1)

if __name__ == '__main__':
    main()    
