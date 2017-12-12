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
edges = [list(map(int, readl().split())) for __ in xrange(ne)]
edges.sort(key = lambda x: (x[2], x[0]+x[1]))
ds = DisjointSet(xrange(1, nv+1))
mst_weight = 0
i = 0
while ds.size() > 1:
  p, q = edges[i][0], edges[i][1]
  if not ds.connected(p, q):
    ds.connect(p, q)
    mst_weight += edges[i][2]
  i += 1  
print(mst_weight)    
