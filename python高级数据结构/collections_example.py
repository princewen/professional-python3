"""collections模块包含了内建类型之外的一些有用的工具，
例如Counter、defaultdict、OrderedDict、deque以及nametuple。
其中Counter、deque以及defaultdict是最常用的类。"""

"""1 Counter()"""
from collections import Counter
import re

"""如果你想统计一个单词在给定的序列中一共出现了多少次，诸如此类的操作就可以用到Counter。来看看如何统计一个list中出现的item次数："""
li = ["Dog",'Cat','Mouse',42,'Dog',42,'Cat','Dog']
print (Counter(li)) #Counter({'Dog': 3, 42: 2, 'Cat': 2, 'Mouse': 1})
"""若要统计一个list中不同单词的数目，可以这么用："""
print (len(Counter(li))) #4
"""如果需要对结果进行分组，可以这么做："""
a = Counter(li)
print ("{0}:{1}".format(a.values(),a.keys())) # dict_values([2, 1, 2, 3]):dict_keys([42, 'Mouse', 'Cat', 'Dog'])
print (a.most_common(3)) # [('Dog', 3), ('Cat', 2), (42, 2)]


string = """   Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nunc ut elit id mi ultricies
    adipiscing. Nulla facilisi. Praesent pulvinar,
    sapien vel feugiat vestibulum, nulla dui pretium orci,
    non ultricies elit lacus quis ante. Lorem ipsum dolor
    sit amet, consectetur adipiscing elit. Aliquam
    pretium ullamcorper urna quis iaculis. Etiam ac massa
    sed turpis tempor luctus. Curabitur sed nibh eu elit
    mollis congue. Praesent ipsum diam, consectetur vitae
    ornare a, aliquam a nunc. In id magna pellentesque
    tellus posuere adipiscing. Sed non mi metus, at lacinia
    augue. Sed magna nisi, ornare in mollis in, mollis
    sed nunc. Etiam at justo in leo congue mollis.
    Nullam in neque eget metus hendrerit scelerisque
    eu non enim. Ut malesuada lacus eu nulla bibendum
    id euismod urna sodales.  """

words = re.findall(r'\w+',string)
lower_words = [word.lower() for word in words]
words_count = Counter(lower_words)
#Counter({'sed': 5, 'in': 5, 'elit': 5, 'adipiscing': 4, 'mollis': 4, 'nulla': 3, 'non': 3, 'consectetur': 3, 'ipsum': 3, 'eu': 3, 'nunc': 3, 'id': 3, 'ornare': 2, 'at': 2, 'a': 2, 'congue': 2, 'ultricies': 2, 'praesent': 2, 'ut': 2, 'amet': 2, 'quis': 2, 'mi': 2, 'aliquam': 2, 'lorem': 2, 'lacus': 2, 'dolor': 2, 'etiam': 2, 'pretium': 2, 'magna': 2, 'urna': 2, 'metus': 2, 'sit': 2, 'facilisi': 1, 'malesuada': 1, 'curabitur': 1, 'neque': 1, 'posuere': 1, 'ullamcorper': 1, 'justo': 1, 'tellus': 1, 'tempor': 1, 'vestibulum': 1, 'diam': 1, 'nullam': 1, 'luctus': 1, 'sodales': 1, 'enim': 1, 'dui': 1, 'leo': 1, 'ante': 1, 'orci': 1, 'scelerisque': 1, 'pulvinar': 1, 'bibendum': 1, 'ac': 1, 'nibh': 1, 'lacinia': 1, 'vitae': 1, 'sapien': 1, 'pellentesque': 1, 'euismod': 1, 'turpis': 1, 'iaculis': 1, 'nisi': 1, 'massa': 1, 'eget': 1, 'vel': 1, 'augue': 1, 'feugiat': 1, 'hendrerit': 1})
print (words_count)

"""2 Deque"""
"""
Deque是一种由队列结构扩展而来的双端队列(double-ended queue)，队列元素能够在队列两端添加或删除。
因此它还被称为头尾连接列表(head-tail linked list)，尽管叫这个名字的还有另一个特殊的数据结构实现。

Deque支持线程安全的，经过优化的append和pop操作，在队列两端的相关操作都能够达到近乎O(1)的时间复杂度。
虽然list也支持类似的操作，但是它是对定长列表的操作表现很不错，而当遇到pop(0)和insert(0, v)这样既改变
了列表的长度又改变其元素位置的操作时，其复杂度就变为O(n)了。
"""
import time
from collections import deque

num = 100000
def append(c):
    for i in range(num):
        c.append(i)


def appendleft(c):
    if isinstance(c,deque):
        for i in range(num):
            c.appendleft(i)
    else:
        for i in range(num):
            c.insert(0,i)


def pop(c):
    for i in range(num):
        c.pop()

def popleft(c):
    if isinstance(c,deque):
        for i in range(num):
            c.popleft()
    else:
        for i in range(num):
            c.pop(0)


for container in [deque,list]:
    for operation in [append,appendleft,pop,popleft]:
        c = container(range(num))
        start = time.time()
        operation(c)
        elapsed = time.time()-start
        #Completed deque/append in 0.01348114013671875 seconds: 7417770.232031692 ops/sec
        # Completed deque/appendleft in 0.009357929229736328 seconds: 10686124.84076433 ops/sec
        # Completed deque/pop in 0.010100841522216797 seconds: 9900165.226832837 ops/sec
        # Completed deque/popleft in 0.009299039840698242 seconds: 10753798.42576212 ops/sec
        # Completed list/append in 0.009653806686401367 seconds: 10358608.08574745 ops/sec
        # Completed list/appendleft in 7.774795055389404 seconds: 12862.075371450605 ops/sec
        # Completed list/pop in 0.012604951858520508 seconds: 7933390.077361024 ops/sec
        # Completed list/popleft in 1.8698699474334717 seconds: 53479.655169204176 ops/sec
        print ("Completed {0}/{1} in {2} seconds: {3} ops/sec".format(container.__name__,operation.__name__,elapsed,num/elapsed))

"""另一个例子是执行基本的队列操作："""
q = deque(range(5))
q.append(5)
q.appendleft(6)
print (q)
print (q.pop())
print (q.popleft())
"""
rotate是队列的旋转操作，Right rotate(正参数)是将右端的元素移动到左端，而Left rotate(负参数)则相反。
"""
print (q.rotate(3))
print (q)
print (q.rotate(-1))
print (q)

"""3 Defaultdict"""
"""
这个类型除了在处理不存在的键的操作之外与普通的字典完全相同。
当查找一个不存在的键操作发生时，它的default_factory会被调用，
提供一个默认的值，并且将这对键值存储下来。其他的参数同普通的字典方法dict()一致，
一个defaultdict的实例同内建dict一样拥有同样地操作。

defaultdict对象在当你希望使用它存放追踪数据的时候很有用。
举个例子，假定你希望追踪一个单词在字符串中的位置，那么你可以这么做：
"""
from collections import defaultdict

s = "the quick brown fox jumps over the lazy dog"

words = s.split()
# value的类型是list
location = defaultdict(list)
for m, n in enumerate(words):
    location[n].append(m)

print (location)
for key,value in location.items():
    print (key,':',value)
"""是选择lists或sets与defaultdict搭配取决于你的目的，使用list能够保存你插入元素的顺序，而使用set则不关心元素插入顺序，它会帮助消除重复元素。"""

from collections import defaultdict

s = "the quick brown fox jumps over the lazy dog"

words = s.split()
location = defaultdict(set)
for m, n in enumerate(words):
    location[n].add(m)

print (location)
