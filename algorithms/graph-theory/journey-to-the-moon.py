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
xrange = range
nv, ne = map(int, readl().split())

ds = DisjointSet(xrange(nv))
for __ in xrange(ne):
  u, v = map(int, readl().split())
  ds.connect(u, v)
pairs = sum((ds.size(x)*(nv-ds.size(x)) for x in ds.root()))

print(pairs//2)    
