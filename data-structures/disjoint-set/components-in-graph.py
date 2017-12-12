from copy import copy
class DisjointSet:

  def __init__(self, s=set()):
    self.__par = {x: x for x in s}
    self.__csz = dict.fromkeys(s, 1)
    self.__root = set(s)

  def root(self, x=None):
    if x is None:
      return(copy(self.__root))
    r = x
    while r != self.__par[r]:
      r = self.__par[r]
    while x != r:
      p = self.__par[x]
      self.__par[x] = r
      x = p
    return(r)

  def add(self, x):
    if x not in self.__par:
      self.__par[x] = x
      self.__csz[x] = 1
      self.__root.add(x)

  def connected(self, x, y):
    return(self.root(x) == self.root(y))

  def connect(self, x, y):
    rx, ry = self.root(x), self.root(y)
    if rx == ry:
      return(rx)
    if self.__csz[rx] < self.__csz[ry]:
      rx, ry = ry, rx
    self.__par[ry] = rx
    self.__csz[rx] += self.__csz[ry]
    self.__root.remove(ry)
    return(rx)

  def size(self, x=None):
    if x is None:
      return(len(self.__root))  
    else:
      return(self.__csz[self.root(x)])

  def __len__(self):
    return(len(self.__par))
    
from sys import stdin
readl = stdin.readline

n = int(readl())

ds = DisjointSet(xrange(1, 2*n+1))
for _ in xrange(n):
  p, q = map(int, readl().split())
  ds.connect(p, q)

print min(ds.size(r) for r in ds.root() if ds.size(r) > 1), max(ds.size(r) for r in ds.root())
