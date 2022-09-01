# Union-find Constructor- O(N)
# Find- O(1)
# Union- O(N)
# Connected- O(1)

class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
    
    def find(self,x):
        return self.root[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
                    
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
#Test Case
uf = UnionFind(10)

uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

print(uf.connected(1, 5))
print(uf.connected(3, 4))

uf.union(3, 4)
print(uf.connected(3, 4))