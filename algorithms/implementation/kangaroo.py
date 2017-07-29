'''
https://www.hackerrank.com/challenges/kangaroo
'''

from sys import stdin
readl = stdin.readline

def main():
    x1, v1, x2, v2 = map(int, readl().split())
    if v1 > v2 and not (x2 - x1)%(v1 - v2):
        print('YES')
    else:
        print('NO')    

if __name__ == '__main__':
    main()
