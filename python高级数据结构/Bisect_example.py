"""
bisect模块能够提供保持list元素序列的支持。它使用了二分法完成大部分的工作。
它在向一个list插入元素的同时维持list是有序的。在某些情况下，
这比重复的对一个list进行排序更为高效，并且对于一个较大的list来说，
对每步操作维持其有序也比对其排序要高效。
"""

import bisect

a = [(0, 100), (150, 220), (500, 1000)]
bisect.insort_right(a,(250,600))
#[(0, 100), (150, 220), (250, 600), (500, 1000)]
print (a)

"""
我们可以使用bisect()函数来寻找插入点：
bisect(sequence, item) => index 返回元素应该的插入点，但序列并不被修改。
"""
bisect.insort_right(a,(399,800))
print (a)
print (bisect.bisect(a,(550,1200)))#5





