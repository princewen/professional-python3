"""
heapq模块使用一个用堆实现的优先级队列。堆是一种简单的有序列表，并且置入了堆的相关规则。

堆是一种树形的数据结构，树上的子节点与父节点之间存在顺序关系。二叉堆(binary heap)能够用
一个经过组织的列表或数组结构来标识，在这种结构中，元素N的子节点的序号为2*N+1和2*N+2(下标始于0)。
简单来说，这个模块中的所有函数都假设序列是有序的，所以序列中的第一个元素(seq[0])是最小的，
序列的其他部分构成一个二叉树，并且seq[i]节点的子节点分别为seq[2*i+1]以及seq[2*i+2]。
当对序列进行修改时，相关函数总是确保子节点大于等于父节点。

"""

import heapq

heap = []

for value in [20,10,30,50,40]:
    heapq.heappush(heap,value)
# 10
# 20
# 30
# 40
# 50
while heap:
    print (heapq.heappop(heap))

"""heapq模块有两个函数nlargest()和nsmallest()，顾名思义，让我们来看看它们的用法。"""
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print (heapq.nlargest(3,nums))
print (heapq.nsmallest(3,nums))


"""两个函数也能够通过一个键参数使用更为复杂的数据结构，例如："""
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
#
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]

print (heapq.nlargest(3,portfolio,key = lambda x:x['price']))
print (heapq.nsmallest(3,portfolio,key = lambda x:x['price']))

"""来看看如何实现一个根据给定优先级进行排序，并且每次pop操作都返回优先级最高的元素的队列例子。"""


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print (q)
print (q.pop()) # Item('bar')
print (q.pop())  # Item('spam')
print (q.pop())  # Item('foo')
print (q.pop())  # Item('grok')


