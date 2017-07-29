from sys import stdin
readl = stdin.readline

MOD = 10**9 + 7

def towerColoring(n):
    return pow(3, pow(3, n, MOD - 1), MOD)

def main():
    n = int(readl())
    r = towerColoring(n)
    print (r)

if __name__ == '__main__':
    main()
