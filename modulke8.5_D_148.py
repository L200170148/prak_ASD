import heapq
class Prior(object):
    def __init__(self):
        self.qlist= []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self, data, prior):
        heapq.heappush(self.qlist, (prior, data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(-1)
    
a = Prior()

a.enqueue('aa', 5)
a.enqueue('bb', 1)
a.enqueue('cc', 2)

print(a.qlist)
a.dequeue()
print(a.qlist)
